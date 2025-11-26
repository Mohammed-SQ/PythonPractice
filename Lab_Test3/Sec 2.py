def classify(age):
    if age >= 60:
        return "Senior"
    else:
        return "not a Senior"

data = input("Enter Name:Age years (entries separated by ';'): ")
parts = data.split(";") # Ayesha: 30 years;John:45 years;Mary:67 years;Alice:30 years;Robert:62 years
people = {}

for item in parts:
    item = item.strip()
    if item == "":
        continue
    name, age_text = item.split(":")
    name = name.strip()
    age_text = age_text.replace("years", "").strip()
    age = int(age_text)
    people[name] = age

for name in people:
    print(name, "is", classify(people[name]) + ".")

print()

eldest_name = ""
eldest_age = -1
youngest_name = ""
youngest_age = 9999

for name in people:
    age = people[name]
    if age > eldest_age:
        eldest_age = age
        eldest_name = name
    if age < youngest_age:
        youngest_age = age
        youngest_name = name

print("The eldest person is", eldest_name + ", aged", str(eldest_age) + " years.")
print("The youngest person is", youngest_name + ", aged", str(youngest_age) + " years.")
