RuntimeError: 
            Attempt to start a new process before the current process
            has finished its bootstrapping phase.
            This probably means that you are on Windows and you have
            forgotten to use the proper idiom in the main module:
                if __name__ == '__main__':
                    freeze_support()
                    ...
            The "freeze_support()" line can be omitted if the program
            is not going to be frozen to produce a Windows executable.

## Solution

As the note said, add `__main__`` guard and add `freeze_support()` and the begining.

```
if __name__ == "__main__":
    multiprocessing.freeze_support()
    start = time.time()
    ...
```

Ref:

https://discuss.pytorch.org/t/runtimeerror-an-attempt-has-been-made-to-start-a-new-process-before-the-current-process-has-finished-its-bootstrapping-phase/145462/9

