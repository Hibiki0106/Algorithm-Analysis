# 演算法分析機測
# 學號 : 10827111/ 10827209 / 10827215
# 姓名 : 袁本誠 / 何承泓 / 李政叡
# 中原大學資訊工程系

def dij(start, graph):
    n = len(graph)
    
    length = [99999 for _ in range(n)]
    length[start] = 0
    dotParent = [-1 for _ in range(n)]
    visited = [False for _ in range(n)] 
    t = []  
    while len(t) < n:
        node_min = None
        
        length_min = 99999
        
        for i in range(n):
            if not visited[i] and length[i] < length_min:
                length_min = length[i]
                node_min = i
        t.append(node_min)
        visited[node_min] = True

        for j in graph[node_min]:
            if not visited[j[0]] and length_min + j[1] < length[j[0]]:
                
                length[j[0]] = length_min + j[1]
                dotParent[j[0]] = node_min
    return length, dotParent




if __name__ == '__main__':
    print("請輸入節點及邊的個數")
    num_list = [int(i) for i in input().split()] 
     # 第一個是字母有幾個 第二個是幾筆資料
    while num_list[0] < 0 or num_list[1] < 0 :
        print("請重新輸入節點及邊的個數")
        num_list.clear()
        num_list = [int(i) for i in input().split()] 
    
        
    dot = input()
    dot = dot.replace(" ", "")
    i = 0
    #print(dot)
    while i < num_list[0] :
        if dot[i] >= 'A' and dot[i] <= 'Z' :
           print("請重新輸入小寫字母")
           dot = ""
           dot = input()
           dot = dot.replace(" ", "")
           i = 0
        i += 1
             

    data = []
      
    for w in range(0, num_list[1]):
        
      #linecount = input()
      dot1, dot2, count = input().split()
      count = int(count)
      
      while count < 0 :
          print("請重新輸入")
          dot1, dot2, count = input().split()
          count = int(count)
          
      row = []
       # print(count)
      for i in range(0, num_list[0]) :
          if dot1 == dot[i] : row.append(i) 

      for i in range(0, num_list[0]) :
          if dot2 == dot[i] : row.append(i) 
          
      row.append(int(count)) 
        #print(row)
      data.append(row)
        
      
        
    n = num_list[0]  
    graph = [[] for _ in range(n)]
    for i in data:
        graph[i[0]].append([i[1], i[2]])
          
          
          
    costs, parents = dij(0, graph)
    c, d = map(int,input().split())
    while c != 0 or d != 0 :
         print('輸入0 0')
         c, d = map(int,input().split())
         

    print('Graph#1')
     

    for i in range(1, num_list[0]):
       # print()
      print('From',dot[0],'to',dot[i], '=',costs[i],)
        
        
    print(dot[0],'source node')
    
    #print(parents)
    for p in range(1, num_list[0]):
        print(dot[p],'’s',sep='',end='')
        print(' parent node = ',end='') 
        #for i in range(0, num_list[0]) :
            #if parents[p] == i :
                #print(dot[i])
                #break;
        if parents[p] == 0 : print(dot[0])
        elif parents[p] == 1 : print(dot[1])
        elif parents[p] == 2 : print(dot[2])
        elif parents[p] == 3 : print(dot[3])
        elif parents[p] == 4 : print(dot[4])
       # print(parents)
        
        
        
  