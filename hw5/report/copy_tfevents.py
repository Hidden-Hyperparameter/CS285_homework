import os,re
from datetime import datetime
# name is like: q2_pg_cartpole_CartPole-v0_26-05-2024_21-47-16
#               q2_pg_cartpole_CartPole-v0_26-05-2024_21-47-27
def getMain(s:str):
    f = re.findall('^(.+)_([^_]+_[^_]+)$',s)
    if len(f)>0:
        return f[0]

def ToName(name:str,time:str):
    return name+'_'+datetime.strftime(time,'%d-%m-%Y_%H-%M-%S')

def list_task_time(root_dir:str):
    latest_dic = dict()
    for item in os.listdir(root_dir):
        name,date=getMain(item)
        formated = datetime.strptime(date,'%d-%m-%Y_%H-%M-%S')
        if name in latest_dic:
            if formated>latest_dic[name]:
                latest_dic[name]=formated
        else:
            latest_dic[name]=formated
    return latest_dic

if __name__ == '__main__':
    print('!name is main!')
    dic1 = list_task_time('./data')
    dic2 = list_task_time('./run_logs')

    for k,v in dic1.items():
        file=ToName(k,v)
        if not k in dic2:
            os.system(f'cp -r ./data/{file} ./run_logs/{file}')
        else:
            if v > dic2[k]:
                oldfolder = os.path.join('./run_logs',ToName(k,dic2[k]))
                # print(f'try to replace {oldfolder} with {file}')
                os.system(f'rm -rf {oldfolder}')
                os.system(f'cp -r ./data/{file} ./run_logs/{file}')
else:
    print('safe, name is ',__name__)