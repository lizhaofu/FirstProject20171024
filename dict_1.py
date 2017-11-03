alien_0 = {"color":"green","point":5}
print(alien_0)
print(alien_0["color"])
print(alien_0["point"])

user_0 = {
    'username':"efermi",
    "first":"enrico",
    "last":"fermi",
}
for key, value in user_0.items():
    print("\nkey: " + key)
    print("\nvalue: " + value)

aliens = []
for alien_number in range(30):
    new_alien = {"color":"green","points":5,"speed":"slow"}
    aliens.append(new_alien)
for alien in aliens[:5]:
    print(alien)
print("***********")
print(len(aliens))