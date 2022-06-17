import re


sentence = "/type;흑맥주/ 할게"

slot_pattern = re.compile(r"/(.+);(.+)/")
print(slot_pattern.findall(sentence))
print(slot_pattern.sub("/슬롯/", sentence))

    
slot_pattern_found = slot_pattern.findall(sentence)
line_refined = slot_pattern.sub("/슬롯/", sentence)
tokens = ""
tags = ""
slot_index = 0

for word in line_refined.split():
## "/게임명;일곱개의 대죄/" --> ("게임명", "일곱개의 대죄")
    if word.startswith("/"):
        slot, entity = slot_pattern_found[slot_index]
        slot_index += 1
        print(slot, entity)

    ## 엔티티를 토크나이즈 한 후, 토큰별로 태그를 추가해준다. 
    # entity_tokens = " ".join(tokenizer.tokenize(entity))

    # tokens += entity_tokens + " "
    # tags += (slot + " ") * len(entity_tokens.split())

    # ## 조사가 붙은 것이며(eg. "/슬롯/이", "/슬롯/에서"),
    # ## 조사에 대해서 추가적으로 토큰 및 태그를 추가해 준다.
    # if not word.endswith("/"):
    #     ## 우선 "/" 뒤에 오는 조사를 찾아 준다.
    #     josa = word[word.rfind("/")+1:]
    #     josa_tokens = " ".join(tokenizer.tokenize(josa))

    #     tokens += josa_tokens + " "
    #     tags += "O " * len(josa_tokens.split())

    # elif "/" in word:
    #     prefix = word.split("/")[0]
    #     tokenized_prefix = " ".join(tokenizer.tokenize(prefix))
    #     tokens += tokenized_prefix + " "
    #     tags += "O " * len(tokenized_prefix.split())

    #     slot, entity = slot_pattern_found[slot_index]
    #     slot_index += 1

    #     entity_tokens = " ".join(tokenizer.tokenize(entity))

    #     tokens += entity_tokens + " "
    #     tags += (slot + " ") * len(entity_tokens.split())

    # else:
    #     word_tokens = " ".join(tokenizer.tokenize(word))
    #     tokens += word_tokens + " "
    #     tags += "O " * len(word_tokens.split())

    # tokens = multi_spaces.sub(" ", tokens.strip())
    # tags = multi_spaces.sub(" ", tags.strip())
