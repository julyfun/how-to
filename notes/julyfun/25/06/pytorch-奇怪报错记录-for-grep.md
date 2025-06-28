---
reliability: "20% (author)"
os: "Linux julyfun-4070s-ubuntu 6.8.0-60-generic #63~22.04.1-Ubuntu SMP PREEMPT_DYNAMIC Tue Apr 22 19:00:15 UTC 2 x86_64 x86_64 x86_64 GNU/Linux"
author: "julyfun-4070s-ubuntu2204"
assume-you-know: [computer]
date: 2025-06-17
title: "pytorch 奇怪报错记录 for grep"
tags: []
---

# pytorch 奇怪报错记录 for grep

## 25.6.17

```
---------------------------------------------------------------------------
RuntimeError                              Traceback (most recent call last)
File /home/julyfun/Documents/GitHub/julyfun/how-to/notes/julyfun/技术学习/diffusion-models-class/unit2-02_class_conditioned_diffusion_model_example.py:3
      1 # %%
      2 @run
----> 3 def func():
      4     net = ClassConditionedUnet(num_classes=10).to(device)
      5     img = torch.randn(3, 1, 28, 28).to(device)

File ~/Documents/GitHub/julyfun/robotoy/robotoy/ziglike/test.py:58, in run(func)
     57 def run(func):
---> 58     func()

File /home/julyfun/Documents/GitHub/julyfun/how-to/notes/julyfun/技术学习/diffusion-models-class/unit2-02_class_conditioned_diffusion_model_example.py:4
      2 @run
      3 def func():
----> 4     net = ClassConditionedUnet(num_classes=10).to(device)
      5     img = torch.randn(3, 1, 28, 28).to(device)
      6     cls = torch.tensor([0, 1, 9]).to(device)

File ~/Documents/GitHub/diffusion-models-class/.venv/lib/python3.10/site-packages/torch/nn/modules/module.py:1355, in Module.to(self, *args, **kwargs)
   1352         else:
   1353             raise
-> 1355 return self._apply(convert)

File ~/Documents/GitHub/diffusion-models-class/.venv/lib/python3.10/site-packages/torch/nn/modules/module.py:915, in Module._apply(self, fn, recurse)
    913 if recurse:
    914     for module in self.children():
--> 915         module._apply(fn)
    917 def compute_should_use_set_data(tensor, tensor_applied):
    918     if torch._has_compatible_shallow_copy_type(tensor, tensor_applied):
    919         # If the new tensor has compatible tensor type as the existing tensor,
    920         # the current behavior is to change the tensor in-place using `.data =`,
   (...)
    925         # global flag to let the user control whether they want the future
    926         # behavior of overwriting the existing tensor or not.

File ~/Documents/GitHub/diffusion-models-class/.venv/lib/python3.10/site-packages/torch/nn/modules/module.py:942, in Module._apply(self, fn, recurse)
    938 # Tensors stored in modules are graph leaves, and we don't want to
    939 # track autograd history of `param_applied`, so we have to use
    940 # `with torch.no_grad():`
    941 with torch.no_grad():
--> 942     param_applied = fn(param)
    943 p_should_use_set_data = compute_should_use_set_data(param, param_applied)
    945 # subclasses may have multiple child tensors so we need to use swap_tensors

File ~/Documents/GitHub/diffusion-models-class/.venv/lib/python3.10/site-packages/torch/nn/modules/module.py:1341, in Module.to.<locals>.convert(t)
   1334     if convert_to_format is not None and t.dim() in (4, 5):
   1335         return t.to(
   1336             device,
   1337             dtype if t.is_floating_point() or t.is_complex() else None,
   1338             non_blocking,
   1339             memory_format=convert_to_format,
   1340         )
-> 1341     return t.to(
   1342         device,
   1343         dtype if t.is_floating_point() or t.is_complex() else None,
   1344         non_blocking,
   1345     )
   1346 except NotImplementedError as e:
   1347     if str(e) == "Cannot copy out of meta tensor; no data!":

RuntimeError: CUDA error: device-side assert triggered
CUDA kernel errors might be asynchronously reported at some other API call, so the stacktrace below might be incorrect.
For debugging consider passing CUDA_LAUNCH_BLOCKING=1
Compile with `TORCH_USE_CUDA_DSA` to enable device-side assertions.
```


- context see above.
- [ok, but why] 重启 kernel 运行就没问题了.

