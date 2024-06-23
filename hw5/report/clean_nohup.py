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
    for file1 in [
        # '4.1-dqn.log',
        # '4.1-cql.log',
        'exp_alpha0.log',
        'exp_alpha2.log',
        'exp_alpha4.log',
        'exp_alpha6.log',
        'exp_alpha8.log',
        'exp_alpha10.log',
        # 'log-4.2.log',
        # '4.3.log'
    ]:
        clean_nohup(file1)