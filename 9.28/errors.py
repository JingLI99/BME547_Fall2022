import imp


a = "The sky is blue"
print(a)

for letter in a:
    print(letter)
# Two types of error
# Syntax Error no output
# Exceptions


def function_name():
    X = [1, 3, 5]
    try:
        print(X[5])
    except IndexError:
        print("X[5] has an IndexError."
              "Print X[0] insread")
        print(X[0])
# More exception errors:
# ZeroDivisionError
# TypeError("x" + 2)
# ValueError
# IndexError
# ModuleNotFoundError
# AssertionError


def calc_square_root(n):
    try:
        from my_calculator import sqrt
    except ModuleNotFoundError:
        print("The my_calculator module was not found."
              "Loading Python math labrary instead")
        from math import sqrt
    answer = sqrt(n)
    print(answer)


def main():
    function_name()
#   calc_square_root(16)


if __name__ == "__main__":
    main()
