import random 
target=random.randint(1, 10)
while True:
    G= int(input("Enter your answer:(1-10)"))
    if G>target:
        print("Too High")
    if G<target:
        print("Too Low")
    if G==target:
        print ("correct")
        break