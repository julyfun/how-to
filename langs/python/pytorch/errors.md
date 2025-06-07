- [25.6.7]
    - `RuntimeError: Input type (torch.FloatTensor) and weight type (torch.cuda.FloatTensor) should be the same or input should be a MKLDNN tensor and weight is a dense tensor`
    - [ok, problem is] Tensor 不在一个设备上.
    ```
    net = BasicUNet(in_channels=1, out_channels=1).to(<gpu>)
    x = torch.randn(8, 1, 28, 28)
    net(x)
    ```
