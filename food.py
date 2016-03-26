import re
import getopt
import sys
import requests
from bs4 import BeautifulSoup

print ("오늘의 급식:\n")

url = requests.get("http://yongma.ms.kr/tablemenu/menu.do")
soup = BeautifulSoup(url.text, "lxml")
food = soup.find("tr", { "valign" : "middle" })

pattern = '	'
text = food.text

match = re.search(pattern, text)
startIndex = match.start()
endIndex = match.end()

result = '{}'.format(
	text[startIndex:endIndex+40]
)

print(result.strip())


pattern = '열량:'
text = food.text

match = re.search(pattern, text)
startIndex = match.start()
endIndex = match.end()

result1 = '{}'.format(
	text[startIndex:endIndex+10]
)

print(result1)
