import requests

# r = requests.get("https://docs.github.com/rest/reference/repos#list-branches")
"""
r = requests.get("https://api.github.com/repos/JingLI99/BME547_Fall2022/branches")
print(r)
print(type(r))
print(r.text)
if r.status_code == 200:
    answer = r.json()
    print(type(answer))
    for branch in answer:
        print(branch["name"])
else:
    print("Bad request: {}".format(r.text))


output_info = {"name": "Jing LI",
               "net_id": "JingLI99",
               "e-mail": "jl1104@duke.edu"}
r = requests.post("http://vcm-21170.vm.duke.edu:5000/student",
                  json=output_info)
print(r)
print(r.text)

r = requests.get("http://vcm-21170.vm.duke.edu:5000/list")
print(r.text)

"""
output_info = {"user": "Jing LI",
               "message": "Hello World"}
r = requests.post("http://vcm-21170.vm.duke.edu:5001/add_message",
                  json=output_info)
print(r)
print(r.text)

r2 = requests.get("http://vcm-21170.vm.duke.edu:5001/get_messages/Jing LI")
print(r2)
print(r2.text)
