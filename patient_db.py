def create_patient_entry(patient_name, patient_id, patient_age):
    new_patient = [patient_name, patient_id, patient_age, []]
    return new_patient


def main():
    db = []
    db.append(create_patient_entry("Ann Ables", 1, 30))
    db.append(create_patient_entry("Bob Boyles", 2, 34))
    db.append(create_patient_entry("Chris Chou", 3, 25))
    print_patient_information(db)
    x = look_up_id(db, 3)
    print(x)
    add_test_result(db, 2, 'Blood', 'Good')
    print(db)


def print_patient_information(db):
    for i in db:
        print("Name: {}, id: {}, age: {}.".format(i[0], i[1], i[2]))


def look_up_id(db, id):
    for i in db:
        if i[1] == id:
            return i
    return False


def add_test_result(db, id, test_name, test_value):
    patient = look_up_id(db, id)
    patient[3].append((test_name, test_value))


if __name__ == "__main__":
    main()
