a = int(input())
for i in range (a):
    b = int(input())
    if b < 10 or b == 10:
      print("Go to work!")
    elif b > 10 and b <= 25:
      print("You are weak")
    elif b > 25 and b <= 45:
      print("Okay, fine") 
    else:
      print("Burn! Burn! Burn Young!")
    