text = input("Input: ")
# Python is fun. Python is easy to learn. Fun is important.
clean = ""
for ch in text:
    if ch.isalpha() or ch.isspace():
        clean += ch.lower()
    else:
        clean += " "

words = clean.split()

if len(words) == 0:
    print("No words found in the input")
else:
    print("Total words:", len(words))

    freq = {}
    for w in words:
        if w in freq:
            freq[w] += 1
        else:
            freq[w] = 1

    max_word = ""
    max_count = 0
    for w in freq:
        if freq[w] > max_count:
            max_count = freq[w]
            max_word = w

    print("Most frequent word:", '"' + max_word + '"')
    print("Frequency:", max_count)
    print("Unique words:", len(freq))
