import sys

def is_palindrome(string):
    pureletters = ''
    for i in string:
        if i.isalpha():
            pureletters += i.lower()
    if len(pureletters) < 2:
        return True
    if pureletters[0] != pureletters[-1]:
        return False
    return is_palindrome(pureletters[1:-1])

if __name__ == "__main__":
    string = sys.argv[1:]
    print(string)
    if len(string) > 0:
        print(is_palindrome(sys.argv[1:]))
    else:
        string = input("What string would you like me to check? ")
        print(is_palindrome(string))
