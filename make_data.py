import random
import re

# 슬롯 : 종류, 도수, 맛, 향 
beer_types = ['/type;에일/', '/type;IPA/', '/type;라거/', '/type;바이젠/', '/type;흑맥주/']

# for word in beer_types: # 한글만
#     code = ord(word[-2])
#     if 44032 <= code <= 55203 and (code - ord("가")) % 28 > 0:
#         print(word)

beer_abv = ['/abv;3도/', '/abv;4도/', '/abv;5도/', '/abv;6도/', '/abv;7도/', '/abv;8도/',
            '/abv;3도이상/', '/abv;4도이상/', '/abv;5도이상/', '/abv;6도이상/', '/abv;7도이상/',
           '/abv;3도 이상/', '/abv;4도 이상/', '/abv;5도 이상/', '/abv;6도 이상/', '/abv;7도 이상/',
           '/abv;4도이하/', '/abv;5도이하/', '/abv;6도이하/', '/abv;7도이하/', '/abv;8도이하/',
            '/abv;4도 이하/', '/abv;5도 이하/', '/abv;6도 이하/', '/abv;7도 이하/', '/abv;8도 이하/']

# for word in beer_abv:
#     if (ord(word[-2]) - ord("가")) % 28 > 0:
#         print(word)

beer_flavor = ['/flavor;과일/', '/flavor;홉/', '/flavor;꽃/', '/flavor;상큼한/', '/flavor;커피/', '/flavor;스모키한/']
        
beer_taste = [
        '/taste;단/', '/taste;달달한/', '/taste;달콤한/',
        '/taste;안단/', '/taste;안 단/', '/taste;달지 않은/', '/taste;달지않은/',
        '/taste;쓴/', '/taste;씁쓸한/','/taste;쌉쌀한/', '/taste;달콤씁쓸한/',
        '/taste;안쓴/', '/taste;안 쓴/', '/taste;쓰지 않은/',
        '/taste;신/', '/taste;상큼한/', '/taste;새콤달콤한/', '/taste;시지 않은/', '/taste;시지않은/',
        '/taste;쓰지않은/','/taste;안신/', '/taste;안 신/',
        '/taste;과일/', '/taste;고소한/', '/taste;구수한/']

cnt = 55
slots = []
append_text = slots.append        

# 문장 불러오기 함수
def slots_txt(filename):
    
    f = open(filename, 'r', encoding = 'utf-8')
    lines = f.readlines()
        
    for line in lines:
        # txt 파일 내 주석 제거
        if "#" in line:
            line = line.replace(line,"")
        if "{1}" or "{2}" or "{3}" or "{4}" in line:
            line = line.replace("{1}", random.choice(beer_types)).strip()    
            line = line.replace("{2}", random.choice(beer_abv)).strip()

            line = line.replace("{3}", random.choice(beer_flavor)).strip()
            line = line.replace("{4}", random.choice(beer_taste)).strip()
            
            # 정규 표현식 맛, 향 명사 표현             
            line = re.sub(re.compile(r'/taste;과일/\s*(거|걸로|게|건데|으로|것)'), '/taste;과일/맛 나는 거', line)
            line = re.sub(re.compile(r'/flavor;과일/\s*(거|걸로|게|건데|으로|것)'), '/flavor;과일/향 나는 거', line)
            line = re.sub(re.compile(r'/flavor;홉/\s*(거|걸로|게|건데|으로|것)'), '/flavor;홉/향 나는 거', line)
            line = re.sub(re.compile(r'/flavor;꽃/\s*(거|걸로|게|건데|으로|것)'), '/flavor;꽃/향 나는 거', line)
            line = re.sub(re.compile(r'/flavor;커피/\s*(거|걸로|게|건데|으로|것)'), '/flavor;커피/향 나는 거', line)
            
            slots.append(line)
                        
    f.close()

# 슬롯이 없는 문장 불러오기
slots_txt("./slot_txt/slot_de.txt")

# 문장 틀 불러오기
for i in range(cnt):
    slots_txt("./slot_txt/slot_1.txt")
    slots_txt("./slot_txt/slot_2.txt")
    slots_txt("./slot_txt/slot_3.txt")
    slots_txt("./slot_txt/slot_4.txt")
    
# 중복 제거    
slots_unique = set(slots)
slots = list(slots_unique)

# data.txt 에 저장
file = 'data.txt'
with open(file, 'w+', encoding = 'UTF-8') as f:
    f.write('\n'.join(slots))

print("")    
print("data.txt complete")
print("sentence cnt :", len(slots))