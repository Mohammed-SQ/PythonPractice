def classify(age):
    if age >= 60:
        return "Senior"
    else:
        return "not a Senior"
# ---------------- MAIN PROGRAM ----------------
data = input("Enter Name:Age years (entries separated by ';'): ")

# Split entries by ; 
entries = data.split(";")

people = {}   # dictionary name → age

for item in entries:
    item = item.strip()         # remove spaces
    if item == "":
        continue

    # Example item:  "Ayesha: 30 years"
    name, age_text = item.split(":")
    name = name.strip()

    # remove "years" and spaces
    age_text = age_text.replace("years", "").strip()

    age = int(age_text)

    people[name] = age

# ---- Classification ----
for name in people:
    result = classify(people[name])
    print(f"{name} is {result}.")

print()
# ---- Eldest and Youngest ----
# find max age
eldest_name = ""
eldest_age = -1

youngest_name = ""
youngest_age = 1000

for name in people:
    age = people[name]
    if age > eldest_age:
        eldest_age = age
        eldest_name = name
    if age < youngest_age:
        youngest_age = age
        youngest_name = name

print(f"The eldest person is {eldest_name}, aged {eldest_age} years.")
print(f"The youngest person is {youngest_name}, aged {youngest_age} years.")
