# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
from flask_ngrok import run_with_ngrok
import tensorflow as tf
import os, pickle, re, sys
import pandas as pd


############################### TODO ##########################################
sys.path.append("/content/drive/MyDrive/codes")
from to_array.bert_to_array import BERTToArray
from models.bert_slot_model import BertSlotModel
from to_array.tokenizationK import FullTokenizer
###############################################################################
graph = tf.compat.v1.get_default_graph()
msg_k = ["type", "abv", "flavor", "taste"]
msg_v = ["맥주 종류", "맥주 도수", "맥주 향", "맥주 맛"]

# 슬롯
slots = {"type" : "맥주 종류", "abv" : "맥주 도수", "flavor" : "맥주 향", "taste" : "맥주 맛"}
beer_types = ['에일', 'IPA', '라거', '바이젠', '흑맥주']
beer_abv = ['3도', '4도', '5도', '6도', '7도', '8도',
            '3도이상', '4도이상', '5도이상', '6도이상', '7도이상',
            '3도 이상', '4도 이상', '5도 이상', '6도 이상', '7도 이상',
            '4도이하', '5도이하', '6도이하', '7도이하', '8도이하',
            '4도 이하', '5도 이하', '6도 이하', '7도 이하', '8도 이하']
beer_flavor = ['과일', '홉', '꽃', '상큼한', '커피', '스모키한']
beer_taste = ['단', '달달한', '달콤한', '안단', '안 단',
              '달지 않은', '달지않은', '쓴', '씁쓸한',
              '쌉쌀한', '달콤씁쓸한', '안쓴', '안 쓴', '쓰지 않은',
              '신', '상큼한', '새콤달콤한', '시지 않은', '시지않은',
              '쓰지않은/','안신', '안 신', '과일', '고소한', '구수한']

bert_model_hub_path = '/content/drive/MyDrive/codes/bert-module'
load_folder_path = '/content/drive/MyDrive/codes/save_model'
is_bert = True
############################### TODO ##########################################
# this line is to disable gpu
os.environ["CUDA_VISIBLE_DEVICES"]="-1"

config = tf.ConfigProto(intra_op_parallelism_threads=1,
                        inter_op_parallelism_threads=1,
                        allow_soft_placement=True,
                        device_count = {'CPU': 1})
sess = tf.compat.v1.Session(config=config)

bert_vocab_path = os.path.join(bert_model_hub_path, '/content/drive/MyDrive/vocab.korean.rawtext.list')
bert_to_array = BERTToArray(is_bert, bert_vocab_path)
vocab_file = os.path.join(bert_model_hub_path, "assets/vocab.korean.rawtext.list")

print('Loading Models...')
if not os.path.exists(load_folder_path):
  print(f'Folder {load_folder_path} not exist')

tags_to_array_path = os.path.join(load_folder_path, 'tags_to_array.pkl')

with open(tags_to_array_path, 'rb') as handle:
  tags_to_array = pickle.load(handle)
  slots_num = len(tags_to_array.label_encoder.classes_)
  
model = BertSlotModel.load(load_folder_path, sess)
tokenizer = FullTokenizer(vocab_file=vocab_file)
###############################################################################

app = Flask(__name__)
app.static_folder = 'static'

@app.route("/")
def home():

############################### TODO ##########################################
# 슬롯 사전 만들기
    # app.slot_dict = {'a_slot': None, 'b_slot':None}
    # beer_types, beer_abv, beer_flavor, beer_taste
    app.slot_dict = {'types' : beer_types, 'abv' : beer_abv, 'flavor' : beer_flavor, 'taste' : beer_taste}
    # app.slot_dict = {'beer_types' : None, 'beer_abv' : None, 'beer_flavor' : None, 'beer_taste' : None}
    
###############################################################################

    return render_template("index.html")
    
@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg').strip() # 사용자가 입력한 문장

############################### TODO ##########################################
# 1. 사용자가 입력한 한 문장을 슬롯태깅 모델에 넣어서 결과 뽑아내기
    text_arr = tokenizer.tokenize(userText)
    input_ids, input_mask, segment_ids = bert_to_array.transform([" ".join(text_arr)])
    
    with graph.as_default():
        with sess.as_default():
            inferred_tags, slots_score = model.predict_slots(
                [input_ids, input_mask, segment_ids], tags_to_array
            )

    # 결과 체크
    print("text_arr:", text_arr) 
    print("inferred_tags:", inferred_tags[0])
    print("slots_score:", slots_score[0])
    
# 2. 추출된 슬롯 정보를 가지고 더 필요한 정보 물어보는 규칙 만들기 (if문)
    # app.slot.dict['beer_types'] = inferred_tags[0]
    # if app.slot_dict['beer_types'] is None:
    #     message = '어떤 종류의 맥주를 원하세요?'
    #     return message                
    
    # 중복 제거
    inf_tags_unique = set(inferred_tags[0])
    inferred_tags[0] = list(inf_tags_unique)
    print("중복제거 inf :", inferred_tags[0])

    if len(inferred_tags[0]) == 1:
        if inferred_tags[0][0] == 'O':
            message = "{}, {}, {}, {} 중 하나를 입력해주세요".format(msg_v[0], msg_v[1], msg_v[2], msg_v[3])
            return message
        else:
            message = "{}".format(slots[inferred_tags[0][0]])
            return message 
     
    if len(inferred_tags[0]) == 2:
        if 'O' in inferred_tags[0]:
            inferred_tags[0].remove('O')
            message = "{}".format(slots[inferred_tags[0][0]]) 
            return message
        elif 'O' not in inferred_tags[0]:
            message = "{}, {}".format(slots[inferred_tags[0][0]], slots[inferred_tags[0][1]]) 
            return message
            
    if len(inferred_tags[0]) == 3:
        if 'O' in inferred_tags[0]:
            inferred_tags[0].remove('O')
            message = "{}, {}".format(slots[inferred_tags[0][0]], slots[inferred_tags[0][1]]) 
            return message
        elif 'O' not in inferred_tags[0]:
            message = "{}, {}, {}".format(slots[inferred_tags[0][0]], slots[inferred_tags[0][1]], slots[inferred_tags[0][2]]) 
            return message
    
    if len(inferred_tags[0]) == 4:
        if 'O' in inferred_tags[0]:
            inferred_tags[0].remove('O')
            message = "{}, {}, {}".format(slots[inferred_tags[0][0]], slots[inferred_tags[0][1]], slots[inferred_tags[0][2]])
            return message
        elif 'O' not in inferred_tags[0]:
            message = "{}, {}, {}, {}".format(slots[inferred_tags[0][0]], slots[inferred_tags[0][1]], slots[inferred_tags[0][2]], slots[inferred_tags[0][3]]) 
            return message
    
    if len(inferred_tags[0]) == 5:
        inferred_tags[0].remove('O')
        message = "{}, {}, {}, {}".format(slots[inferred_tags[0][0]], slots[inferred_tags[0][1]], slots[inferred_tags[0][2]], slots[inferred_tags[0][3]]) 
        return message

    print(app.slot_dict)

    return "bad"
###############################################################################



