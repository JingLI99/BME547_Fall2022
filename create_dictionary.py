def create_dictionary():
    new_dictionary = {"day": "between sunrise and sunset",
                      "food": "something to eat",
                      "night":  "when the moon is out"}
    return new_dictionary


def output_dictionary(in_dictionary):
    print("Variable type:")
    print(type(in_dictionary))
    print("Dictionary contents:")
    print(in_dictionary)


if __name__ == "__main__":
    my_dictionary = create_dictionary()
    output_dictionary(my_dictionary)
