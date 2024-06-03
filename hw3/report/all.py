from parse_log import load
from plot1 import plot
import matplotlib.pyplot as plt
# plt.figure(figsize=(10,5))
names = [
    'log',
]
for name in names:
    load(name)
    plot(name)
    print(f'finish {name}')
plt.legend()
plt.savefig('./P2-4-1.png')