def convert_weight():
    weight_lb = float(input("Enter weight in lbs: "))
    weight_kg = weight_lb / 2.205
    return weight_kg


if __name__ == '__main__':
    weight_kg = convert_weight()
    print(weight_kg)
