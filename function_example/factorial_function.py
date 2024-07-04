'''순환 함수 형태: iterative form of factorial'''
def factorial1(n):
  if n == 0:
    return 1
  else:
    result = 1
    for i in range(1,n+1):
      result = result*i
    return result

'''
재귀함수 형태: recursive form of factorial'''
def factorial2(n):
  if n==0:
    return 1
  elif n==1:
    return 1
  else:
    return n*factorial2(n-1)
  
"""
a = int(input("입력할 값을 쓰세요"))
f = factorial1(a)
print(f)
"""
a=0
list_input =[]

while True:
  in_1 = str(input())
  list_input.append(in_1)
  a=a+1
  if list_input[-1] =="!":
    break

if a == 2 and list_input[0].isdigit():
  print("="+str(factorial1(int(list_input[0]))))
else:
  print("error")