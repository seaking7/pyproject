import requests
from crawling.libs.evparser import EvGoKrSubsidyParser

url = "https://ev.or.kr/nportal/buySupprt/initSubsidyPaymentCheckAction.do"
data = requests.get(url)

ev_parser = EvGoKrSubsidyParser(data.text)
ev_parser.save_to_excel("crawl_subsidy_all.xlsx")
# ev_parser.parse()
