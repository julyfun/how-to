#set page(paper: "us-letter")
#set heading(numbering: "1.1.")
#set figure(numbering: "1")

// 这是注释
#figure(image("sjtu.png", width: 50%), numbering: none) \ \ \

#align(center, text(17pt)[
  *Database System Concepts - Assignment (I)* \ \
  #table(
      columns: 2,
      stroke: none,
      rows: (2.5em),
      // align: (x, y) =>
      //   if x == 0 { right } else { left },
      align: (right, left),
      [Name:], [Junjie Fang],
      [Student ID:], [521260910018],
      [Date:], [2024/3/4],
      [Score:], [],
    )
])

#pagebreak()

#set page(header: align(right)[
  DB Lab1 Report - Junjie FANG
], numbering: "1")

#show outline.entry.where(
  level: 1
): it => {
  v(12pt, weak: true)
  strong(it)
}

#outline(indent: 1.5em)

= Problem 1


