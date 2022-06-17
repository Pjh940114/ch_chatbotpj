# -*- coding: utf-8 -*-

# from to_array.bert_to_array import BERTToArray
from to_array.bert_to_array import *
from models.bert_slot_model import BertSlotModel

import argparse
import os
import pickle
import tensorflow as tf


# read command-line parameters
parser = argparse.ArgumentParser('Evaluating the BERT / ALBERT NLU model')
parser.add_argument('--model', '-m', help = 'Path to BERT / ALBERT NLU model', type = str, required = True)
parser.add_argument('--type', '-tp', help = 'bert or albert', type = str, default = 'bert', required = False)


VALID_TYPES = ['bert', 'albert']

args = parser.parse_args()
load_folder_path = args.model
type_ = args.type

# this line is to disable gpu
os.environ["CUDA_VISIBLE_DEVICES"]="-1"

config = tf.ConfigProto(intra_op_parallelism_threads=1,
                        inter_op_parallelism_threads=1,
                        allow_soft_placement=True,
                        device_count = {'CPU': 1})
sess = tf.compat.v1.Session(config=config)

if type_ == 'bert':
    bert_model_hub_path = '/content/drive/MyDrive/codes/bert-module'
    is_bert = True
elif type_ == 'albert':
    bert_model_hub_path = 'https://tfhub.dev/google/albert_base/1'
    is_bert = False
else:
    raise ValueError('type must be one of these values: %s' % str(VALID_TYPES))

bert_vocab_path = os.path.join(bert_model_hub_path, '/content/drive/MyDrive/vocab.korean.rawtext.list')
bert_to_array = BERTToArray(is_bert, bert_vocab_path)

print('Loading Models...')
if not os.path.exists(load_folder_path):
  print(f'Folder {load_folder_path} not exist')

tags_to_array_path = os.path.join(load_folder_path, 'tags_to_array.pkl')

with open(tags_to_array_path, 'rb') as handle:
  tags_to_array = pickle.load(handle)
  slots_num = len(tags_to_array.label_encoder.classes_)
  
model = BertSlotModel.load(load_folder_path, sess)

while True:
    print('\nEnter your sentence: ')
    try:
        input_text = input().strip()
    except:
        continue
        
    if input_text == 'quit':
        break

    else :
        text_arr = bert_to_array.tokenizer.tokenize(input_text)

        input_ids, input_mask, segment_ids = bert_to_array.transform([' '.join(text_arr)])

        inferred_tags, slot_score = model.predict_slots([input_ids, input_mask, segment_ids], tags_to_array)

        print(text_arr)
        print(inferred_tags[0])
        print(slot_score[0])

tf.compat.v1.reset_default_graph()

