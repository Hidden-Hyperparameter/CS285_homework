import re
ls = open('log.log').readlines()
names = [
    # 'Train_AverageReturn',
    # 'Train_StdReturn',
    'Eval_AverageReturn',
    'Eval_StdReturn',
    'Expert',
]
dic = dict()
for l in ls:
    for name in names:
        f = re.findall(f'{name} : ([\d]+\.[\d]+)',l)
        if len(f)>0:
            if name in dic:
                dic[name].append(f[0])
            else:
                dic[name]=[f[0]]
for key in dic:
    dic[key]=[float(c) for c in dic[key]]
print(dic)
            
    
