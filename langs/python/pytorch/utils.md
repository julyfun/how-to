## print parameters num

sum(p.numel() for p in model.parameters())

```python
def numel(model):
    return sum(p.numel() for p in model.parameters())
```

