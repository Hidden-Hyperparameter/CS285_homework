from read import read_tfevents_file
from find_tfevent_by_logs import get_tfevents_file_folder
import matplotlib.pyplot as plt
import os
import numpy as np

def smooth(x:np.ndarray):
    window_size = 10
    window = np.ones(window_size)/window_size
    return np.convolve(x, window, mode='same')

if __name__ != '__main__':
    print('do not import!')
    exit(114514)

# CONFIGS

labels = {
    # Task 2.5
    # 'vanilla':[
    #     'log2-seed1',
    #     'log2-seed2',
    #     'log2-seed3'
    # ],
    # 'double q':[
    #     'log4_seed1',
    #     'log4_seed2',
    #     'log4_seed3'
    # ]

    # Task 2.4.3
    # 'original lr=1e-3':['log'],
    # 'lr=0.05':['log3']

    # Task 2.6
    # 'lr=1.0e-3':['log4_seed1','log4_seed2','log4_seed3'],
    # 'lr=3.0e-4':['log5_param1'],
    # 'lr=9.0e-4':['log5_param2'],
    # 'lr=0.4e-4':['log5_param3']

    # Task 3.1.3.1
    # 'my':['log6'],
    # 'bird':['bird']

    # Task 3.1.4.1
    # '':['log8_processed']

    # Task 3.1.4.2 # Unfinished

    'reinforce 1':['log7'],
    'reinforce 10':['log7-2'],
    'reparameterize':['log9.5']

    # Task 3.1.5
    # 'singleq':['log10-1'],
    # 'clipq':['log10-2'],
    # 'doubleq':['log10-3'],
    # 'redq':['log10-4']

    # Task 3.1.3

    # Task 3.1.4


}

x_axis = 'step'
y_axises = ['eval_return']
y_label = 'return'
plot_title = None
plot_name = 'P3-1-4-2.png'
do_smooth = False

# CONFIG END

# KEYS
"step"
"critic_loss"
"q_values"
"target_values"
"grad_norm"
"epsilon"
"lr"

"train_return"
"train_ep_len"
"eval_return"
"eval_ep_len"

"eval/return_std"
"eval/return_max"
"eval/return_min"
"eval/ep_len_std"
"eval/ep_len_max"
"eval/ep_len_min"
# KEYS END

def parse_tf_json(tf_path:str):
    x_values = [[].copy() for _ in range(len(y_axises))]
    y_values = [[].copy() for _ in range(len(y_axises))]
    l = read_tfevents_file(tf_path)
    for dic in l:
        for i,y_axis in enumerate(y_axises):
            if x_axis in dic and y_axis in dic:
                x_values[i].append(dic[x_axis])
                y_values[i].append(dic[y_axis])
    return [np.array(x_values[i]) for i in range(len(y_axises))],\
        [np.array(y_values[i]) for i in range(len(y_axises))]

for label,files in labels.items():
    x_s = [[].copy() for _ in range(len(y_axises))]
    y_s = [[].copy() for _ in range(len(y_axises))]
    for file in files:
        print('finish file',file)
        tf_folder = get_tfevents_file_folder(file+'.log')
        tf_file_path = os.listdir(tf_folder)[0]
        tf_file_path = os.path.join(tf_folder,tf_file_path)
        x,y = parse_tf_json(tf_file_path)
        for i,y_axis in enumerate(y_axises):
            print(f'{i}(for {y_axis}) append x: {x[i].shape}')
            x_s[i].append(x[i]);y_s[i].append(y[i])
    for i,y_axis in enumerate(y_axises):
        m_len1 = min([len(c) for c in x_s[i]])
        m_len2 = min([len(c) for c in y_s[i]])
        m_len = min(m_len1,m_len2)
        x_s[i] = np.stack([c[:m_len] for c in x_s[i]],axis=0).mean(axis=0)
        y_s[i] = np.stack([c[:m_len] for c in y_s[i]],axis=0).mean(axis=0)
        print(f'ploting label <{label} {y_axis}>...')
        if 'train' in y_axis or do_smooth:
            plt.plot(x_s[i],smooth(y_s[i]),label=label+' '+y_axis)
        else:
            plt.plot(x_s[i],y_s[i],label=label+' '+y_axis)

plt.xlabel(x_axis)
plt.ylabel(y_label)
plt.legend()
plt.title(plot_title)

if os.path.exists(plot_name):
    do=input('image file exists. overwrite?[y/n]')
    if do!='y':
        exit()
plt.savefig(plot_name)

