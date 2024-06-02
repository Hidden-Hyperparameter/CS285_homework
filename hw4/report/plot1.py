import numpy as np
import matplotlib.pyplot as plt
import json
def plot(logname:str,label:str=None):
    dic = json.load(open(f'{logname}.json'))
    ret = np.array(dic['Average eval return'])
    x = np.arange(0,len(ret))
    # plt.errorbar(x, ret, yerr=ret_var) 
    plt.plot(x,ret,label=logname if label is None else label)
    plt.xlabel('Iteration')
    plt.ylabel('Eval Average Return')
    # plt.title('Evaluation Average Return with Error Bars')
    # plt.savefig(f'{logname}.png')
    # plt.close()