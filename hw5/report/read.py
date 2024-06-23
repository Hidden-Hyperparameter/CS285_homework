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
    file_path = '/root/CS285_homework/hw5/cs285/scripts/../../data/hw5_finetune_PointmassHard-v0_cql0.1_23-06-2024_21-29-30'.strip()
    file_name = os.listdir(file_path)
    file_path = os.path.abspath(os.path.join(file_path,file_name[0]))
    print(file_path)
    assert os.path.exists(file_path)

    records = read_tfevents_file(file_path)
    json.dump(records,open('text.json','w'),indent=4)