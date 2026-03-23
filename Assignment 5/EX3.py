cities = []
for i in range(5):
    name = input(f"Nhập tên thành phố {i+1}: ")
    cities.append(name)
print("Danh sách thành phố:")
for city in cities:
    print(city)