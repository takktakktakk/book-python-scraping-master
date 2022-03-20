# BeautifulSoupを利用してHTMLを解析 --- (※1)
from bs4 import BeautifulSoup

with open("ch2/eki-link.html", encoding="utf-8") as file:
    html = file.read()

bs = BeautifulSoup(html, "html.parser")

# テーブルを解析する --- (※2)
result = []

# <table>タグを得る --- (※3)
table = bs.select_one("table")

# <tr>タグを得る --- (※4)
tr_list = table.find_all("tr")
print(tr_list)

for tr in tr_list:
    # <td>あるいは<th>タグを得る --- (※5)
    result_row = []
    td_list = tr.find_all(["th","td"])
    for td in td_list:
        cell = td.get_text()
        result_row.append(cell)
    result.append(result_row)

# リストをCSVファイルとして出力 --- (※6)
for row in result:
    print(",".join(row))

