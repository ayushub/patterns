for i in range(9):
     num=i-1
     for j in range(2*i-1):
         if(j>i-1):
             num=9 if num==0 else num-1
             print(num)
         if(j<i-1):
             print(num)
             num=0 if num==9 else num+1
         if(j==i-1):
             print(num)
