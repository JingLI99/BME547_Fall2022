from tkinter import filedialog
import base64
import requests


def upload_image():
    filename = get_image_file_name()
    b64_string = convert_file_to_b64(filename)
    # result = upload_b64_to_server(b64_string)
    status_code, get_b64 = get_stored_image()
    # Saves the downloaded base64 string as an image file
    image = save_b64_image(get_b64)


def get_image_file_name():
    # filename = filedialog.askopenfilename()
    filename = 'images/china.jpg'
    return filename


def convert_file_to_b64(filename):
    with open(filename, "rb") as image_file:
        b64_bytes = base64.b64encode(image_file.read())
    b64_string = str(b64_bytes, encoding='utf-8')
    return b64_string


def upload_b64_to_server(b64_string):
    out_data = {'image': b64_string, 'net_id': 'jl1104', 'id_no': 2}
    r = requests.post("http://vcm-21170.vm.duke.edu/add_image",
                      json=out_data)
    return r.status_code, r.text


def get_stored_image():
    r = requests.get("http://vcm-21170.vm.duke.edu/get_image/jl1104/1")
    return r.status_code, r.text


def save_b64_image(base64_string):
    image_bytes = base64.b64decode(base64_string)
    with open("new-img.jpg", "wb") as out_file:
        out_file.write(image_bytes)
    return


if __name__ == '__main__':
    upload_image()
