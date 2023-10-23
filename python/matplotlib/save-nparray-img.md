```py
        # print("[jf]", obs.size())
        # [jf] torch.Size([4, 480, 480])
        def func():
            ...
            print("[jf] #20 save im")
            import matplotlib.pyplot as plt
            arr = obs[:3].cpu().numpy()
            arr = (arr * 255).astype(np.uint8)
            img = np.transpose(arr, (1, 2, 0))
            SAVE_PATH = '/home/junjie/repos/cloth-funnels/dist'
            plt.imsave(os.path.join(SAVE_PATH, f'{time.strftime("%Y-%m-%d %H-%M-%S")+" "+str(time.time())}.png'), img)

        # func()
```
