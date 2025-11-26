import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import UnivariateSpline

# 数据
x = np.array([3.9, 12.8, 23.4, 36.2, 53.1, 73.7])
y = np.array([0, 20, 40, 60, 80, 100])

# 拟合平滑曲线
spline = UnivariateSpline(x, y, k=3, s=0)

# 选择画切线的点（这里选加速度 = 36.2）
xt = 36.2
yt = spline(xt)

# 计算导数（斜率）
slope = spline.derivative()(xt)

# 生成切线
x_tan = np.linspace(min(x), max(x), 200)
y_tan = yt + slope * (x_tan - xt)

# 绘图
plt.figure(figsize=(7,5))
plt.plot(x, y, 'o', label="数据点")
plt.plot(x_tan, spline(x_tan), label="平滑曲线")
plt.plot(x_tan, y_tan, '--', label="切线")
plt.scatter([xt], [yt], color='red', label="切点")
plt.xlabel("加速度")
plt.ylabel("力 (N)")
plt.title("加速度-力 图像及切线")
plt.grid(True)
plt.legend()
plt.show()