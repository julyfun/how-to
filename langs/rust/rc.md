## Rc

rust 的函数参数类型为非引用时，将会吃掉参数的所有权。

当不需要 share 时，使用 Box，否则使用 Rc。

```rust
trait Output {
    fn output(&self);
}

struct Foo {
    x: i32,
}

impl Output for Foo {
    fn output(&self) {
        println!("{}", self.x);
    }
}

fn func(v: &mut Vec<Rc<dyn Output>>) {
    let foo = Foo { x: 1 };
    let bar = Bar { y: 2.0 };
    v.push(Rc::new(foo));
    v.push(Rc::new(bar));
}
```

神奇的是，Rc<Type> 可以直接调用 Type 的成员函数，我也不知道为什么。

