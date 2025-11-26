paragraph = input("Input: ")

# Remove punctuation that may stick to words
clean = ""
for ch in paragraph:
    if ch.isalpha() or ch.isspace():
        clean += ch.lower()
    else:
        clean += " "

# Split into words
words = clean.split()

# Case: empty or no words
if len(words) == 0:
    print("No words found in the input")
else:
    # 1. Total words
    total = len(words)
    print("Total words:", total)

    # 2 & 3. Most frequent word and its frequency
    freq = {}
    for w in words:
        if w in freq:
            freq[w] += 1
        else:
            freq[w] = 1

    # find max frequency
    max_count = 0
    most_word = ""

    for w in freq:
        if freq[w] > max_count:
            max_count = freq[w]
            most_word = w

    print("Most frequent word:", '"' + most_word + '"')
    print("Frequency:", max_count)

    # 4. Unique word count (case-insensitive)
    unique_count = len(freq)
    print("Unique words:", unique_count)
