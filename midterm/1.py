def CheckLeap(Year):  
  if((Year % 400 == 0) or  
     (Year % 100 != 0) and  
     (Year % 4 == 0)):   
    print("YES");  
  else:  
    print ("NO")  
Year = int(input())  
CheckLeap(Year)
