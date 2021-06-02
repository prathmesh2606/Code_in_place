def read_phonebooks_numbers():
    d = {}
    while True:
        name = input("Enter the name: ")
        if name == "":
            break
        number = input("Enter the mobile number: ")
        d[name] = number
    return d

def print_phonebook(d):
    for k,v in d.items():
        print(k,"-->",v)

def lookup_phonebook(d):
    while True:
        name = input("Enter name to lookup: ")
        if name == "":
            break
        if name not in d:
            print("Enter name is not in phonebook.")
        else:
            print(d[name])

def main():
    phonebook = read_phonebooks_numbers()
    print_phonebook(phonebook)
    lookup_phonebook(phonebook)

if __name__ == "__main__":
    main()