import requests

url = "https://ev.or.kr/nportal/buySupprt/initSubsidyPaymentCheckAction.do"
data = requests.get(url)
print(data.text)

f = open("local_info.html", "w+", encoding="utf-8")
f.write(data.text)
f.close()
