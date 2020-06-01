def multi_line():
    output = []
    print("Please enter the text to be analyzed. Press Enter, then press ctrl-c to save it.")
    while True:
        try:
            output.append(input())
        except:
            break
    return output

def flatten(lst):
    output = []
    for i in lst:
        if type(i) != list:
            output.append(i)
        else:
            output += flatten(i)
    return output

def contains_letters(word):
    for i in word:
        if i.isalpha():
            return True
    return False

text = multi_line()
text = flatten(text)
string = ' '.join(text)
words = string.split()
print(len(words))
