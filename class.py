from hashlib import new


class Patient:

    def __init__(self):
        self.first_name = ""
        self.last_name = ""
        self.paient_id = ""
        self.age = ""
        self.tests = []

    def full_name(self):
        return "{} {}".format(self.first_name, self.last_name)


def create_patient_entry(petient_first_name,
                         patient_last_name, patient_id,
                         patient_age):
    new_patient = Patient()
    new_patient.first_name = petient_first_name,
    new_patient.last_name = patient_last_name,
    new_patient.paient_id = patient_id,
    new_patient.age = patient_age
    return new_patient


def main():
    x = Patient
