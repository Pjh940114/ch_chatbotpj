import os, re
import argparse

# get tokenizer python script
from tokenizationK import FullTokenizer

## get tokenizer vocab file
tokenizer = FullTokenizer(vocab_file="vocab.korean.rawtext.list")

## ----------------- 문제 1 ---------------- ##
# slot_pattern = [알맞은 정규표현식으로 채워보세요]
slot_pattern = re.compile(r"/(.+);(.+)/")
# multi_spaces = [알맞은 정규표현식으로 채워보세요]
multi_spaces = re.compile(r"\s+")
## ---------------------------------------- ##

def process_file(file_path, output_dir):
  if not os.path.isdir(output_dir):
    os.mkdir(output_dir)
  
  data = open(file_path).read().splitlines()

  ## line별로 processing
  processed_data = [process_line(line, tokenizer) for line in data]

  ## ----------------- 문제 2 ---------------- ##
  # tokens = 알맞은 코드를 써주세요
  tokens = list(map(lambda x: x[0], processed_data))
  
  # tags = 알맞은 코드를 써주세요
  tags = list(map(lambda x: x[1], processed_data))
  ## ---------------------------------------- ##

  ## seq_in : 토큰들로만 이루어진 파일
  ## seq_out : 태그들로만 이루어진 파일
  seq_in = os.path.join(output_dir, "seq.in")
  seq_out = os.path.join(output_dir, "seq.out")

  with open(seq_in, "w") as f:
    f.write("\n".join(tokens)+ "\n")

  with open(seq_out, "w") as f:
    f.write("\n".join(tags)+ "\n")

def process_line(sentence, tokenizer):
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

    ## 엔티티를 토크나이즈 한 후, 토큰별로 태그를 추가해준다. 
    entity_tokens = " ".join(tokenizer.tokenize(entity))

    tokens += entity_tokens + " "
    tags += (slot + " ") * len(entity_tokens.split())

    ## 조사가 붙은 것이며(eg. "/슬롯/이", "/슬롯/에서"),
    ## 조사에 대해서 추가적으로 토큰 및 태그를 추가해 준다.
    if not word.endswith("/"):
      ## 우선 "/" 뒤에 오는 조사를 찾아 준다.
      josa = word[word.rfind("/")+1:]
      josa_tokens = " ".join(tokenizer.tokenize(josa))

      tokens += josa_tokens + " "
      tags += "O " * len(josa_tokens.split())
    
    elif "/" in word:
      prefix = word.split("/")[0]
      tokenized_prefix = " ".join(tokenizer.tokenize(prefix))
      tokens += tokenized_prefix + " "
      tags += "O " * len(tokenized_prefix.split())

      slot, entity = slot_pattern_found[slot_index]
      slot_index += 1

      entity_tokens = " ".join(tokenizer.tokenize(entity))

      tokens += entity_tokens + " "
      tags += (slot + " ") * len(entity_tokens.split())

    else:
      word_tokens = " ".join(tokenizer.tokenize(word))
      tokens += word_tokens + " "
      tags += "O " * len(word_tokens.split())
  
  tokens = multi_spaces.sub(" ", tokens.strip())
  tags = multi_spaces.sub(" ", tags.strip())

  ## 만일 토큰의 개수와 슬롯의 개수가 맞지 않다면 본래 라인과 더불어 토큰/슬롯들을 프린트해준다.
  ## ----------------- 문제 3 ---------------- ##
  # [if 문으로 시작하는 코드 작성 ! ]
  if len(tokens.split()) != len(tags.split()):      
        print(sentence)
        print("\t" + tokens + "\t", len(tokens.split()))
        print("\t" + tags + "\t", len(tags.split()))
  ## ---------------------------------------- ##
  
  return tokens, tags