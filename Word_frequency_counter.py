# Here the code begins for the word frequency counter
count = 0

para = input('''Enter the paragraph to count the frequency of words: ''')
word = input('''Enter the word to count: ''')

words = para.lower().split()


if(word.lower() in words):
    count = words.count(word.lower())


print(f"The word '{word}' occurs {count} times in the paragraph.")