Rustln:

由于 Rust 的 mutable 特性，一个结构体中的字段，要么全都是 immutable，要么全部是 mutable，不支持针对部分字段进行设置。比如，在一个 struct 中，可能只有个别的字段需要修改，而其他字段并不需要修改，为了一个字段而将整个 struct 变为 &mut 也是不合理的。

所以，实现 内部可变性 的 Cell 和 RefCell 正是为了解决诸如这类问题存在的，通过它们可以实现 struct 部分字段可变，而不用将整个 struct 设置为 mutable。

