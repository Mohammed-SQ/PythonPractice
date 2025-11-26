def update_words(words):
    updated = []
    for w in words:
        if w[0].lower() == w[-1].lower():
            updated.append("xxxxx")
        elif len(w) >= 4:
            updated.append(w)
    return updated

sentence = input("Enter a sentence: ")
all_words = sentence.split()
same_letter = []

for w in all_words:
    if w[0].lower() == w[-1].lower():
        same_letter.append(w.lower())

print("Words starting and ending with the same letter:", same_letter)
updated_list = update_words(all_words)
print("Updated word list:", updated_list)
print("Total number of words in the sentence:", len(all_words))