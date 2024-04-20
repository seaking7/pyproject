from bs4 import BeautifulSoup

f = open("local_info.html", encoding="utf-8")
page_string  = f.read()
bsobj = BeautifulSoup(page_string, "html.parser")
table = bsobj.find("table", {"class":"table01 fz15"})
trs = table.find("tbody").find_all("tr")
tr = trs[0]
#
# for tr in trs:
#     print(tr)
#     print("---------")

tds = tr.find_all("td")

# for td_index in tds:
#     print(td_index.text)

sido = tds[0].text
region = tds[1].text

민간공고대수 = tds[5].text
접수대수 = tds[6].text
출고대수 = tds[7].text
출고잔여대수 = tds[8].text

print(민간공고대수)
print(접수대수)
print(출고대수)
print(출고잔여대수)
