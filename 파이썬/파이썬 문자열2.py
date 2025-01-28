a = "3"
b = "4"
print(a + b)
# 예상 결과: 34
# 문자열은 숫자열이 아니기때문에 결과가 34로 출력된다

print("Hi" * 3)
# 예상 결과: HiHiHi

print("-" * 80)

t1 = 'python'
t2 = 'java'
t3 = t1 + ' ' + t2 + ' '
print(t3 * 4)

name1 = "김민수"
age1 = 10
name2 = "이철희"
age2 = 13
print(f"이름: {name1} 나이: {age1}")
print(f"이름: {name2} 나이: {age2}")

상장주식수 = "5,965,782,550"
컴마제거 = 상장주식수.replace(",", "")
타입변환 = int(컴마제거)
print(타입변환, type(타입변환))

분기 = "2020/03(E) (IFRS연결)"
print( 분기[:7])

data = "   삼성전자    "
data1 = data.strip()
print(data1)