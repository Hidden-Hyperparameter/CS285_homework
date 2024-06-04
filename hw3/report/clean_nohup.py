def clean_nohup(filename:str):
    ls = open(filename).readlines()
    outs = []
    for l in ls:
        l = l.strip(' \n')
        a = l.find('it/s]')
        b = l.find('s/it]')
        if a != -1:
            l_processed = l[a+5:]
        elif b != -1:
            l_processed = l[b+5:]
        else:
            l_processed = l
        if l_processed.strip(' \n') != '':
            outs.append(l_processed+'\n')
    open(filename.replace('.log','_processed.log'),'w').writelines(outs)

if __name__ == '__main__':
    clean_nohup('report/test.log')