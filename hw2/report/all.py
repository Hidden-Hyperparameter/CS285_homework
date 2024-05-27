from parse_log import load
from plot1 import plot
import matplotlib.pyplot as plt
names = [
    'log_cartpole',
    'log_cartpole_rtg',
    'log_cartpole_na',
    'log_cartpole_rtg_na',
    # 'log_cartpole_lb',
    # 'log_cartpole_lb_rtg',
    # 'log_cartpole_lb_na',
    # 'log_cartpole_lb_rtg_na',
]
for name in names:
    load(name)
    plot(name)
    print(f'finish {name}')
plt.legend()
plt.savefig('./all_E1-1.png')