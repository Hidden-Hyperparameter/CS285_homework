import numpy as np
import matplotlib.pyplot as plt
import json
dic = json.load(open('log.json'))
ret = np.array(dic['Eval_AverageReturn'])
ret_var = np.array(dic['Eval_StdReturn'])
x = np.array(dic['Train_EnvstepsSoFar'])
# plt.errorbar(x, ret, yerr=ret_var) 
plt.plot(x,ret)
plt.xlabel('Train_EnvstepsSoFar')
plt.ylabel('Eval_AverageReturn')
# plt.title('Evaluation Average Return with Error Bars')
plt.show()
