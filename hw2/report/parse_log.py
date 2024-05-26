import re,json
def load(logname:str):
    s = open(f'{logname}.log').readlines()
    D = """
Eval_AverageReturn : 9.642857551574707
Eval_StdReturn : 0.7178482413291931
Eval_MaxReturn : 11.0
Eval_MinReturn : 8.0
Eval_AverageEpLen : 9.642857142857142
Train_AverageReturn : 37.0
Train_StdReturn : 0.0
Train_MaxReturn : 37.0
Train_MinReturn : 37.0
Train_AverageEpLen : 37.0
Actor Loss : 18.721797943115234
Train_EnvstepsSoFar : 37
TimeSinceStart : 0.03225994110107422
Initial_DataCollection_AverageReturn : 37.0
    """
    def convert(s:str):
        if s=='nan':
            return 0
        if s.find('.')!=-1:
            return float(s)
        return int(s)
    names = []
    for l in D.split('\n'):
        i = l.find(' : ')
        if i!=-1:
            name = l[:i]
            names.append(name)
    out = {n:[] for n in names}
    for l in s:
        for n in names:
            find_al = re.findall(f'^{n} \: (.+)$',l)
            if len(find_al)>0:
                out[n].append(convert(find_al[0]))
    json.dump(out,
    open(f'{logname}.json','w'),indent=4
    )
if __name__ == '__main__':
    load('log')