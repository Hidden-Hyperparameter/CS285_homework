from parse_log import load
load('last_time_humanoid')
load('log11_processed')
load('log9_processed')
import numpy as np
import matplotlib.pyplot as plt
import json

dic1 = json.load(open('last_time_humanoid.json'))
ret1 = np.array(dic1['Eval_AverageReturn'])
x1 = np.array(dic1['Train_EnvstepsSoFar'])
plt.plot(x1,ret1,label='Policy Gradients')

dic2 = json.load(open('log11_processed.json'))
ret2 = np.array(dic2['eval_return'])
x2 = np.array(dic2['step'])
plt.plot(x2,ret2,label='Double Q-Learning')

dic3 = json.load(open('log9_processed.json'))
ret3 = np.array(dic3['eval_return'])
x3 = np.array(dic3['step'])
plt.plot(x3,ret3,label='Clip Q-Learning')

plt.xlabel('Env steps')
plt.ylabel('Eval Average Return')
plt.xlim(0,1000000)
plt.ylim(0,750)
plt.legend()
    # plt.title('Evaluation Average Return with Error Bars')
plt.savefig('3-1-5-3.png')
    # plt.close()