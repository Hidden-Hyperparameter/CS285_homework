from parse_log import load
from plot1 import plot
import matplotlib.pyplot as plt
# plt.figure(figsize=(10,5))
names = [
    # 'log_cartpole',
    # 'log_cartpole_rtg',
    # 'log_cartpole_na',
    # 'log_cartpole_rtg_na',
    # 'log_cartpole_lb',
    # 'log_cartpole_lb_rtg',
    # 'log_cartpole_lb_na',
    # 'log_cartpole_lb_rtg_na',

    # 'log_cheetah',
    # 'log_cheetah_baseline',
    # 'log_cheetah_baseline_lowlr',
    # 'log_cheetah_baseline_lowgs'

    'log_lunar_lander_lambda_0',
    # 'log_lunar_lander_lambda_0.95',
    # 'log_lunar_lander_lambda_0.98',
    # 'log_lunar_lander_lambda_0.99',
    'log_lunar_lander_lambda_1',
]
for name in names:
    load(name)
    plot(name)
    print(f'finish {name}')
plt.legend()
plt.savefig('./E3_0.98.png')