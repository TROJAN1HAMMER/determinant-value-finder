print("Hello!")
print("Welcome to determinant .py calculator")

def main():
    print("! a b c !")
    print("! d e f !")
    print("! g h i !")

    a = int(input("What is the value of a: "))
    b = int(input("What is the value of b: "))
    c = int(input("What is the value of c: "))
    d = int(input("What is the value of d: "))
    e = int(input("What is the value of e: "))
    f = int(input("What is the value of f: "))
    g = int(input("What is the value of g: "))
    h = int(input("What is the value of h: "))
    i = int(input("What is the value of i: "))

    a_1 = (e*i) - (h*f)
    b_1 = (d*i) - (g*f)
    c_1 = (d*h) - (g*e)

    a_2 = a * a_1
    b_2 = b * b_1
    c_2 = c * c_1

    determinant = a_2 - b_2 + c_2

    print("Given matrices is: ")

    print("!", a, b, c, "!")
    print("!", d, e, f, "!")
    print("!", g, h, i, "!")

    repeat = input("Is there any correction?")
    if repeat == "yes":
        main()
    else:
        print("The value of the give determinant is: ", determinant)
        print("Thank you for using determinant .py calculator.")

main()
