from calculator_logo import logo

def calculate(n1, sym, n2):
    if sym == '+':
        return n1 + n2
    elif sym == "-":
        return n1-n2
    elif sym == '*':
        return n1*n2
    elif sym == '/':
        return n1/n2
    else:
        return "NaN"

print(logo)

to_cont = True
to_cont_op = True
result = 0
count = 1
while to_cont:
    if not to_cont_op or count==1:
        n1 = float(input("What's the first number?: "))
        sym = input("+\n-\n*\n/\nPick an operation: ")
        n2 = float(input("What's the next number?: "))
        result = calculate(n1, sym, n2)
        print(f"{n1} {sym} {n2} = {result}")
    else:
        sym = input("+\n-\n*\n/\nPick an operation: ")
        n2 = float(input("What's the next number?: "))
        result_prev = result
        result = calculate(result_prev, sym, n2)
        print(f"{result_prev} {sym} {n2} = {result}")

    count += 1

    get_to_cont = input(f"Type 'y' to continue calculating with {result}\nType 'n' to start a new calculator\nType 'exit' to exit the program\n")
    if "n" in get_to_cont:
        result = 0
        to_cont_op = False
    elif get_to_cont == "exit":
        to_cont = False
    elif "y" in get_to_cont:
        to_cont_op = True




