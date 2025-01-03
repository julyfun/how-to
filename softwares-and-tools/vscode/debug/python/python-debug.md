This method is verified!

https://code.visualstudio.com/docs/python/debugging

https://stackoverflow.com/questions/51244223/visual-studio-code-how-debug-python-script-with-arguments

## 开始

vscode cmd: show run and debug.

click 'create launch.json'

A file is created.

If you wanna run shell script for python like this:

```sh
CUDA_VISIBLE_DEVICES=0 python cloth_funnels/run_sim.py \
name="demo-single" \
load=models/longsleeve_canonicalized_alignment.pth \
eval_tasks=assets/tasks/longsleeve-single.hdf5 \
eval=True \
num_processes=1 \
episode_length=10 \
wandb=disabled \
fold_finish=True \
dump_visualizations=True

```

Add args like:

```json
{
    // Use IntelliSense to learn about possible attributes.
    // Hover to view descriptions of existing attributes.
    // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: 当前文件",
            "type": "python",
            "request": "launch",
            "program": "${file}",
            "console": "integratedTerminal",
            "args": ["name=\"demo-single\"",
                "load=models/longsleeve_canonicalized_alignment.pth",
                "eval_tasks=assets/tasks/longsleeve-single.hdf5",
                "eval=True",
                "num_processes=1",
                "episode_length=10",
                "wandb=disabled",
                "fold_finish=True",
                "dump_visualizations=True"],
        }
    ]
}
```

Switch to the file you want to run (as in launch.json we by default designate "Run current file", so you have to switch to the exact file to run).

Add a breakpoint,

Click the green delta in "Run python and debug" menu,

Everything is well! And watch params in the menu!

## Remote

Using vscode-ssh is also ok to run python debug in remote machine.

