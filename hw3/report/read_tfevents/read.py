from tensorflow.core.util import event_pb2
from tensorflow.python.lib.io import tf_record
import os,json

def remove_all_bytes(s):
    if isinstance(s,list):
        for i,item in enumerate(s):
            s[i]=remove_all_bytes(item)
        return s
    elif isinstance(s,dict):
        new_dic = dict()
        for k,v in s.items():
            new_dic[remove_all_bytes(k)]=remove_all_bytes(v)
        return new_dic
    else:
        if isinstance(s,(str,float,int)):
            return s
        if isinstance(s,bytes):
            return  s.hex()
        return None

def decode_file(file_path):
    records = []
    for record in tf_record.tf_record_iterator(file_path):
        event = event_pb2.Event.FromString(record)
        record_dict = {}
        for field in event.DESCRIPTOR.fields:
            value = getattr(event, field.name)
            if field.name == 'summary':
                value = {v.tag: v.simple_value for v in value.value}
            if not field.name in ['wall_time','file_version','graph_def','log_message','session_log','tagged_run_metadata','meta_graph_def']:
                record_dict[field.name] = value
        records.append(record_dict)
    return remove_all_bytes(records)

def read_tfevents_file(file_path):
    l = decode_file(file_path)
    final = dict()
    for dic in l:
        step = dic['step']
        if not step in final:
            final[step]=dic['summary']
        else:
            final[step].update(dic['summary'])
    ret = []
    for k,v in final.items():
        d = {'step':k}
        d.update(v)
        ret.append(d.copy())
    return ret

if __name__ == '__main__':
    file_path = 'data/hw3_dqn_dqn_CartPole-v1_s64_l2_d0.99_03-06-2024_09-26-58/events.out.tfevents.1717378018.zhh-82TK'
    file_path = os.path.abspath(file_path)
    print(file_path)
    assert os.path.exists(file_path)

    records = read_tfevents_file(file_path)
    json.dump(records,open('text.json','w'),indent=4)