import tensorflow as tf
from tensorflow.core.util import event_pb2
from tensorflow.python.lib.io import tf_record

def read_tfevents_file(file_path):
    records = []
    for record in tf_record.tf_record_iterator(file_path):
        event = event_pb2.Event.FromString(record)
        record_dict = {}
        for field in event.DESCRIPTOR.fields:
            value = getattr(event, field.name)
            if field.name == 'summary':
                value = {v.tag: v.simple_value for v in value.value}
            record_dict[field.name] = value
        records.append(record_dict)
    return records

file_path = 'events.out.tfevents.1717373696.zhh-82TK'
records = read_tfevents_file(file_path)