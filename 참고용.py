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

def make_data():
    sentences = ['다 좋아요.',
                 '앗 잠깐만요.',
                '뭐가 제일 잘나가요?',
                '물 주세요.'
                ]
    pass


sandwich_slot = ['/sandwich;페퍼로니 피자썹/', '/sandwich;이탈리안 비엠티/', '/sandwich;에그마요/',
                   '/sandwich;스테이크 치즈/', '/sandwich;써브웨이 클럽/', '/sandwich;로티세리 바비큐 치킨/',
                   '/sandwich;풀드 포그 바비큐/', '/sandwich;치킨 데리야끼/', '/sandwich;스파이시 이탈리안/',
                   '/sandwich;쉬림프/', '/sandwich;페퍼 치킨 슈니첼/', '/sandwich;K-바비큐/',
                   '/sandwich;터키 베이컨 아보카도/', '/sandwich;로스트 치킨/', '/sandwich;베지/',
                   '/sandwich;터키/', '/sandwich;햄/', '/sandwich;참치/', '/sandwich;미트볼/', '/sandwich;비엘티/']

bread_slot = ['/bread;화이트/', '/bread;하티/', '/bread;파마산 오레가노/', '/bread;위트/', '/bread;허니오트/', '/bread;플랫/']

cheese_slot = ['/cheese;아메리칸 치즈/', '/cheese;슈레드 치즈/', '/cheese;모짜렐라 치즈/']

extras_slot = ['/extras;미트 추가/', '/extras;쉬림프 더블업 추가/', '/extras;에그마요 추가/',
               '/extras;오믈렛 추가/', '/extras;아보카도 추가/', '/extras;베이컨 추가/',
               '/extras;페퍼로니 추가/', '/extras;치즈 추가/']

vegetable_slot = ['/vegetable;양상추/', '/vegetable;토마토/', '/vegetable;오이/', '/vegetable;피망/',
                '/vegetable;피클/', '/vegetable;올리브/', '/vegetable;할라피뇨/', '/vegetable;양파/']

sauce_slot = ['/sauce;랜치/', '/sauce;마요네즈/', '/sauce;스위트 어니언/', '/sauce;허니 머스타드/',
               '/sauce;스위트 칠리/', '/sauce;핫 칠리/', '/sauce;사우스 웨스트/', '/sauce;머스타드/',
               '/sauce;홀스래디쉬/', '/sauce;올리브 오일/', '/sauce;레드와인 식초/', '/sauce;소금/',
               '/sauce;후추/', '/sauce;스모크 바베큐/']

drinks_slot = ['/drinks;코카콜라/', '/drinks;스프라이트/', '/drinks;닥터페퍼/', '/drinks;코카콜라 제로/',
                '/drinks;생수/', '/drinks;아메리카노/']

cookies_slot = ['/cookies;더블 초코칩/', '/cookies;초코칩/', '/cookies;오트밀 레이즌/',
                 '/cookies;라즈베리 치즈케잌/', '/cookies;화이트 초코 마카다미아/', '/cookies;파인애플 쿠키/']

length_slot = ['/length;15cm/', '/length;30cm/', '/length;십오센치/', '/length;삼십센치/',
               '/length;15센치/', '/length;30센치/']

def gen_data():
    sentences = ['네 다 넣어주세요.',
                '포장이요.',
                '앗 잠깐만요.',
                '뭐가 제일 잘나가요?',
                '추천소스로 뿌려 주세요.',
                '매운소스에는 뭐가 있어요?',
                '안매운소스가 어떤거에요?',
                '달콤한 소스로 해주세요.',
                '스위트 칠리 많이 맵나요?',
                '음료 주세요.',
                '네 감사합니다.',
                '네 괜찮아요.',
                '인기 많은 걸로 주세요.',
                '잠시만요.',
                '주문할게요.',
                '먹고가요.',
                '안녕히계세요.',
                '휴지 어디있어요?',
                '물티슈 하나 주세요.',
                '포장 예약 했어요.',
                '포인트 해주세요.',
                '포인트 없어요.',
                '쿠폰 있어요.',
                '이거 어떻게 써요?',
                '뭐 먹지?',
                '화장실은 어디에요?',
                '휴지 주세요.',
                '티슈 주세요.',
                '빨대 어딨어요?',
                '멤버십 포인트 있어요.',
                '물은 어디있어요?']

    # 빵_치즈_소스
    # 빵 화이트에 슈레드 치즈 주세요. 스모크 바베큐 뿌려주세요. 
    # 화이트요. 슈레드 치즈요. 스모크 바베큐 소스요.
    for b in bread_slot:
        for c in cheese_slot:
            for sc in sauce_slot:
                text = f'빵 {b}에 {c} 주세요. {sc} 뿌려주세요.'
                sentences.append(text)
                text = f'{b}이요. {c}요. {sc} 소스요.'
                sentences.append(text)

    # 빵_길이
    # 빵은 화이트 15센치로 할게요.
    # 15센치 화이트로 주세요.
    for b in bread_slot:
        for l in length_slot:
            text = f'빵은 {b} {l}로 할게요.'
            sentences.append(text)
            text = f'{l} {b}로 주세요.'
            sentences.append(text)

    # 야채_소스
    # 양상추 빼주시고, 소스는.. 잠시만요. 랜치로 할게요.
    # 양상추 빼고 다 넣어 주세요. 랜치 소스요.
    for v in vegetable_slot:
        for sc in sauce_slot:
            text = f'{v} 빼주시고, 소스는.. 잠시만요. {sc}로 할게요.'
            sentences.append(text)
            text = f'{v} 빼고 다 넣어주세요. {sc} 소스요.'
            sentences.append(text)

    # 샌드위치
    # 추천 해주세요. 풀드 포크 바베큐 할게요.
    # 풀드 포크 바베큐 맛있나요? 그럼 그걸로 주세요.
    for s in sandwich_slot:
        text = f'추천 해주세요. {s} 할게요.'
        sentences.append(text)
        text = f'{s} 맛있나요? 그럼 그걸로 주세요.'
        sentences.append(text)

    # 빵
    # 빵은 어떤게 맛있나요? 그럼 화이트로 주세요.
    for b in bread_slot:
        text = f'빵은 어떤게 맛있나요? 그럼 {b}로 주세요.'
        sentences.append(text)

    # 치즈
    # 치즈 뭐하지.. 아메리칸 치즈로 주세요.
    # 토핑은 안하고 슈레드 치즈 주세요.
    for c in cheese_slot:
        text = f'치즈 뭐하지.. {c} 주세요.'
        sentences.append(text)
        text = f'토핑은 안하고 {c} 넣어주세요.'
        sentences.append(text)

    # 소스
    # 여기에 소스 어떤게 좋은가요? 그럼 랜치로 할게요.
    # 어.. 랜치로 뿌려주세요.
    for sc in sauce_slot:
        text = f'여기에 소스 어떤게 좋은가요? 그럼 {sc}로 할게요.'
        sentences.append(text)
        text = f'어.. {sc}로 뿌려주세요.'
        sentences.append(text)

    # 길이_샌드위치_빵_치즈_야채_소스_랜덤 200개
    for x in range(200):
        text = f'{random.choice(length_slot)} {random.choice(sandwich_slot)}에 {random.choice(bread_slot)}빵에, {random.choice(cheese_slot)}, {random.choice(vegetable_slot)} 빼주시고 {random.choice(sauce_slot)}소스로 주세요.'
        sentences.append(text)

    # 샌드위치_빵_치즈_소스_야채_랜덤 400개
    for x in range(200):
        text = f'{random.choice(sandwich_slot)}하나요. {random.choice(bread_slot)}빵에, {random.choice(cheese_slot)}주세요. {random.choice(sauce_slot)} 소스에 {random.choice(vegetable_slot)} 빼주세요.'
        sentences.append(text)
        text = f'{random.choice(sandwich_slot)}요. {random.choice(bread_slot)}요. {random.choice(cheese_slot)}요. {random.choice(vegetable_slot)} 빼주세요. {random.choice(sauce_slot)}로 해주세요.'
        sentences.append(text)

    # 샌드위치_빵_치즈_소스_랜덤 400
    for x in range(200):
        text = f'{random.choice(sandwich_slot)}에 빵은 {random.choice(bread_slot)}로 주시고 치즈는 {random.choice(cheese_slot)}, 소스는 {random.choice(sauce_slot)}로 주세요.'
        sentences.append(text)
        text = f'{random.choice(sandwich_slot)}로 주시고 {random.choice(bread_slot)} 빵에 {random.choice(cheese_slot)} 치즈로 주세요. {random.choice(sauce_slot)} 소스뿌려 주세요.'
        sentences.append(text)

    # 샌드위치_길이_빵_랜덤 200
    for x in range(200):
        text = f'{random.choice(sandwich_slot)} {random.choice(length_slot)}에 {random.choice(bread_slot)}로 주세요.'
        sentences.append(text)


    sentences = set(sentences)
    sentences = list(sentences)
    # len(sentences)
    return sentences