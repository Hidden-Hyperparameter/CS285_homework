from parse_log import load
import matplotlib.pyplot as plt
import numpy as np
import json
names = {
    'log_pendulum_default':'default',
    'log_pendulum_discount0.99_smallbatch_gae0.98':'my'
}
for name in names:
    rewards = []
    steps = []
    for i in range(1,6):
        dic = json.load(open(f'{name}_s{i}.json'))
        rewards.append(dic['Eval_AverageReturn'])
        steps.append(dic['Train_EnvstepsSoFar'])
    rewards = np.mean(np.stack(rewards,axis=-1),axis=-1)
    steps = np.mean(np.stack(steps,axis=-1),axis=-1)
    plt.plot(steps,rewards,label=name)
plt.legend()
plt.savefig(f'./E4_all.png')