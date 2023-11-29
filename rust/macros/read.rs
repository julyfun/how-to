#[allow(unused_macros)]
macro_rules! read {
    ($out:ident as $type:ty) => {
        let mut inner = String::new();
        std::io::stdin().read_line(&mut inner).expect("a String");
        let $out = inner.trim().parse::<$type>().expect("parsable");
    };
}

#[allow(unused_macros)]
macro_rules! read_str {
    ($out:ident) => {
        let mut inner = String::new();
        std::io::stdin().read_line(&mut inner).expect("a String");
        let $out = inner.trim();
    };
}

#[allow(unused_macros)]
macro_rules! read_vec {
    ($out:ident as $type:ty) => {
        let mut inner = String::new();
        std::io::stdin().read_line(&mut inner).unwrap();
        let $out = inner
            .trim()
            .split_whitespace()
            .map(|s| s.parse::<$type>().unwrap())
            .collect::<vec<$type>>();
    };
}

fn main() {
    read!(x as u32);
    read!(y as f64);
    read!(z as char);
    println!("{} {} {}", x, y, z);

    read_vec!(v as u32); // Reads space separated integers and stops when newline is encountered.
    println!("{:?}", v);
}
