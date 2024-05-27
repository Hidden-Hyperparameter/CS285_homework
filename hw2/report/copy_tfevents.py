import os,re
from datetime import datetime
l=(os.listdir('./data'))
# name is like: q2_pg_cartpole_CartPole-v0_26-05-2024_21-47-16
#               q2_pg_cartpole_CartPole-v0_26-05-2024_21-47-27
def getMain(s:str):
    f = re.findall('^(.+)_([^_]+_[^_]+)$',s)
    if len(f)>0:
        return f[0]
latest_dic = dict()
for item in l:
    name,date=getMain(item)
    formated = datetime.strptime(date,'%d-%m-%Y_%H-%M-%S')
    if name in latest_dic:
        if formated>latest_dic[name]:
            latest_dic[name]=formated
    else:
        latest_dic[name]=formated
for k,v in latest_dic.items():
    file=k+'_'+datetime.strftime(v,'%d-%m-%Y_%H-%M-%S')
    os.system(f'cp -r ./data/{file} ./run_logs/{file}')