import sys

def reverse(phrase):
    return phrase[::-1]

if __name__ == "__main__":
    try:
        for i in reverse(sys.argv[1:]):
            print(reverse(i),end=' ')
    except:
        phrase = input("What phrase should I reverse? ")
        print(reverse(phrase))
