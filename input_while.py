'''
message = input("Tell me something, and I will repeat it back to you: ")
print(message)

current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1
'''
unconfimed_users = ["alice","brian","candance"]
confimed_users = []

while unconfimed_users:
    current_user = unconfimed_users.pop()
    print("Verifying user: " + current_user.title())
    confimed_users.append(current_user)
print("\nThe following users have been confirmed: ")
for confimed_user in confimed_users:
    print(confimed_user.title())