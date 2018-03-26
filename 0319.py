import requests
import json
from bs4 import BeautifulSoup

# 下載 Yahoo 首頁內容
r = requests.get('http://www.books.com.tw/web/sys_bkmtop/books/')


# 開啟檔案
fp = open("bookstest.txt", "a")
# 確認是否下載成功
if r.status_code == requests.codes.ok:
  # 以 BeautifulSoup 解析 HTML 程式碼
  soup = BeautifulSoup(r.text, 'html.parser')

  # 以 CSS 的 class 抓出各類頭條新聞
  stories = soup.select('div.type02_bd-a > h4')
  #stories = soup.find_all('div.type02_bd-a>h4')
  for s in stories:
    # 新聞標題
    print("書名：" + s.text)
    # 寫入每本書名到檔案
    fp.write(s.text + '\n')

# 關閉檔案
fp.close()

 

 


 

