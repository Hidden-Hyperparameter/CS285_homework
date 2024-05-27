from parse_log import load
import matplotlib.pyplot as plt
import numpy as np
import json
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--name',type=str,default='default')
args = parser.parse_args()
N = f'log_pendulum_{args.name}'
names = [f'{N}_s{i}' for i in range(1,6)]
for name in names:
    load(name)
rewards = []
steps = []
for i in range(1,6):
    dic = json.load(open(f'{N}_s{i}.json'))
    rewards.append(dic['Eval_AverageReturn'])
    steps.append(dic['Train_EnvstepsSoFar'])
rewards = np.mean(np.stack(rewards,axis=-1),axis=-1)
steps = np.mean(np.stack(steps,axis=-1),axis=-1)
plt.plot(steps,rewards,label=N)
plt.legend()
plt.savefig(f'./E4_{N}.png')