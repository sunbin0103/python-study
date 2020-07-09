#a = input()
#print(a)

#b = input("정수를 입력하세요: ")
#print(b)

x, y = 10, 20
print(x,y)

i, j = input("정수를 입력하세요: ").split()
p = int(i)
q = int(j)
print(i+j)
print(p+q)

p, q = input().split("*")
print(p)
print(q)

c, d = map(int, input("정수를 입력하세요: ").split())
print(c)
print(d)
print(c+d)

e, f = map(float, input("실수를 입력하세요: ").split())
print(e)
print(f)
print(e+f)

a = [1,1,1,2,2,3,3,3,4,4,5]
print(set(a))

#정수 세 개를 입력 받고 그 합계가 출력되는 코드를 작성하라.
num1, num2, num3 = map(int, input("정수를 입력하세요: ").split())
print(num1+num2+num3)

n1 = int(input("첫번째 정수를~~:"))
n2 = int(input("두번째 정수를~~:"))
n3 = int(input("세번째 정수를~~:"))
print(n1+n2+n3)
