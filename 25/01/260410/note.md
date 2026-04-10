
---
    pub const PAT: &str =
        r#"'(?:[sdmt]|ll|ve|re)| ?\p{L}+| ?\p{N}+| ?[^\s\p{L}\p{N}]+|(?:\r?\n)+|[^\S\r\n]+"#;
        let pat = " ?(?:".to_string() + special_tokens1.join("|").as_str() + ")(?:\\s)?|" + PAT;

<The> 数量 4541

---
    pub const PAT: &str =
        r#"'(?:[sdmt]|ll|ve|re)| ?\p{L}+| ?\p{N}+| ?[^\s\p{L}\p{N}]+|\s+(?!\S)|\s+"#;

        let pat = " ?(?:".to_string() + special_tokens1.join("|").as_str() + ")(?:\\s)?|" + PAT;

依然 4541

---

2.txt
    pub const PAT: &str =
        r#"'(?:[sdmt]|ll|ve|re)| ?\p{L}+| ?\p{N}+| ?[^\s\p{L}\p{N}]+|\s+(?!\S)|\s+"#;
        let pat = " ?(?:".to_string() + special_tokens1.join("|").as_str() + ")|" + PAT;
这样 4538 但是
At index 627 diff: (b' g', b'ive') != (b'\n', b'\n') 
这是能匹配 \n\n，但是数量偏少

give: 610
\n\n: 607（实际 614）即 `(?<!>)\n\n`. 忽略了一些 :\n\n 和 `.\n\n`，不过统计了所有 |>\n\n\n (2.txt)

观察发现有 
```
match <said>
match <:>
match <
>
match <
>
match <said>
match <.>
match <
>
match <
>
```
说明遇到 `.\n\n` 会拆开成 3 个
---

(?<! )The : 4538 （实际）

不是空格，也不是 \n: 146
(?<![" \n])The: 1

\nThe: 4392

