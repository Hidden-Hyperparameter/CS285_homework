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