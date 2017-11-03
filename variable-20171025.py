'''
message = "Hello world!"
print(message)
'''

message = "Hello Python Crash Course 'reader!'"
print(message)
message_split = message.split(" ")
for m in message_split:
    print(m)

name = "ada love lace"
print(name.title())
print(name.title().upper())
print(name.title().lower())
print(name.lstrip())

message = "Happy " + str(23) +"rd Birthday!"
print(message)

#import this

names = ["li","zhao","zhang","wang"]
names.insert(2,'dong')
print(names)
del names[1]
print(names)
