# 演算法分析機測
# 學號 : 10827111/ 10827209 / 10827215
# 姓名 : 袁本誠 / 何承泓 / 李政叡
# 中原大學資訊工程系

print("輸入背包容量 : ", end = "")
maxW = int(input()) # 背包容量
while maxW < 0 :
    print("請輸入大於0的數 : ")
    maxW = int(input())
    
    
print("輸入物品數 : ", end = "")
N = int(input()) # 物品数
while N < 0 :
    print("請輸入大於0的數 : ")
    N = int(input())



weight = [0] * (N + 1)  # 重量 1 ~ N
value = [0] * (N + 1)  # 价值 1 ~ N
print("輸入重量 价值 : ", end = "")
for i in range(1, N + 1):
    weight[i], value[i] = map(int, input().split())
    while weight[i] < 0 or value[i] < 0 :
        print("請輸入大於0的數 : ")
        weight[i], value[i] = map(int, input().split())

#print(weight)
f = [[0 for i in range(maxW+1)] for i in range(N+1)]  # 初始化全0
#f[i][j], 代價表前i个物品，存入容量为為j的背包里的最大值
we = maxW

for i in range(1, N + 1):  # 4
    for j in range(maxW + 1): # 50
        f[i][j] = f[i - 1][j] # 2 30 = 1 30    4 50 = 3 50
        #print(j)
        if j >= weight[i]:
            f[i][j] = max(f[i][j], f[i - 1][j - weight[i]] + value[i]) # max( 2 30,  1 30-20 (60+120) )
            
            #temp = j
            #if f[i][j] != f[i][temp-1] :
                #print(i)
     
                

            
totalValue = int(f[N][maxW])             
#print(f)


ans = list()
value.pop(0)
weight.pop(0)

for i in range(N, 0, -1):
    #print(i)
    if totalValue <= 0:
        break
    if totalValue == f[i - 1][we]:
        continue
    else:
        ans.append(i)
        totalValue = totalValue - value[i - 1]
        we = we - weight[i - 1]

ans.sort( reverse = False )
#print(ans)

print("Total Value = ",f[N][maxW])
print("Item = ", end="")
for i in range(0,len(ans)):
    if i+1 < len(ans) :
      print(ans[i], end=",")
    else :
      print(ans[i], end="")