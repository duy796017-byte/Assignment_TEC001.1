numbers = []
while True:
    user_input = input("Nhập số (Enter để thoát): ")
    if user_input == "":
        break
    numbers.append(float(user_input))  
numbers.sort(reverse=True)
print("5 số lớn nhất:")
print(numbers[:5])