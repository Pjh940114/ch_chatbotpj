import os, re
import argparse

# get tokenizer python script
from tokenizationK import FullTokenizer

## get tokenizer vocab file
tokenizer = FullTokenizer(vocab_file="vocab.korean.rawtext.list")

# 방법 1: 최소매칭 .+?
slot_pattern = re.compile(r"/(.+?);(.+?)/")
# 방법 2 : not [^/]
# slot_pattern = re.compile(r"/([^/]+);([^/+)/")

# 방법 1
multi_spaces = re.compile(r"\s+")
# 방법 2 : 2회 이상의 스페이스를 잡음
# multi_spaces = re.compile(r"\s{2,}")

def process_file(file_path, output_dir):
  if not os.path.isdir(output_dir):
    os.mkdir(output_dir)
  
  data = open(file_path, encoding = 'utf-8').read().splitlines()

  ## line별로 processing
  processed_data = [process_line(line, tokenizer) for line in data] # (토근화된 문장, 슬롯 0 0 슬롯 0 0)

  tokens = list(map(lambda x: x[0], processed_data))
  tags = list(map(lambda x: x[1], processed_data))

  ## seq_in : 토큰들로만 이루어진 파일
  ## seq_out : 태그들로만 이루어진 파일
  seq_in = os.path.join(output_dir, "seq.in")
  seq_out = os.path.join(output_dir, "seq.out")

  with open(seq_in, "w", encoding = 'utf-8') as f:
    f.write("\n".join(tokens)+ "\n")

  with open(seq_out, "w", encoding = 'utf-8') as f:
    f.write("\n".join(tags)+ "\n")

def process_line(sentence, tokenizer):
  #slot_pattern = re.compile()
  # ['/인물;한지민/', '/인물/;한예슬/']
  slot_pattern_found = slot_pattern.findall(sentence)
  
  # '/슬롯/ /슬롯/ /슬롯/ 나오는 드라마 있어'
  line_refined = slot_pattern.sub("/슬롯/", sentence)
  tokens = ""
  tags = ""
  slot_index = 0

  for word in line_refined.split():
    ## "/게임명;일곱개의 대죄/" --> ("게임명", "일곱개의 대죄")
    # /슬롯/ ~ 을 잡는 if문
    if word.startswith("/"):
      slot, entity = slot_pattern_found[slot_index]
      slot_index += 1

    ## 엔티티를 토크나이즈 한 후, 토큰별로 태그를 추가해준다. 
      entity_tokens = " ".join(tokenizer.tokenize(entity))

      tokens += entity_tokens + " "
      tags += (slot + " ") * len(entity_tokens.split())

      ## 조사가 붙은 것이며(eg. "/슬롯/이", "/슬롯/에서"),
      ## 조사에 대해서 추가적으로 토큰 및 태그를 추가해 준다.
      # 조사로 끝나는 것
      if not word.endswith("/"):
      ## 우선 "/" 뒤에 오는 조사를 찾아 준다.
       josa = word[word.rfind("/")+1:]
       josa_tokens = " ".join(tokenizer.tokenize(josa))

       tokens += josa_tokens + " "
       tags += "O " * len(josa_tokens.split())
       
    # 안녕/슬롯/ --> 전처리가 잘못된 경우
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

    # 일반적인 토큰들
    else:
      word_tokens = " ".join(tokenizer.tokenize(word))
      tokens += word_tokens + " "
      tags += "O " * len(word_tokens.split())
  
  tokens = multi_spaces.sub(" ", tokens.strip())
  tags = multi_spaces.sub(" ", tags.strip())

  ## 만일 토큰의 개수와 슬롯의 개수가 맞지 않다면 본래 라인과 더불어 토큰/슬롯들을 프린트해준다.

  if len(tokens.split()) != len(tags.split()):      
        print(sentence)
        print("\t" + tokens + "\t", len(tokens.split()))
        print("\t" + tags + "\t", len(tags.split()))
  
  return tokens, tags

process_file("data.txt", "./output")
# print(process_line("/type;라거/에 /abv;3도 이상/이고 /flavor;과일/냄새인 /taste;시지 않은/ 거 있어?", tokenizer))

'''
인자값(argparse)을 쓰는 이유
- ipynb 에서는 별 필요 없음
- process_file(file_path) -> 실행
- 터미널 환경에서 실행할 때는 보통 python test.py --> 이럴때 filepath 를 어떻게 입력할까?
- python test.py -i input_dir -o output_dir
- python test.py --input input_dir --output output_dir
'''

# import argparse

# # 인자값을 받을 수 있는 인스턴스 생성
# # 인자값 : 터미널에서 파이썬 실행할 때 쓰는 일종의 input ex) 경로
# parser = argparse.ArgumentParser(description='사용법 테스트입니다.')

# # 입력받을 인자값 등록
# # --target: 이름 / required = True/False : 필수 여부
# parser.add_argument('--target', required=True, help='어느 것을 요구하냐')
# parser.add_argument('--env', required=False, default='dev', help='실행환경은 뭐냐')
# # or
# # parser.add_argument('-t', required=True, help='어느 것을 요구하냐')
# # parser.add_argument('-e', required=False, default='dev', help='실행환경은 뭐냐')

# # python test.py --target "안녕하세요" --env "반가워요"
# # python test.py -t "안녕하세요" -e "반가워요"

# # 입력받은 인자값을 args에 저장 (type: namespace)
# args = parser.parse_args()

# # 입력받은 인자값 출력 (앞서 썼던 이름 --target, --env --> args.target / args.env 에 따라 사용)
# print(args.target)
# print(args.env)