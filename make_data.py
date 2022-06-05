import random

# 슬롯 : 종류, 도수, 맛, 향 
beer_types = ['/type;에일/', '/type;IPA/', '/type;라거/', '/type;바이젠/', '/type;흑맥주/']
beer_abv = ['/abv;3/', '/abv;4/', '/abv;5/', '/abv;6/', '/abv;7/', '/abv;8/']
beer_flavor = ['/flavor;과일향/', '/flavor;홉향/', '/flavor;꽃향기/', '/flavor;상큼한향/', '/flavor;묵직한향/']
beer_taste = [
        '/taste;단맛/', '/taste;달달한맛/', '/taste;달콤한맛/', '/taste;달큰한맛/', '/taste;감미로운맛/', '/taste;꿀맛/', '/taste;달짝지근한맛/',
        '/taste;단/', '/taste;달달한/', '/taste;달콤한/', '/taste;달큰한/', '/taste;감미로운/', '/taste;꿀/', '/taste;달짝지근한/',
        '/taste;안단맛/', '/taste;안 단맛/', '/taste;달지 않은맛/', '/taste;달지않은맛/', '/taste;쓴맛/', '/taste;씁쓸한맛/', '/taste;떫은맛/', 
        '/taste;안단/', '/taste;안 단/', '/taste;달지 않은/', '/taste;달지않은/', '/taste;쓴/', '/taste;씁쓸한/', '/taste;떫은/', 
        '/taste;쌉싸름한맛/', '/taste;달콤씁쓸한맛/', 
        '/taste;쌉싸름한/', '/taste;달콤씁쓸한/', 
        '/taste;신맛/', '/taste;시큼한맛/', '/taste;새콤한맛/', '/taste;상큼한맛/', '/taste;새콤달콤한맛/',
        '/taste;신/', '/taste;시큼한/', '/taste;새콤한/', '/taste;상큼한/', '/taste;새콤달콤한/',
        '/taste;과일맛/', '/taste;레몬맛/', '/taste;오렌지맛/', '/taste;자몽맛/', '/taste;복숭아맛/', 
        '/taste;고소한맛/', '/taste;구수한맛/', '/taste;묵직한맛/', '/taste;가벼운맛/', '/taste;프레쉬한맛', '/taste;진한맛', '/taste;연한맛',
        '/taste;고소한/', '/taste;구수한/', '/taste;묵직한/', '/taste;가벼운/', '/taste;프레쉬한', '/taste;진한', '/taste;연한'
        ]

# 슬롯 0 // 30 문장
beer_default = ["안녕하세요", "맥주 추천해주세요", "맥주 추천", "맥주 종류", "물 주세요", "맥주 말고 다른건 없나요?",
        "소주 주세요", "얼마인가요?", "다른 맥주 주세요", "음료수 주세요", "다른 맥주 없나요?", "도수 낮은 맥주 주세요",
        "계산해 주세요", "주문이요", "주문할게요", "대리 있나요?", "신분증 안가져왔어요", "안 취했어요",
        "화장실이 어디인가요?", "저기요", "여기요", "사장님", "물티슈 주세요", "앞접시 주세요",
        "숟가락 주세요", "젓가락 주세요", "포크 주세요", "육수 주세요", "기본 안주 더 주세요","메뉴판 주세요"
        ]

# cnt = len(beer_types) * len(beer_abv) * len(beer_flavor) * len(beer_taste)
cnt = 2000

slot = []
beer_default.extend(slot)
append_text = slot.append

# 슬롯 1
# 종류
for types in beer_types:    
    append_text(f'{random.choice(types)}')
    append_text(f'{random.choice(types)} 종류로 추천해주세요.')
    append_text(f'{random.choice(types)}로 추천해주세요.')
    append_text(f'{random.choice(types)} 추천해주세요.')

# 도수
for abv in beer_abv:    
    append_text(f'{random.choice(abv)}')
    append_text(f'{random.choice(abv)}도 맥주 추천해주세요.')
    append_text(f'{random.choice(abv)}도 이하 맥주 추천해주세요.')
    append_text(f'{random.choice(abv)}도 이상 맥주 추천해주세요.')
     
# 맛
for taste in beer_taste:
    append_text(f'{random.choice(taste)}')
    append_text(f'{random.choice(taste)}이 나는 맥주 추천해주세요.')
    append_text(f'{random.choice(taste)} 나는 맥주 추천해주세요.')
    append_text(f'{random.choice(taste)}이 안나는 맥주 추천해주세요.')
    append_text(f'{random.choice(taste)} 안나는 맥주 추천해주세요.')

# 향
for flavor in beer_flavor:    
    append_text(f'{random.choice(flavor)}')
    append_text(f'{random.choice(flavor)}이 나는 맥주 추천해주세요.')
    append_text(f'{random.choice(flavor)} 나는 맥주 추천해주세요.')
    append_text(f'{random.choice(flavor)}이 안나는 맥주 추천해주세요.')
    append_text(f'{random.choice(flavor)} 안나는 맥주 추천해주세요.')

for i in range(cnt):
# 슬롯 2 
    # 도수 + 종류
    append_text(f'{random.choice(abv)}{random.choice(beer_types)}')
    append_text(f'{random.choice(abv)}도 맥주 중에 {random.choice(beer_types)} 추천해주세요.')
    append_text(f'{random.choice(abv)}도 이상 맥주 중에 {random.choice(beer_types)} 추천해주세요.')
    append_text(f'{random.choice(abv)}도 이하 맥주 중에 {random.choice(beer_types)} 추천해주세요.')

    # 도수 + 맛
    append_text(f'{random.choice(abv)}{random.choice(beer_taste)}')
    append_text(f"{random.choice(beer_abv)}도 맥주 중에 {random.choice(beer_taste)}이 나는 맥주 추천해주세요.")
    append_text(f"{random.choice(beer_abv)}도 이상 맥주 중에 {random.choice(beer_taste)}이 나는 맥주 추천해주세요.")
    append_text(f"{random.choice(beer_abv)}도 이하 맥주 중에 {random.choice(beer_taste)}이 나는 맥주 추천해주세요.")
    append_text(f"{random.choice(beer_taste)}이 나는 맥주 중에 {random.choice(beer_abv)}도 맥주 추천해주세요.")
    append_text(f"{random.choice(beer_taste)}이 나는 맥주 중에 {random.choice(beer_abv)}도 이상 맥주 추천해주세요.")
    append_text(f"{random.choice(beer_taste)}이 나는 맥주 중에 {random.choice(beer_abv)}도 이하 맥주 추천해주세요.")

    # 도수 + 향
    append_text(f'{random.choice(abv)}{random.choice(beer_flavor)}')
    append_text(f"{random.choice(beer_abv)}도 맥주 중에 {random.choice(beer_flavor)} 이나는 맥주 추천해주세요.")
    append_text(f"{random.choice(beer_abv)}도 이상 맥주 중에 {random.choice(beer_flavor)} 나는 맥주 추천해주세요.")
    append_text(f"{random.choice(beer_abv)}도 이하 맥주 중에 {random.choice(beer_flavor)} 나는 맥주 추천해주세요.")
    append_text(f"{random.choice(beer_flavor)} 나는 맥주 중에 {random.choice(beer_abv)}도 맥주 추천해주세요.")
    append_text(f"{random.choice(beer_flavor)} 나는 맥주 중에 {random.choice(beer_abv)}도 이상 맥주 추천해주세요.")
    append_text(f"{random.choice(beer_flavor)} 나는 맥주 중에 {random.choice(beer_abv)}도 이하 맥주 추천해주세요.")

    # 종류 + 맛
    append_text(f'{random.choice(types)}{random.choice(beer_taste)}')
    append_text(f"{random.choice(beer_types)} 중에 {random.choice(beer_taste)}이 나는 맥주 추천해주세요.")
    append_text(f"{random.choice(beer_types)} 중에 {random.choice(beer_taste)} 맥주 추천해주세요.")
    append_text(f"{random.choice(beer_taste)}이 나는 맥주 중에 {random.choice(beer_types)} 종류 추천해주세요.")
    append_text(f"{random.choice(beer_taste)}이 나는 맥주 중에 {random.choice(beer_types)} 종류의 맥주 추천해주세요.")

    # 종류 + 향
    append_text(f'{random.choice(types)}{random.choice(beer_flavor)}')
    append_text(f"{random.choice(beer_types)} 중 {random.choice(beer_flavor)}이 나는 맥주 추천해주세요.")
    append_text(f"{random.choice(beer_types)} 중에 {random.choice(beer_flavor)} 맥주 추천해주세요.")
    append_text(f"{random.choice(beer_flavor)}이 나는 맥주 중에 {random.choice(beer_types)} 종류 추천해주세요.")
    append_text(f"{random.choice(beer_flavor)}이 나는 맥주 중에 {random.choice(beer_types)} 종류의 맥주 추천해주세요.")

    # 맛 + 향
    append_text(f'{random.choice(taste)}{random.choice(beer_flavor)}')
    append_text(f"{random.choice(beer_taste)}이 나면서 {random.choice(beer_flavor)}이 나는 맥주 추천해주세요.")
    append_text(f"{random.choice(beer_abv)}도 이상인 {random.choice(beer_types)} 종류로 추천해주세요.")
    append_text(f"{random.choice(beer_flavor)}이 나면서 {random.choice(beer_abv)}이 나는 맥주 추천해주세요.")
    append_text(f"{random.choice(beer_types)} 맥주 중에 {random.choice(beer_abv)} 이상 인 맥주 추천해주세요.")

# 슬롯 3
    # 도수 + 종류 + 맛
    append_text(f'{random.choice(abv)}{random.choice(beer_types)}{random.choice(beer_taste)}')
    append_text(f"{random.choice(beer_abv)}도 인 {random.choice(beer_types)} 중에 {random.choice(beer_taste)}이 나는 맥주 추천해 주세요.")
    
    # 도수 + 종류 + 향
    append_text(f'{random.choice(abv)}{random.choice(beer_types)}{random.choice(beer_flavor)}')
    append_text(f"{random.choice(beer_abv)}도 인 {random.choice(beer_types)} 중에 {random.choice(beer_flavor)}이 나는 맥주 추천해 주세요.")

    # 도수 + 맛 + 향
    append_text(f'{random.choice(abv)}{random.choice(beer_taste)}{random.choice(beer_flavor)}')
    append_text(f"{random.choice(beer_abv)}도 인 맥주 중에 {random.choice(beer_taste)}과 {random.choice(beer_flavor)}이 나는 맥주 추천해 주세요.")

    # 종류 + 맛 + 향
    append_text(f'{random.choice(types)}{random.choice(beer_taste)}{random.choice(beer_flavor)}')
    append_text(f"{random.choice(beer_types)} 중에 {random.choice(beer_taste)}과 {random.choice(beer_flavor)}이 나는 맥주 추천해 주세요.")

# 슬롯 4
    append_text(f'{random.choice(types)}{random.choice(beer_taste)}{random.choice(beer_flavor)}{random.choice(beer_abv)}')
    append_text(f"도수가 {random.choice(beer_types)}도 인 {random.choice(beer_types)} 중에 {random.choice(beer_flavor)}과 {random.choice(beer_taste)}이 나는 맥주 추천해 주세요.")

# 중복 제거    
slot_unique = set(slot)
slot = list(slot_unique)

# data.txt 에 저장
file = 'data.txt'
with open(file, 'w+', encoding = 'UTF-8') as f:
    f.write('\n'.join(slot))
    
print("data.txt complete")
print("sentence cnt :", len(slot)) 