import skingrabber as sg
import requests
from PIL import Image

s = sg.skingrabber()

name = ''

while name != exit:
    try:
        name = input('Minecraft username> ')
        r = s.get_skin_rendered(name)

        response = requests.get(r)
        #print (response.status_code)
        with open('img.png', 'wb') as f:
            f.write(response.content)

        img = Image.open('img.png')
        img.show()
    except:
        print('An error occured, please try again')