import sys

def pl(word):
    initcap = False
    if word[0].isupper():
        initcap = True
    vowels = 'aeiouy'
    if word[0].lower() in vowels and word[0].lower() != 'y':
        return (word + 'way')
    if word[0].lower() == 'y':
        word = word[1:] + word[0]
    while word[0].lower() not in vowels:
        word = word[1:] + word[0]
    if initcap:
        newword = word[0].upper()
        for i in word[1:]:
            newword += i.lower()
        word = newword
    return (word + 'ay')

def piglatin(phrase):
    words = phrase.split(' ')
    output = []
    for word in words:
        output.append(pl(word))
    return ' '.join(output)

if __name__ == "__main__":
    try:
        print(piglatin(' '.join(sys.argv[1:])))
    except:
        phrase = input("Please enter a phrase to translate: ")
        print(piglatin(phrase))
