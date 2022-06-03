import requests
from bs4 import BeautifulSoup
import pandas as pd

req = requests.get("https://dailybeer.co.kr/board/index.php?board=menu_01&sca=2") # HTTP - GET REQUEST

html = req.text

soup_obj = BeautifulSoup(html, 'html.parser')

info_eng = soup_obj.select("p.info_ttl_eng")

info_ttl = soup_obj.select("p.info_ttl_kor")

beer_detail = soup_obj.select("p.text.beer_detail")

beer_Abv = soup_obj.select("ul.asi.fs_def")

#bg_image = soup_obj.select("")

#video_bg = soup_obj.select("")

beer_menu = [] # 빈 리스트를 전역변수로 생성
for eachLine in zip(info_eng, info_ttl, beer_Abv, beer_detail):
	beer_menu.append(
        [
            eachLine[0].text,eachLine[1].text, eachLine[2].text, eachLine[3].text 
            
        ]
) 
# for i in beer_menu:
#     print(i])

# print(beer_menu)

beer_names_eng = [] # 빈 리스트를 전역변수로 생성
beer_names_kor = [] 
beer_Abvs = []
beer_explanations = []


for eachLine in zip(info_eng, info_ttl, beer_Abv, beer_detail):
    beer_name_eng = eachLine[0].text
    beer_names_eng.append(beer_name_eng)
    beer_name_kor = eachLine[1].text
    beer_names_kor.append(beer_name_kor)
    beer_Abv = eachLine[2].text.replace("\n", '  ')
    beer_Abvs.append(beer_Abv)
    
    beer_explanation = eachLine[3].text.replace('\r\n', '')
    beer_explanation = beer_explanation.replace('\n', '')
    beer_explanations.append(beer_explanation)
    
beer_menu = pd.DataFrame({'eng_name' : beer_names_eng, 'kor_name' : beer_names_kor, 'Abv,ibu,srm' : beer_Abvs, 'info' :beer_explanations})
# print(beer_menu['Abv,ibu,srm'])

print(min(beer_menu['Abv,ibu,srm']))    
print(max(beer_menu['Abv,ibu,srm']))    
    