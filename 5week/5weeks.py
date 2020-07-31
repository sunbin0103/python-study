import random  # random 모듈 가져옴

for i in range(10):
         print(i)

 a = range(10,0,-2)
 print(list(a))

 n = int(input("반복횟수: "))
 for j in range(n):
     print(j+1)

a = [10,20,30,40,50]
for i in a:
    print(i)

fruits = ('사과','귤','포도')
for fruit in fruits:
    print(fruit)

for letter in 'Python':
    print(letter)

i = 10
while i>0:
    print(i)
    i -= 1

n = int(input("반복횟수: "))
i = 1
while i<=n:
    print(i)
    i += 1

random.randint(1,6) # 정수난수

i = 0
while i != 3: # i가 3이 아닐 때 반복
    i = random.randint(1,6)
    print(i)

dice = ['학교','사목리','사목항','마두산','공소','순교성지','말총곶']
c = ''
while c != '사목항':
    c = random.choice(dice)
    print(c)

while True:
    print("Hi")