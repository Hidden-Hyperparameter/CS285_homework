import numpy as np
import matplotlib.pyplot as plt
import json
def plot(logname:str):
    dic = json.load(open(f'{logname}.json'))
    ret = np.array(dic['eval_return'])
    # ret_var = np.array(dic['Eval_StdReturn'])
    x = np.array(dic['step'])
    # plt.errorbar(x, ret, yerr=ret_var) 
    plt.plot(x,ret,label=logname)
    plt.xlabel('step')
    plt.ylabel('eval_return')
    # plt.title('Evaluation Average Return with Error Bars')
    # plt.savefig(f'{logname}.png')
    # plt.close()