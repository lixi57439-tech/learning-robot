# -*- coding: utf-8 -*-
# check_env.py —— 阶段 0 环境自检：把本阶段装的东西全部验一遍
import sys        # 内置模块：拿 Python 自己的信息（如版本）
import shutil     # 内置模块：查找某个命令装在哪

def line(name, ok, detail=""):
    """打印一行检查结果：ok 为真显示 OK，否则显示 NG"""
    print(f"[{'OK' if ok else 'NG'}] {name:<8} {detail}")
    return ok               # 返回结果，方便最后统一判断

results = []                # 用一个列表收集所有检查结果

# ① Python 版本够不够（要求 >= 3.9）
results.append(line("Python", sys.version_info >= (3, 9), sys.version.split()[0]))

# ② numpy 能不能导入（注意：import 要写在 try 里面，否则缺包时程序会直接崩）
try:
    import numpy
    # 【修复这里】：把 False 改成 True，并且加上版本号
    results.append(line("numpy", True, numpy.__version__))
except ImportError:                       # 导入失败就走到这里
    results.append(line("numpy", False, "缺失，执行: pip install numpy"))

# ③ PyTorch 能不能导入，以及显卡能不能用
try:
    import torch
    results.append(line("PyTorch", True, torch.__version__))
    gpu = torch.cuda.is_available()
    results.append(line("CUDA", gpu, "GPU 可用" if gpu else "不可用（见教程 7.1）"))
except ImportError:
    results.append(line("PyTorch", False, "缺失，按教程 7.2 安装"))

# ④ 三个命令行工具是否在 PATH 里（用 Day1 学的 which 的 Python 版）
for cmd in ("git", "docker", "conda"):
    path = shutil.which(cmd)
    results.append(line(cmd, path is not None, path or "未安装"))

# ⑤ 汇总
print("-" * 50)
failed = results.count(False)
if failed == 0:
    print("全部通过，阶段 0 验收达标！")
    sys.exit(0)             # 退出码 0 = 成功（命令行惯例）
print(f"有 {failed} 项未通过，对照教程第 8 节排错表处理。")
sys.exit(1)                 # 非 0 = 失败
