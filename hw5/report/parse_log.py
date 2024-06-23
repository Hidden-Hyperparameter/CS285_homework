import re,json
def load(logname:str):
    s = open(f'{logname}.log').readlines()
    D = """
step : 90000
eval_return : 107.2
eval_ep_len : 107.2
eval return_std : 9.662298
eval return_max : 126.0
eval return_min : 97.0
eval ep_len_std : 9.66229786334493
eval ep_len_max : 126
eval ep_len_min : 97

Collecting data for eval...
Eval_AverageReturn : 127.65997314453125
Eval_StdReturn : 45.606258392333984
Eval_MaxReturn : 241.85488891601562
Eval_MinReturn : 87.27986145019531
Eval_AverageEpLen : 26.1875
Train_AverageReturn : 110.43861389160156
Train_StdReturn : 33.454750061035156
Train_MaxReturn : 302.39996337890625
Train_MinReturn : 71.44929504394531
Train_AverageEpLen : 22.667271078875793
Actor Loss : 1103.785888671875
Baseline Loss : 2116.1361987304685
Train_EnvstepsSoFar : 50004
TimeSinceStart : 51.42696762084961
Initial_DataCollection_AverageReturn : 110.43861389160156
Done logging...

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