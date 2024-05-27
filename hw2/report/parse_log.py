import re,json
def load(logname:str):
    s = open(f'{logname}.log').readlines()
    D = """
Eval_AverageReturn : -708.81103515625
Eval_StdReturn : 0.0
Eval_MaxReturn : -708.81103515625
Eval_MinReturn : -708.81103515625
Eval_AverageEpLen : 1000.0
Train_AverageReturn : -662.6456909179688
Train_StdReturn : 34.013126373291016
Train_MaxReturn : -625.0535888671875
Train_MinReturn : -721.0574340820312
Train_AverageEpLen : 1000.0
Actor Loss : -554552.375
Baseline Loss : 190.6030303955078
Train_EnvstepsSoFar : 5000
TimeSinceStart : 0.7141199111938477
Initial_DataCollection_AverageReturn : -662.6456909179688
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