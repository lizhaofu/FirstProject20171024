months = []
print(months)
months.append(1)
months.append("Jan")
print(months)

countries = []
temperatures = []
countries.append("China")
countries.append("India")
countries.append("USA")


temperatures.append(30.5)
temperatures.append(25.0)
temperatures.append(15.1)

print(countries)
print(temperatures)
print(countries[0])
print(temperatures[1])

int_mounths = [1,2,3,4,5,6,7,8,9,10,11,12]
print(len(int_mounths))

index = len(int_mounths)-5
last_value = int_mounths[index]
print(last_value)
print(int_mounths[-2])
print(int_mounths[3:7])
print(int_mounths[:5])
for str in int_mounths:
    print(str)

i = 0
while i < 3:
    i += 1
    print(i)
print(range(10))

for l in range(10):
    print(l)

animals = ["cat","dog","dabbit"]
if "cat" in animals:
    print("cat found")

scores = {}
print(type(scores))
scores["Jin"] = 80
scores["Sue"] = 85
scores["Ann"] = 75
print(scores.keys())
print(scores)
print(scores["Jin"])
#print(scores.get())

pantry = ["apple","orange","grape","apple","orange"
    ,"apple","tomato","potato","grape"]
pantry_counts = {}

for item in pantry:
    if item in pantry_counts:
        pantry_counts[item] = pantry_counts[item] + 1
    else:
        pantry_counts[item] = 1
print(pantry_counts)





