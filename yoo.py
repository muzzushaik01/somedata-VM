def div():
    try:
        a = int(input())
        b = int(input())
        print(a/b)
    except ZeroDivisionError:
        print("demoninator is zero")
    except ValueError:
        print("Value Error")
    except ArithmeticError:
        print("Arthematic Error")


def stringop():
    try:
        a = input()
        b = input()
        print(a/b)
    except TypeError:
        print("TYPEERROR")
    except ValueError:
        print("Value Error")
c = stringop()

