```
struct_for cannot be nested inside a kernel
```


## problem

In a ti.kernel

```py

        if self.lift_up_is_on[None] == 1:
            lift_up = ti.Vector([0.0, 50.0, 0.0])
            for k in self.TO_LIFT: # this is a ti.ndarray
                i = self.TO_LIFT[k]
                self.v_soft[i][1] = max(0, self.v_soft[i][1])
                self.v_soft[i] += lift_up * self.dt
                self.highlight_vertex(i)
```

An error was raised when compiling taichi code. 

## solution

```py

        if self.lift_up_is_on[None] == 1:
            lift_up = ti.Vector([0.0, 50.0, 0.0])
            for k in range(self.TO_LIFT.shape[0]):
                i = self.TO_LIFT[k]
                self.v_soft[i][1] = max(0, self.v_soft[i][1])
                self.v_soft[i] += lift_up * self.dt
                self.highlight_vertex(i)
```

## why

Don't know.

