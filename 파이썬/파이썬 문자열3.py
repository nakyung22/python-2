ticker = "btc_krw"
up = ticker.upper()
print(up)

ticker = "BTC_KRW"
low = ticker.lower()
print(low)

word = 'hello'
word = word.capitalize()
print(word)

file_name = "보고서.xlsx"
print(file_name.endswith("xlsx"))

file_name = "보고서.xlsx"
print(file_name.endswith(("xlsx", "xls")))

file_name = "2020_보고서.xlsx"
print(file_name.startswith("2020"))

a = "hello world"
print(a.split())

ticker = "btc_krw"
print(ticker.split("_"))

date = "2020-05-01"
print(date.split("-"))

data = "039490     "
print(data.rstrip(" "))