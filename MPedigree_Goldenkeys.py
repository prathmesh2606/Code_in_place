import random
N_LABELS = 1000
def main():
    for i in range(N_LABELS):
        random_part = pad(random.randint(0,99999),5)
        incremental_part = pad(i,4)
        print(random_part+incremental_part)

def pad(num,no_of_digit):
    num_string = str(num)
    zero = "0"
    while len(num_string) < no_of_digit:
        num_string = zero + num_string
    return num_string

if __name__ == "__main__":
    main()

