import random

# 슬롯 : 종류, 도수, 맛, 향 
beer_types = ['/type;에일/', '/type;IPA/', '/type;라거/', '/type;바이젠/', '/type;흑맥주/']
beer_abv = ['/abv;3도/', '/abv;4도/', '/abv;5도/', '/abv;6도/', '/abv;7도/', '/abv;8도/',
            '/abv;3도이상/', '/abv;4도이상/', '/abv;5도이상/', '/abv;6도이상/', '/abv;7도이상/',
           '/abv;3도 이상/', '/abv;4도 이상/', '/abv;5도 이상/', '/abv;6도 이상/', '/abv;7도 이상/',
           '/abv;4도이하/', '/abv;5도이하/', '/abv;6도이하/', '/abv;7도이하/', '/abv;8도이하/',
            '/abv;4도 이하/', '/abv;5도 이하/', '/abv;6도 이하/', '/abv;7도 이하/', '/abv;8도 이하/']

beer_flavor = ['/flavor;과일/', '/flavor;홉/', '/flavor;꽃/', '/flavor;상큼한/', '/flavor;커피/', '/flavor;스모키한/']
beer_taste = [
        '/taste;단/', '/taste;달달한/', '/taste;달콤한/',
        '/taste;안단/', '/taste;안 단/', '/taste;달지 않은/', '/taste;달지않은/',
        '/taste;쓴/', '/taste;씁쓸한/','/taste;쌉쌀한/', '/taste;달콤씁쓸한/',
        '/taste;안쓴/', '/taste;안 쓴/', '/taste;쓰지 않은/',
        '/taste;신/', '/taste;상큼한/', '/taste;새콤달콤한/', '/taste;시지 않은/', '/taste;시지않은/',
        '/taste;쓰지 않은/','/taste;안신/', '/taste;안 신/',
        '/taste;과일/', '/taste;고소한/', '/taste;구수한/']

cnt = 80
slot = []
append_text = slot.append

# 문장 불러오기 함수
def slot_txt(filename):
    
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
            slot.append(line)     
                       
    f.close()

# 슬롯이 없는 문장 불러오기
slot_txt("./slot_txt/slot_de.txt")

# 문장 틀 불러오기
for i in range(cnt):
    slot_txt("./slot_txt/slot_1.txt")
    slot_txt("./slot_txt/slot_2.txt")
    slot_txt("./slot_txt/slot_3.txt")
    slot_txt("./slot_txt/slot_4.txt")
    # slot_txt("slot_merge.txt")
    
# 중복 제거    
slot_unique = set(slot)
slot = list(slot_unique)

# data.txt 에 저장
file = 'data.txt'
with open(file, 'w+', encoding = 'UTF-8') as f:
    f.write('\n'.join(slot))

print("")    
print("data.txt complete")
print("sentence cnt :", len(slot)) 