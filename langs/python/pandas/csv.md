https://blog.csdn.net/AwesomeP/article/details/124975721

## 不将首行当作 index（标题）

```
df = pd.read_csv('example.csv', header=None)
```

## Iterator

```
first_5_rows = df.head(5)

# 绘制每行数据，使用semilogy绘制对数坐标轴
for index, row in first_5_rows.iterrows():
    plt.semilogy(row.index, row.values, label=f'Row {index}')
```

