def dosage_on_age(age_in_years):
    if age_in_years < 10:
        print("15 mg")
    elif age_in_years < 15:
        print("18 mg")
    elif age_in_years < 20:
        print("22 mg")
    else:
        print("25 mg")


if __name__ == '__main__':
    print("The dosage is: ")
    dosage_on_age(19)
