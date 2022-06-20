# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
import tensorflow as tf
import os, sys
import pickle
import re

############################### TODO ##########################################
sys.path.append("/content/drive/MyDrive/codes")
# from to_array.bert_to_array import BERTToArray
# from models.bert_slot_model import BertSlotModel
from to_array.bert_to_array import *
from models.bert_slot_model import BertSlotModel
from to_array.tokenizationK import FullTokenizer
###############################################################################
graph = tf.compat.v1.get_default_graph()

bert_model_hub_path = '/content/drive/MyDrive/codes/bert-module' # TODO 경로 고치기
load_folder_path = '/content/drive/MyDrive/codes/save_model'
is_bert = True

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
# made_slot
made_slot = {'beer_types':'맥주 종류',
        'beer_abv':'맥주 도수',
        'beer_flavor':'맥주 향',
        'beer_taste':'맥주 맛'}

dic = {i:globals()[i] for i in made_slot}

cmds = {'명령어':[],
        '맥주 종류':beer_types,
        '맥주 도수':beer_abv,
        '맥주 향':beer_flavor,
        '맥주 맛':beer_taste}

cmds["명령어"] = [k for k in cmds]

############################### TODO ##########################################
# 슬롯태깅 모델과 벡터라이저 불러오기
os.environ["CUDA_VISIBLE_DEVICES"] = "0"
config = tf.compat.v1.ConfigProto(intra_op_parallelism_threads=1, inter_op_parallelism_threads=1, allow_soft_placement=True, device_count={"GPU": 0})
    
sess = tf.compat.v1.Session(config=config)

vocab_file = os.path.join(bert_model_hub_path, "assets/vocab.korean.rawtext.list")
bert_to_array = BERTToArray(vocab_file)

tags_to_array_path = os.path.join(load_folder_path, "tags_to_array.pkl")
with open(tags_to_array_path, "rb") as handle:
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
    app.slot_dict = {'beer_types': [],
     'beer_abv': [],
     'beer_flavor': [],
     'beer_taste': []}
###############################################################################
    
    # 이거 뭐지?
    app.score_limit = 0.7

    return render_template("index.html")

    
@app.route("/get")
def get_bot_response():
############################### TODO ##########################################
# 1. 사용자가 입력한 한 문장을 슬롯태깅 모델에 넣어서 결과 뽑아내기
    userText = request.args.get('msg').strip() # 사용자가 입력한 문장

    if userText[0] == "!":
        # if userText[1:] in members:
        #     message = f"""
        #         <br />
        #         {member_introduction[userText[1:]]}
        #         <br /><br />
        #         """                   
        if userText[1:] in cmds["명령어"]: 
            li = cmds[userText[1:]]
            message = "<br />\n".join(li)
        elif userText.strip().startswith("예"):
            message = '추천이 완료되었습니다.'
        elif userText.strip().startswith("아니오"):
            message = '추천이 취소되었습니다.'
        else:
            message = "입력한 명령어가 존재하지 않습니다."

        return message


    text_arr = tokenizer.tokenize(userText)
    input_ids, input_mask, segment_ids = bert_to_array.transform([" ".join(text_arr)])

    # 예측
    with graph.as_default():
        with sess.as_default():
            inferred_tags, slots_score = model.predict_slots(
                [input_ids, input_mask, segment_ids], tags_to_array
            )

    # 결과 체크
    print("text_arr:", text_arr)
    print("inferred_tags:", inferred_tags[0])
    print("slots_score:", slots_score[0])

    # 슬롯에 해당하는 텍스트를 담을 변수 설정
    slot_text = {k: "" for k in app.slot_dict}

    # 슬롯태깅 실시
    for i in range(0, len(inferred_tags[0])):
        if slots_score[0][i] >= app.score_limit:
            catch_slot(i, inferred_tags, text_arr, slot_text)
        else:
            print("something went wrong!")

    # 메뉴판의 이름과 일치하는지 검증
    for k in app.slot_dict:
        for x in dic[k]:
            x = x.lower().replace(" ", "\s*")
            m = re.search(x, slot_text[k])
            if m:
                app.slot_dict[k].append(m.group())

    print(app.slot_dict)
    
    empty_slot = [made_slot[k] for k in app.slot_dict if not app.slot_dict[k]]
    filled_slot = [made_slot[k] for k in app.slot_dict if app.slot_dict[k]]
    
    print("empty_slot :", empty_slot)
    print("filled_slot :", filled_slot)
    
# 2. 추출된 슬롯 정보를 가지고 더 필요한 정보 물어보는 규칙 만들기 (if문)
    # app.slot_dict['a_slot'] = ''
# ex)
    if app.slot_dict['beer_types']:
        message = '추천완료'
            
    elif app.slot_dict['beer_types'] is None:
        message = '어떤 종류의 맥주를 원하세요?'
    
    elif app.slot_dict['beer_abv'] is None:
        message = '어느 도수의 맥주를 원하세요?'
    
    elif app.slot_dict['beer_flavor'] is None:
        message = '어떤 향이 나는 맥주를 원하세요?'
    
    elif app.slot_dict['beer_taste'] is None:
        message = '어떤 맛의 맥주를 원하세요?'

    # print(app.slot_dict)

    # return 'hi' # 챗봇이 이용자에게 하는 말을 return
    return message
###############################################################################

### copy ##
def check_order_msg(app, made_slot):
    order = []
    for k, v in app.slot_dict.items():
        try:
            if len(v) == 1:
                order.append(f"{made_slot[k]}: {v[0]}")
            else:
                order.append(f"{made_slot[k]}: {', '.join(v)}")
        except:
            order.append(f"{made_slot[k]}: {None}")
    order = "<br />\n".join(set(order))

    message = f"""
        주문 확인하겠습니다.<br />
        ===================<br />
        {order}
        <br />===================<br />
        이대로 주문 완료하시겠습니까? (예 or 아니오)
        """

    return message

def init_app(app):
    app.slot_dict = {
        'beer_types': [],
        'beer_abv': [],
        'beer_flavor': [],
        'beer_taste': [],
        }

def catch_slot(i, inferred_tags, text_arr, slot_text):
    if not inferred_tags[0][i] == "O":
        word_piece = re.sub("_", " ", text_arr[i])
        if word_piece == 'ᆫ':
            word = slot_text[inferred_tags[0][i]]
            slot_text[inferred_tags[0][i]] = word[:-1]+chr(ord(word[-1])+4)
        else:    
            slot_text[inferred_tags[0][i]] += word_piece


