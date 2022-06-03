import random

# 슬롯 : 종류, 도수, 맛, 향 
beer_types = ['/type;에일/', '/type;IPA/', '/type;라거/', '/type;바이젠/', '/type;스타우트/', '/type;흑맥주/']
beer_abv = ['/abv;3/', '/abv;4/', '/abv;5/', '/abv;6/', '/abv;7/', '/abv;8/']
beer_taste = ['/taste;단맛/', '/taste;쓴맛/', '/taste;신맛/', '/taste;고소한 맛/', '/taste;상큼한 맛/']
beer_flavor = ['/flavor;과일향/', '/flavor;홉향/', '/flavor;꽃향기/', '/flavor;상큼한 향/']

#/종류;{random.choice(beer_types)}/
#/도수;{random.choice(beer_abv)}/
#/맛;{random.choice(beer_taste)}/
#/향;{random.choice(beer_flavor)}/

cnt = 50000

# 슬롯 0
slot = ["안녕하세요", "맥주 추천해줘"]

# 슬롯 1
# 종류
for i in range(cnt):
    text = f'{random.choice(beer_types)} 종류로 추천해주세요.'
    slot.append(text)
    text = f'{random.choice(beer_types)} 중에 하나 주세요.'
    slot.append(text)
    
# 도수
for i in range(cnt):
    text = f'{random.choice(beer_abv)}도 맥주 추천해주세요.'
    slot.append(text)
    text = f'{random.choice(beer_abv)}도 이하 맥주 추천해주세요.'
    slot.append(text)
    text = f'{random.choice(beer_abv)}도 이상 맥주 추천해주세요.'
    slot.append(text)
    
# 맛
for i in range(cnt):
    text = f'{random.choice(beer_taste)}이 나는 맥주 추천해주세요.'
    slot.append(text)
    
# 향
for i in range(cnt):
    text = f'{random.choice(beer_flavor)}이 나는 맥주 추천해주세요.'
    slot.append(text)

# 슬롯 2
# 도수 + 종류
for i in range(cnt):
    text = f"{random.choice(beer_abv)}도 맥주 중에 {random.choice(beer_types)} 종류 중 추천해주세요."
    slot.append(text)
    text = f"{random.choice(beer_abv)}도 이상 맥주 중에 {random.choice(beer_types)} 종류 중 추천해주세요."
    slot.append(text)
    text = f"{random.choice(beer_abv)}도 이하 맥주 중에 {random.choice(beer_types)} 종류 중 추천해주세요."
    slot.append(text)
    text = f"{random.choice(beer_types)} 중에 {random.choice(beer_abv)}도 맥주 추천해주세요."
    slot.append(text)
    text = f"{random.choice(beer_types)} 중에 {random.choice(beer_abv)}도 이상 맥주 추천해주세요."
    slot.append(text)
    text = f"{random.choice(beer_types)} 중에 {random.choice(beer_abv)}도 이하 맥주 추천해주세요."
    slot.append(text)

# 도수 + 맛
for i in range(cnt):
    text = f"{random.choice(beer_abv)}도 맥주 중에 {random.choice(beer_taste)}이 나는 맥주 추천해주세요."
    slot.append(text)
    text = f"{random.choice(beer_abv)}도 이상 맥주 중에 {random.choice(beer_taste)}이 나는 맥주 추천해주세요."
    slot.append(text)
    text = f"{random.choice(beer_abv)}도 이하 맥주 중에 {random.choice(beer_taste)}이 나는 맥주 추천해주세요."
    slot.append(text)
    text = f"{random.choice(beer_taste)}이 나는 맥주 중에 {random.choice(beer_abv)}도 맥주 추천해주세요."
    slot.append(text)
    text = f"{random.choice(beer_taste)}이 나는 맥주 중에 {random.choice(beer_abv)}도 이상 맥주 추천해주세요."
    slot.append(text)
    text = f"{random.choice(beer_taste)}이 나는 맥주 중에 {random.choice(beer_abv)}도 이하 맥주 추천해주세요."
    slot.append(text)

# 도수 + 향
for i in range(cnt):
    text = f"{random.choice(beer_abv)}도 맥주 중에 {random.choice(beer_flavor)} 이나는 맥주 추천해주세요."
    slot.append(text)
    text = f"{random.choice(beer_abv)}도 이상 맥주 중에 {random.choice(beer_flavor)} 나는 맥주 추천해주세요."
    slot.append(text)
    text = f"{random.choice(beer_abv)}도 이하 맥주 중에 {random.choice(beer_flavor)} 나는 맥주 추천해주세요."
    slot.append(text)
    text = f"{random.choice(beer_flavor)} 나는 맥주 중에 {random.choice(beer_abv)}도 맥주 추천해주세요."
    slot.append(text)
    text = f"{random.choice(beer_flavor)} 나는 맥주 중에 {random.choice(beer_abv)}도 이상 맥주 추천해주세요."
    slot.append(text)
    text = f"{random.choice(beer_flavor)} 나는 맥주 중에 {random.choice(beer_abv)}도 이하 맥주 추천해주세요."
    slot.append(text)

# 종류 + 맛
for i in range(cnt):
    text = f"{random.choice(beer_types)} 중에 {random.choice(beer_taste)}이 나는 맥주 추천해주세요."
    slot.append(text)
    text = f"{random.choice(beer_types)} 중에 {random.choice(beer_taste)} 맥주 추천해주세요."
    slot.append(text)
    text = f"{random.choice(beer_taste)}이 나는 맥주 중에 {random.choice(beer_types)} 종류 추천해주세요."
    slot.append(text)
    text = f"{random.choice(beer_taste)}이 나는 맥주 중에 {random.choice(beer_types)} 종류의 맥주 추천해주세요."
    slot.append(text)

# 종류 + 향
for i in range(cnt):
    text = f"{random.choice(beer_types)} 중 {random.choice(beer_flavor)}이 나는 맥주 추천해주세요."
    slot.append(text)
    # text = f"{random.choice(beer_types)} 중에 {random.choice(beer_flavor)} 맥주 추천해주세요."
    # slot.append(text)
    text = f"{random.choice(beer_flavor)}이 나는 맥주 중에 {random.choice(beer_types)} 종류 추천해주세요."
    slot.append(text)
    text = f"{random.choice(beer_flavor)}이 나는 맥주 중에 {random.choice(beer_types)} 종류의 맥주 추천해주세요."
    slot.append(text)

# 맛 + 향
for i in range(cnt):
    text = f"{random.choice(beer_taste)}이 나면서 {random.choice(beer_flavor)}이 나는 맥주 추천해주세요."
    slot.append(text)
    # text = f"{random.choice(beer_abv)}도 이상인 {random.choice(beer_types)} 종류로 추천해주세요."
    # slot.append(text)
    text = f"{random.choice(beer_flavor)}이 나면서 {random.choice(beer_abv)}이 나는 맥주 추천해주세요."
    slot.append(text)
    # text = f"{random.choice(beer_types)} 맥주 중에 {random.choice(beer_abv)} 이상 인 맥주 추천해주세요."
    # slot.append(text)

# 슬롯 3
# 도수 + 종류 + 맛
for i in range(cnt):
    text = f"{random.choice(beer_abv)}도 인 {random.choice(beer_types)} 중에 {random.choice(beer_taste)}이 나는 맥주 추천해 주세요."
    slot.append(text)
    
# 도수 + 종류 + 향
for i in range(cnt):
    text = f"{random.choice(beer_abv)}도 인 {random.choice(beer_types)} 중에 {random.choice(beer_flavor)}이 나는 맥주 추천해 주세요."
    slot.append(text)

# 도수 + 맛 + 향
for i in range(cnt):
    text = f"{random.choice(beer_abv)}도 인 맥주 중에 {random.choice(beer_taste)}과 {random.choice(beer_flavor)}이 나는 맥주 추천해 주세요."
    slot.append(text)

# 종류 + 맛 + 향
for i in range(cnt):
    text = f"{random.choice(beer_types)} 중에 {random.choice(beer_taste)}과 {random.choice(beer_flavor)}이 나는 맥주 추천해 주세요."
    slot.append(text)

# 슬롯 4
for i in range(cnt):
    text = f"도수가 {random.choice(beer_types)}도 인 {random.choice(beer_types)} 중에 {random.choice(beer_flavor)}과 {random.choice(beer_taste)}이 나는 맥주 추천해 주세요."
    slot.append(text)

# 중복 제거    
slot_unique = set(slot)
slot = list(slot_unique)

# data.txt 에 저장
file = 'data.txt'
with open(file, 'w+', encoding = 'UTF-8') as f:
    f.write('\n'.join(slot))
    
print("data.txt complete")
print("sentence cnt :", len(slot)) 