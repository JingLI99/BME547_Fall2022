class Patient:
    def __init__(self):
        self.first_name = ""
        self.last_name = ""
        self.patient_id = ""
        self.age = ""
        self.tests = []
    
    def full_name(self):
        return "{} {}".format(self.first_name, self.last_name)


def create_patient_entry(patient_first_name,
                         patient_last_name, patient_id,
                         patient_age):

    new_patient = Patient()
    new_patient.first_name = patient_first_name
    new_patient.last_name = patient_last_name
    new_patient.patient_id = patient_id
    new_patient.age = patient_age

    return new_patient


def print_database(db):
    for patient in db:
        print("Name: {}, id:{}, age: {}".format(get_full_name(db[patient]),
                                                db[patient]["Id"],
                                                db[patient]["Age"]))


def get_full_name(patinet):
    full_name = "{} {}".format(patinet["First Name"], patinet["Last Name"])
    return full_name


def find_patient(db, id_no):
    patient = db[id_no]
    return patient


def add_test_to_patient(db, id_no, test_name, test_value):
    patient = find_patient(db, id_no)
    patient["Tests"].append((test_name, test_value))


def adult_or_minor(patient):
    if patient["Age"] >= 18:
        return "adult"
    else:
        return "minor"


def main():
    x = Patient()
    x.first_name = "Jing"
    x.last_name = "LI"
    print(x.full_name())
    print(type(x))

    y = Patient()
    y.first_name = "Edward"
    y.last_name = "Smith"
    print(y.last_name)
    exit()




    db = {}
    db[11] = create_patient_entry("Ann", "Ables", 11, 30)
    db[22] = create_patient_entry("Bob", "Boyles", 22, 34)
    db[33] = create_patient_entry("Chris", "Chou", 33, 25)
    print_database(db)
    add_test_to_patient(db, 33, "HDL", 100)
    print_database(db)
#    print("Patient {} is a {}".format(get_full_name(db[2]),
#                                      adult_or_minor(db[2])))


if __name__ == "__main__":
    main()