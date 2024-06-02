import os
from copy_tfevents import getMain,list_task_time,ToName
from datetime import datetime
log_dir = './report/logs/'
log_files = os.listdir(log_dir)
have_tasks = list_task_time('./run_logs')

for log_file in log_files:
    print('-'*20)
    s = open(os.path.join(log_dir,log_file)).readlines()
    special = 'logging outputs to  '
    log_path = [c.removeprefix(special).strip(' \n') for c in s if c.startswith(special)][0]
    log_path = os.path.abspath(log_path)
    # print(log_path,os.path.exists(log_path))
    if not os.path.exists(log_path):
        print(f'file {log_file} aborted since path <{log_path}> is on another device...')
        continue
    bname = os.path.basename(log_path)
    main,time = getMain(bname)
    time = datetime.strptime(time,'%d-%m-%Y_%H-%M-%S')
    if (main in have_tasks):
        print(f'file {log_file} is already there.')
        print(f'the file name is        : {bname}')
        print(f'the file in the folder is {ToName(main,have_tasks[main])}')
        overwrite = input('Overwrite? (Hint: If you run two different tasks with the same name, do not overwrite!)[y/n]:')
        if overwrite=='y':
            os.system(f'rm -rf ./run_logs/{ToName(main,have_tasks[main])}')
    os.system(f'cp -r {log_path} run_logs/')
    print(f'file {log_file} is successful.')