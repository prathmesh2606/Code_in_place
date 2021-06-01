def main():
    inp = input("Enter a string: ")
    if is_palindrome(inp):
        print("Given string is Palindrom!")
        print("This palindrom contains {} characters.".format(str(len(inp))))
    else:
        print(inp)
        print("This is not a palindrom.")

def is_palindrome(str):
    normalize_str = normalize(str)
    reverse_str = reverse(normalize_str)
    return normalize_str == reverse_str

def normalize(str):
    normalize = ''
    for ch in str:
        if ch.isalpha():
            normalize += ch.lower()
    return normalize

def reverse(str):
    reverse = ''
    for ch in str:
        reverse = ch + reverse
    return reverse

if __name__ == '__main__':
    main()