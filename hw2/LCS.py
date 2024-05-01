# 演算法分析機測
# 學號 : 10827111/ 10827209 / 10827215
# 姓名 : 袁本誠 / 何承泓 / 李政叡
# 中原大學資訊工程系

import numpy as np


def LCSLength(m, n, x, y, a, b):
    for i in range(1,m+1):
        for j in range(1,n+1):
            if x[i-1]==y[j-1]:
                a[i][j] = a[i-1][j-1]+1
                b[i][j] = 1
            elif a[i-1][j] >= a[i][j-1]:
                a[i][j] = a[i-1][j]
                b[i][j] = 2
            else:
                a[i][j] = a[i][j-1]
                b[i][j] = 3

def LCS(i, j, x, b):
    
    if i==0 or j==0:
        return 
    if b[i][j]==1:
        LCS(i-1, j-1, x, b)
        #lcs = lcs + x[i-1]
        #print(lcs)
        print(x[i-1],end='')
    elif b[i][j]==2:
        LCS(i-1, j, x, b)
    else:
        LCS(i, j-1, x, b)

data = []
num1, num2=map(int,input().split())
#if int(num1) <= 1 or int(num2) >= 100 :
    #print("please input size again")
    
while  int(num1) != 0 and int(num2) != 0 :
  while ( int(num1) <= 1 and int(num1) >= 100 ) or ( int(num2) <= 1 and int(num2) >= 100 ) :
    print("please input size again")
    num1, num2=map(int,input().split())
    
  if int(num1) == 0 and int(num2) == 0:
      break
  
  data.append(num1)
  data.append(num2)
#while  num1 != 0 and num2 != 0  :
  x = input()
  x = x.replace(' ', '')
  while len(x) != int(num1) :
    x = input()
    x = x.replace(' ', '')
      
  y = input()
  y = y.replace(' ', '')
  while len(y) != int(num2) :
    y = input()
    y = y.replace(' ', '')
  #x = "A B C B D A B"
  #y = "B D C A B A "
  
  
  data.append(x)
  data.append(y)
  num1, num2=map(int,input().split())
  
#size = len(data)
run = 0
case = 1
while run+1 <= len(data) :
  num1 = data[run]
  num2 = data[run+1]
  x = data[run+2]
  y = data[run+3]
  #print(x)
  #print(y)
  a = np.zeros((num1+1)*(num2+1)).reshape((num1+1), (num2+1))    # 生成一個m*n且全是0的矩陣
  b = np.zeros((num1+1)*(num2+1)).reshape((num1+1), (num2+1))    # 再來一個m*n且全是0的矩陣

  LCSLength(num1, num2, x, y, a, b)
  print( "Case#", end="" )
  print( case )
  print( "Length of LCS = ", end="" )
  print(int(a[num1][num2]))
  print( "LCS = ", end="" )
  LCS(num1, num2, x, b)
  print()
  print()
  case = case + 1
  run = run + 4

#print(data)