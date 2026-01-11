import numpy as np
import matplotlib.pyplot as plt

# 参数
g = 9.81   # 重力加速度
L = 1.0    # 摆长
m = 1.0    # 质量
c = 0.15   # 阻力系数 (与角速度成正比)

# 数值积分配置
dt = 0.01
t_end = 20.0
steps = int(t_end / dt)

# 初始条件: theta(0), theta_dot(0)
theta = 1.0
theta_dot = 0.0

traj = np.zeros((steps, 2))

def step(theta, theta_dot, dt):
    # 一步积分（显式 Euler）
    theta_ddot = -(c / m) * theta_dot - (g / L) * np.sin(theta)
    theta_dot_next = theta_dot + theta_ddot * dt
    theta_next = theta + theta_dot_next * dt
    return theta_next, theta_dot_next

for i in range(steps):
    traj[i, 0] = theta
    traj[i, 1] = theta_dot
    theta, theta_dot = step(theta, theta_dot, dt)

# 在 (theta, theta_dot) 平面上画轨迹
plt.figure(figsize=(6, 6))
plt.plot(traj[:, 0], traj[:, 1], lw=1.5)
plt.xlabel("theta (rad)")
plt.ylabel("theta_dot (rad/s)")
plt.title("Damped Pendulum Phase Portrait")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
