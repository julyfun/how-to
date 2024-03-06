```rs
use std::thread;

fn is_prime(n: i32) -> bool {
    let mut result = true;
    for k in 2..(n as f32).powf(0.5) as i32 + 1 {
        if n % k == 0 {
            result = false;
            break;
        }
    }
    result
}

fn count_primes(start: i32, end: i32) -> i32 {
    let mut count = 0;
    for k in start..end {
        if is_prime(k) {
            count += 1;
        }
    }
    count
}

fn main() {
    const THREAD_COUNT: usize = 15; // 设置线程数量

    let n = 1e8 as i32;
    let chunk_size = n / THREAD_COUNT as i32;

    let mut handles = vec![];

    for i in 0..THREAD_COUNT {
        let start = i as i32 * chunk_size + 2;
        let end = if i == THREAD_COUNT - 1 {
            n
        } else {
            (i + 1) as i32 * chunk_size + 2
        };

        let handle = thread::spawn(move || count_primes(start, end));
        handles.push(handle);
    }

    let mut total_count = 0;

    for handle in handles {
        total_count += handle.join().unwrap();
    }

    println!("{}", total_count);
}
```

