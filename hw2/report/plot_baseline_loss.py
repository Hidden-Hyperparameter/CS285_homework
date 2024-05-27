import numpy as np
import matplotlib.pyplot as plt
import json
def plot_baseline(logname:str):
    dic = json.load(open(f'{logname}.json'))
    ret = np.array(dic['Baseline Loss'])
    x = np.array(dic['Train_EnvstepsSoFar'])
    # plt.errorbar(x, ret, yerr=ret_var) 
    plt.plot(x,ret,label=logname)
    plt.xlabel('Train_EnvstepsSoFar')
    plt.ylabel('Baseline Loss')
    # plt.title('Evaluation Average Return with Error Bars')
# plt.savefig(f'{logname}_baseline_loss.png')
# plt.close()