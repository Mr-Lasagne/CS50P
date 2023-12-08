def main():
    text = input("Type something with a happy or sad face! ")
    textcon = convert(text)
    print(textcon)

def convert(n):
    return n.replace(":)", "🙂").replace(":(", "🙁")

main()
