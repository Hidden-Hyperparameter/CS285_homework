from parse_log import load
from plot1 import plot
import matplotlib.pyplot as plt
# plt.figure(figsize=(10,5))


labels = {
    # 'log_task3_1':'original',
    # 'log_task3_my_1':'mine'
    # 'log_task3_2':'original',
    # 'log_task3_my_2':'mine',
    # 'log_task3_3':'original',
    # 'log_task3_my_3':'mine'

    # 'log_task3_3':'random shooting',
    # 'log_task5':'CEM with cem_iter 4',
    # 'log_task5_itr2':'CEM with cem_iter 2'

    # 'log_task5':'CEM original',
    # 'log_task5_my':'CEM with my method'

    'log_task6_r0_processed':'SAC baseline',
    'log_task6_r1_processed':'Dyna (rollout=1)',
    'log_task6_r10_processed':'MBPO(rollout=10)',
}

# E = 'Ensemble Size'
# labels = {
#     'log_task4_1': f'{E}=3',
#     'log_task4_2': f'{E}=2',
#     'log_task4_3': f'{E}=4',
# }

# E = 'Ensemble Size'
# labels = {
#     'log_task4_my_1': f'{E}=3',
#     'log_task4_my_2': f'{E}=2',
#     'log_task4_my_3': f'{E}=4',
# }

# E = 'MPC Action Num'
# labels = {
#     'log_task4_1': f'{E}=1000',
#     'log_task4_4': f'{E}=500',
#     'log_task4_5': f'{E}=2000',
# }

# E = 'MPC Horizon'
# labels = {
#     'log_task4_1': f'{E}=10',
#     'log_task4_6': f'{E}=5',
#     'log_task4_7': f'{E}=15',
# }

for name in labels:
    load(name)
    plot(name,label=labels[name])
    print(f'finish {name}')
plt.legend()
# plt.title(f'Different {E}')
plt.savefig('./P6.png')