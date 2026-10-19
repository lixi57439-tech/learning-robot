# -*- coding: utf-8 -*-
# 用最经典的手写数字数据集，验证 PyTorch 能正常训练
import torch, torch.nn as nn, torch.optim as optim
from torchvision import datasets, transforms

# ① 数据：MNIST = 6 万张 28x28 的手写数字图（0-9），用来验证环境
transform = transforms.Compose([transforms.ToTensor()])      # 把图片变成张量（数字矩阵）
train = datasets.MNIST(".", train=True, download=True, transform=transform)
loader = torch.utils.data.DataLoader(train, batch_size=64, shuffle=True)   # 分批喂数据

# ② 模型：三层"全连接网络"（阶段 5 会讲清每一层）
net = nn.Sequential(nn.Flatten(), nn.Linear(784, 128), nn.ReLU(), nn.Linear(128, 10))

# ③ 优化器：负责"根据误差调整模型参数"
opt = optim.Adam(net.parameters())

# ④ 训练循环：反复"预测 → 算误差 → 反向传播 → 更新参数"
for x, y in loader:
    opt.zero_grad()                                  # 清空上一步的梯度
    loss = nn.CrossEntropyLoss()(net(x), y)          # 预测与正确答案的差距
    loss.backward()                                  # 反向传播：算出每个参数该怎么调
    opt.step()                                       # 更新参数
    if loss.item() < 0.3:                            # 误差足够小 → 环境正常
        print("loss < 0.3，环境正常")
        break
