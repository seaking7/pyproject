from bs4 import BeautifulSoup
import pandas as pd


class EvGoKrSubsidyParser():

    trs = []

    def __init__(self, html_text):
        bsobj = BeautifulSoup(html_text, "html.parser")
        table = bsobj.find("table", {"class": "table01 fz15"})
        self.trs = table.find("tbody").find_all("tr")


    # tr을 넘기면 [{}, {}, {}]
    def parse_tr(self, tr):
        tds = tr.find_all("td")

        sido = tds[0].text
        region = tds[1].text

        replace_brackets = lambda x: x.replace("(", "").replace(")", "").split(" ")[1:]

        form = lambda a, b, c, d, e: {"sido": a, "region": b, "sep1": c, "sep2": d, "value": e}

        민간공고대수 = replace_brackets(tds[5].text)
        접수대수 = replace_brackets(tds[6].text)
        출고대수 = replace_brackets(tds[7].text)
        출고잔여대수 = replace_brackets(tds[8].text)

        l = [
            form(sido, region, "민간공고대수", "우선순위", int(민간공고대수[0])),
            form(sido, region, "민간공고대수", "법인과기관", int(민간공고대수[1])),
            form(sido, region, "민간공고대수", "택시", int(민간공고대수[2])),
            form(sido, region, "민간공고대수", "우선비대상", int(민간공고대수[3])),
            form(sido, region, "접수대수", "우선순위", int(접수대수[0])),
            form(sido, region, "접수대수", "법인과기관", int(접수대수[1])),
            form(sido, region, "접수대수", "택시", int(접수대수[2])),
            form(sido, region, "접수대수", "우선비대상", int(접수대수[3])),
            form(sido, region, "출고대수", "우선순위", int(출고대수[0])),
            form(sido, region, "출고대수", "법인과기관", int(출고대수[1])),
            form(sido, region, "출고대수", "택시", int(출고대수[2])),
            form(sido, region, "출고대수", "우선비대상", int(출고대수[3])),
            form(sido, region, "출고잔여대수", "우선순위", int(출고잔여대수[0])),
            form(sido, region, "출고잔여대수", "법인과기관", int(출고잔여대수[1])),
            form(sido, region, "출고잔여대수", "택시", int(출고잔여대수[2])),
            form(sido, region, "출고잔여대수", "우선비대상", int(출고잔여대수[3])),
        ]

        return l

    def parse(self):
        collected_list = []
        for tr in self.trs:
            row = self.parse_tr(tr)
            collected_list += row
        return collected_list

    def save_to_excel(self, excel_filename):
        df = pd.DataFrame(self.parse())
        print(df)
        df.to_excel(excel_filename)


if __name__ == '__main__':

    f = open("local_info.html", encoding="utf-8")
    page_string = f.read()

    ev_or_kr_parser = EvGoKrSubsidyParser(page_string)
    # collected_list = ev_or_kr_parser.parse()

    ev_or_kr_parser.save_to_excel("all_sido2.xlsx")




