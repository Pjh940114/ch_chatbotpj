import requests
from bs4 import BeautifulSoup as bs
from parse import *

def filesave(url):
    try:
        urlsplit = url.split('/')[-1]
        urlsplit = urlsplit.split('.')[0]
        name = 'C:/pythonstudy/choongang/ch_project_2/images/' + urlsplit
        bn = requests.get(url).content
        if bn[0:3] != b'\xff\xd8\xff' or 'jpg' not in urlsplit:
            # print('this file is not JPEG file format')
            # return 0
            name += '.jpg'
        # else:
        #     if 'jpg' not in urlsplit:
        #         name += '.jpg'
        for idx in name:
            f = open(name,'wb')
            f.write(bn)
            f.close()
            print(f'[!] {name} saved')
            return name
    except Exception as e:
        print(e)
        return 0

def main(url):
    s = bs(requests.get(url).text, 'html.parser')
    images = s.find_all('div', {'class':'cutter'})
    for idx, image in enumerate(images):
        result = parse("background-image:url('{}')", image['style'])[0]
        filesave(result)

if __name__ == "__main__":
    main('https://dailybeer.co.kr/board/index.php?board=menu_01&sca=2')