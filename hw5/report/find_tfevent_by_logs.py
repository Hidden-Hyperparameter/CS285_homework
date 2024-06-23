import os
from copy_tfevents import getMain,list_task_time,ToName
from datetime import datetime

def get_tfevents_file_folder(log_file_dir:str):
    print('-'*20)
    s = open(log_file_dir).readlines()
    special = 'logging outputs to  '
    tf_dir = [c.removeprefix(special).strip(' \n') for c in s if c.startswith(special)][0]
    tf_dir = os.path.abspath(tf_dir)
    # print(log_path,os.path.exists(log_path))
    if not os.path.exists(tf_dir):
        print(f'hint: path <{tf_dir}> is on another device...')
        return None
    return tf_dir

if __name__ == '__main__':
    log_dir = './report/logs/'
    log_files = os.listdir(log_dir)
    have_tasks = list_task_time('./run_logs')

    for log_file in log_files:
        print('-'*20)
        tf_dir = get_tfevents_file_folder(os.path.join(log_dir,log_file))
        if tf_dir is None:
            print(f'file {log_file} aborted')
            continue
        bname = os.path.basename(tf_dir)
        main,time = getMain(bname)
        time = datetime.strptime(time,'%d-%m-%Y_%H-%M-%S')
        if (main in have_tasks):
            print(f'file {log_file} is already there.')
            print(f'the file name is        : {bname}')
            print(f'the file in the folder is {ToName(main,have_tasks[main])}')
            overwrite = input('Overwrite? (Hint: If you run two different tasks with the same name, do not overwrite!)[y/n]:')
            if overwrite=='y':
                os.system(f'rm -rf ./run_logs/{ToName(main,have_tasks[main])}')
        os.system(f'cp -r {tf_dir} run_logs/')
        print(f'file {log_file} is successful.')