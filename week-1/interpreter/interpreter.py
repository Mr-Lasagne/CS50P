def main():
    expression = input("Expression: ").strip()
    x, y, z = expression.split(" ")
    
    numx = float(x)
    numz = float(z)
    
    print(result(numx, y, numz))

def result(n1, o, n2):
    if o == "+":
        return float(n1 + n2)
    elif o == "-":
        return float(n1 - n2)
    elif o == "*":
        return float(n1 * n2)
    elif o == "/":
        return float(n1 / n2)

main()
