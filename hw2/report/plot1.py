import numpy as np
import matplotlib.pyplot as plt
import json
def plot(logname:str):
    dic = json.load(open(f'{logname}.json'))
    ret = np.array(dic['Eval_AverageReturn'])
    ret_var = np.array(dic['Eval_StdReturn'])
    x = np.array(dic['Train_EnvstepsSoFar'])
    # plt.errorbar(x, ret, yerr=ret_var) 
    plt.plot(x,ret,label=logname)
    plt.xlabel('Train_EnvstepsSoFar')
    plt.ylabel('Eval_AverageReturn')
    # plt.title('Evaluation Average Return with Error Bars')
    # plt.savefig(f'{logname}.png')
    # plt.close()