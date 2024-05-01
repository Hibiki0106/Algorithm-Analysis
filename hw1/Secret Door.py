# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 16:36:20 2022

@author: kagat
"""


def ouo ( str, now, last ):
    
    temp = "\0"
    if now >= last : return str 
    
    #print(str[now])
    
    for i in range(len(str)) :
        if str[now][len(str[now])-1] == str[i][0] : 
            #if str[now][len(str[now])-1] != str[now+1][0] or str[i][len(str[i])-1] != str[i+1][0] :
            temp = str[now+1]
            str[now+1] = str[i]
            str[i] = temp
            #print(str)
    
    point = 0
    for i in range(len(str)-1):
        if str[i][len(str[i])-1] == str[i+1][0] : point+=1
    
    if point == len(str) - 1 : return str
    
    ouo ( str, now+1, last )
    #return str

point = 0
str = list(input().split())
#print(str)
    
for i in range(len(str)):
    ouo( str, 0, len(str)-1 )
    
    for i in range(len(str)-1):  # 檢查好了沒
        if str[i][len(str[i])-1] == str[i+1][0] : point+=1
    if point == len(str) - 1 : break

if str[0][0] == str[len(str)-1][len(str[len(str)-1])-1] : #怕沒找到
    temp = str[0]
    str.pop(0)
    str.append(temp) 
    
point = 0

for i in range(len(str)-1): 
    if str[i][len(str[i])-1] == str[i+1][0] : point+=1

#print(str)

    
if point == len(str) - 1 :
   print("can open")
   print(str)

if point != len(str) - 1 :    
   print(point)
   print(str)
   print("can't open")
