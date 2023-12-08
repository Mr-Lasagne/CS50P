# Create main function that takes input, applies convert function to input, then prints converted input
def main():
    text = input("Type something with a happy or sad face! ")
    textcon = convert(text)
    print(textcon)

# Create function that replaces ":)" and ":(" with corresponding emoji
def convert(n):
    return n.replace(":)", "🙂").replace(":(", "🙁")

main()
