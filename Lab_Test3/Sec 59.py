usernames = ["alex99", "maria01", "johnny", "sara88"]

print("Existing usernames:", usernames)

new_user = input("Enter a new username: ")

if new_user.lower() in usernames:
    print("Username already exists!")
    base = new_user
    number = 1
    generated = base + str(number)
    while generated.lower() in usernames:
        number += 1
        generated = base + str(number)
    print("New username generated:", generated)
    usernames.append(generated)
else:
    usernames.append(new_user)

print("Updated list:", usernames)