def main():
    text = "This is Sahajayoga Meditation"
    d = {}
    for ch in text.lower():
        if ch.isalpha():
            d[ch] = d.get(ch,0) + 1
    print(d)

if __name__ == "__main__":
    main()