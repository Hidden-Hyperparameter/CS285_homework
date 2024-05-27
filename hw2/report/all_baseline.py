from parse_log import load
from plot_baseline_loss import plot_baseline
import matplotlib.pyplot as plt
names = [
    'log_cheetah_baseline',
    'log_cheetah_baseline_lowlr',
    'log_cheetah_baseline_lowgs'
]
for name in names:
    load(name)
    plot_baseline(name)
    print(f'finish {name}')
plt.legend()
plt.savefig('./all_E2_baseline_hyperparam.png')