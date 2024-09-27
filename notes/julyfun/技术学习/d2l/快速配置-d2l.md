```
mkdir -p ~/miniconda3
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
rm ~/miniconda3/miniconda.sh

conda init
exec bash
conda create --name d2l python=3.9 -y
conda deactivate
conda activate d2l
pip install torch -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install torchvision -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install d2l==0.17.6 -i https://pypi.tuna.tsinghua.edu.cn/simple
--- 本地
scp /Users/florian/code/d2l-zh/pytorch.zip connect.westc.gpuhub.com:~
--- remote
unzip pytorch.zip
```
