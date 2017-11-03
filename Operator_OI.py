f = open("data/test.txt","r")
g = f.read()
print(g)
f.close()

f_1 = open("data/test_write_1.txt","w")
f_1.write("12345678"+"\n")
f_1.write("I am Lizhaofu")
f_1.close()

weather_data = []
weather_data1 = []
f_2 = open("data/dq_unisex_names.csv","r")
data = f_2.read()
rows = data.split("\n")
for row in rows:
    weather_data1.append(row)
    split_row = row.split(",")
    #print(type(split_row))
    weather_data.append(split_row)
print(weather_data)
print(weather_data1)
