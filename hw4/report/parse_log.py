import re,json
def load(logname:str):
    s = open(f'{logname}.log').readlines()

    def convert(s:str):
        if s=='nan':
            return 0
        if s.find('.')!=-1:
            return float(s)
        return int(s)
    names = ['Average eval return']

    out = {n:[] for n in names}
    for l in s:
        for n in names:
            find_al = re.findall(f'^{n}\: (.+)$',l)
            if len(find_al)>0:
                out[n].append(convert(find_al[0]))
    json.dump(out,
    open(f'{logname}.json','w'),indent=4
    )
if __name__ == '__main__':
    load('log')