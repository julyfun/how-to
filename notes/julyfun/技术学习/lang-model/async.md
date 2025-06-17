- 大致概念：[80%-sure] 以 Rust 为例，运行到 func().await 时 (func 为 async fn)
    - func() 内部代码完全交由 async runtime 处理
    - func() 内部通常有等待IO/GPU/定时器的异步部分。**这些部分不由 CPU 负责运算，不应该让 CPU 干等着，所以才写成异步函数.**
    - 如果 func() 内部全是同步代码，没有 .await 或手动挂起点，写成异步（async fn）没有实际意义
        - 它是不会挂起的，会同步执行完毕。

- 轮询
    - poll 调用次数不是固定的，取决于任务的完成时机和外部事件。

## Rust

```rust
async fn my_async(x: u32) -> u32 {
    let a = x + 1;
    a * 2
}

let fut = my_async(10);
fut.await; // 开始轮询
```

- 编译器生成的大致逻辑:

```rust
enum MyAsyncState {
    Start { x: u32 },
    Done,
}

struct MyAsyncFuture {
    state: MyAsyncState,
}

impl Future for MyAsyncFuture {
    type Output = u32;

    fn poll(mut self: Pin<&mut Self>, _cx: &mut Context<'_>) -> Poll<u32> {
        match self.state {
            MyAsyncState::Start { x } => {
                let a = x + 1;
                let result = a * 2;
                self.state = MyAsyncState::Done;
                Poll::Ready(result)
            },
            MyAsyncState::Done => {
                panic!("polled after completion");
            }
        }
    }
}
```

- 另一个例子：

```rust
async fn my_async(x: u32) -> u32 {
    let a = x + 1;
    tokio::time::sleep(Duration::from_secs(3)).await;
    a * 2
}
```

```rust
enum MyAsyncState {
    Start { x: u32 },
    Waiting { a: u32, sleep_future: Sleep },
    Done,
}

impl Future for MyAsyncFuture {
    type Output = u32;

    fn poll(mut self: Pin<&mut Self>, cx: &mut Context<'_>) -> Poll<u32> {
        loop {
            match self.state {
                MyAsyncState::Start { x } => {
                    let a = x + 1;
                    let sleep_future = tokio::time::sleep(Duration::from_secs(3));
                    self.state = MyAsyncState::Waiting { a, sleep_future };
                },
                MyAsyncState::Waiting { a, ref mut sleep_future } => {
                    match Pin::new(sleep_future).poll(cx) {
                        Poll::Pending => return Poll::Pending,
                        Poll::Ready(_) => {
                            let result = a * 2;
                            self.state = MyAsyncState::Done;
                            return Poll::Ready(result);
                        }
                    }
                },
                MyAsyncState::Done => {
                    panic!("polled after completion");
                }
            }
        }
    }
}
```

