import requests
import json


def main():
    r = requests.get("http://vcm-7631.vm.duke.edu:5002/get_patients/jl1104")
    # Get the IDs for two patients
    IDs = r.text
    IDs = IDs.replace('"Donor":', '')
    IDs = IDs.replace('"Recipient":', '')
    IDs = IDs.replace('"', '')
    IDs = IDs.replace('\n', '')
    IDs = IDs.replace('{', '')
    IDs = IDs.replace('}', '')
    print(IDs)
    # The two id
    [id1, id2] = IDs.split(',')
    print(id1, id2)
    r2 = requests.get("http://vcm-7631.vm.duke.edu:5002/get_blood_type/F1")
    r3 = requests.get("http://vcm-7631.vm.duke.edu:5002/get_blood_type/F3")
    blood1 = r2.text
    blood2 = r3.text
    # O- B+
    # Check if it is an acceptable match
    if blood1 == blood2:
        match = 'Yes'
    else:
        match = 'No'
    # Generate json
    result = {"Name": "jl1104", "Match": match}
    out_file = open("check_result.json", "w")
    json.dump(result, out_file)
    out_file.close()

    # check if it's right
    r_check = requests.post("http://vcm-7631.vm.duke.edu:5002/match_check", json=result)
    print(r_check.text)





if __name__ == '__main__':
    main()



