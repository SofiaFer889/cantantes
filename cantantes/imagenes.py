import base64

with open("cantantes/concierto.jpg.jpg", "rb") as img_file:
    my_string = base64.b64encode(img_file.read()).decode('utf-8')
    print(my_string)