# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def getCrossMax( nums, startIndex, middleIndex, endIndex):
        crossLeft = 0
        crossRight = 0
        global arryCROSS
        tmpValue = 0
        leftI = 0
        leftR = 0
        maxvalue = 0
        arryCROSS = []
       
        for i in range(middleIndex-1, startIndex-1, -1):# 從中間向左走最大子集合 -1是從又到左
            tmpValue += nums[i] 
            crossLeft = max(tmpValue, crossLeft)
            # if crossLeft > tmpValue : leftL = i
            if crossLeft == tmpValue : leftI = i
        tmpValue = 0
       
        for i in range(middleIndex+1, endIndex+1): # 從中間向右走最大子集合
            tmpValue += nums[i]
            crossRight = max(tmpValue, crossRight)
            # if crossRight > tmpValue : leftR = i
            if crossRight == tmpValue : leftR = i
        # 將左中右的值都相加後，為中間子集合最大值
        #if crossLeft == 0 and crossRight == 0 : leftI = leftR = middleIndex
        if crossLeft == 0 : leftI = middleIndex
        if crossRight == 0 : leftR = middleIndex
        maxvalue = crossLeft + nums[middleIndex] + crossRight
        arryCROSS.append(maxvalue)
        arryCROSS.append(leftI+1)
        arryCROSS.append(leftR+1)
        return maxvalue
    # 取得最大值
def getMax( nums, startIndex, endIndex):
        # 若開始位置超過結束位置，代表剩一個值，回傳當下的值
        if startIndex >= endIndex:
            return nums[startIndex]
        # 找到中間位置
        middleIndex = int((startIndex + endIndex)/2) 
        
        leftMax = getMax(nums, startIndex, middleIndex-1) # 取得左邊子集合最大值
        
        rightMax = getMax(nums, middleIndex+1, endIndex) # 取得右邊子集合最大值
        
        crossMax = getCrossMax(nums, startIndex, middleIndex, endIndex)# 取得中間子集合最大值
        # 找到目前範圍的最大值
        return max(leftMax, rightMax, crossMax)
        
def maxSubArray( nums: list[int]) -> int:
        return getMax(nums, 0, len(nums)-1)
    
A = []  
size = 0
print("input size:")
size = input()

while int(size) != 0 :
    A = list(input().split())

    for i in range(int(size)):
        A[i] = int(A[i])

    B = A

    SUM = maxSubArray(A)
    find = False
    for i in range(0, int(len(arryCROSS)), +3 ):
        if arryCROSS[i] == SUM :
            find = True
            print("LOW : ", arryCROSS[i+1], "High: ", arryCROSS[i+2], "SUM : ", SUM )
            
    if find == False :
        for i in range(int(size)) :
            if B[i] == SUM : print("LOW : ", i+1, "High: ", i+1, "SUM : ", SUM )
                    
    print("input size:")
    size = input()










    