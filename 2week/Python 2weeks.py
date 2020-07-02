year=2020
if (year%4==0 and year%100!=0) or (year%400==0):
    print(year,'은 윤년이다.')
else:
    print(year,'은 윤년이 아니다.')
