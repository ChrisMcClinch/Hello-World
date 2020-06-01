def multi_line():
    output = []
    print("Please enter the text to be analyzed. Then press ctrl-c to save it.")
    while True:
        try:
            output.append(input())
        except:
            break
    return output

vowels = {'a':0, 'e':0, 'i':0, 'o':0, 'u':0}

text = multi_line()
for paragraph in text:
    for letter in paragraph:
        if letter.lower() in vowels:
            vowels[letter.lower()] += 1
print(' ')
print(vowels)
