```
for idx, row in f5.iterrows():
    print(type(row.values))
    plt.plot(DIMS, row.values + EPS, label=f"{FUNC_NAMES[idx]}")
    # 这是对数轴
    # plt.semilogy(DIMS, row.values + EPS, label=f"{FUNC_NAMES[idx]}")

# 加上图例（就是图标）
plt.legend()
plt.xlabel('log10(Dimension)')
plt.ylabel('Time(s)')

plt.show()
```
