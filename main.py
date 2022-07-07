print("Hello!")
print("Welcome to determinant .py calculator")

print("For which order determinant, do you want to find the determinant value")

y1 = input("Is it 2*2?")

y_1 = y1.lower()

if y_1 == "yes":
    # for 2*2 matrix

    print("Since it is a 2 * 2 matrices...")

    def main():

        print("!", "p", "q", "!")
        print("!", "r", "s", "!")

        p = int(input("What is the value of p: "))
        q = int(input("What is the value of q: "))
        r = int(input("What is the value of r: "))
        s = int(input("What is the value of s: "))

        print("Given matrices is:")
        print("!", p, q, "!")
        print("!", r, s, "!")

        repeat_1 = input("Is there any corrections?")
        repeat = repeat_1.lower()
        if repeat == "yes":
            main()

        else:
            determinant_2 = p * s - q * r

            print("The value of the given determinant is: ", determinant_2)
            print("Thank you for using determinant .py calculator.")

    main()

elif y_1 == "no":

    print("Then since it is a 3 * 3 matrices..")

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

        a_1 = (e * i) - (h * f)
        b_1 = (d * i) - (g * f)
        c_1 = (d * h) - (g * e)

        a_2 = a * a_1
        b_2 = b * b_1
        c_2 = c * c_1

        determinant_3 = a_2 - b_2 + c_2

        print("Given matrices is: ")

        print("!", a, b, c, "!")
        print("!", d, e, f, "!")
        print("!", g, h, i, "!")

        repeat_1 = input("Is there any correction?")
        repeat = repeat_1.lower()

        if repeat == "yes":
            main()
        else:
            print("The value of the give determinant is: ", determinant_3)
            print("Thank you for using determinant .py calculator.")


    main()
