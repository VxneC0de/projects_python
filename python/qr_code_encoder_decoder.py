#import qrcode

#data = 'Don\'t forget to subscribe'

from pyzbar.pyzbar import decode
from PIL import Image

#FirstCode

#img = qrcode.make(data)

#img.save('C:/Users/Vanesa/VxneC0de/projects_python/save/myqrcode.png')



#SecondCode

#qr = qrcode.QRCode(version = 1, box_size=10, border=5)

#qr.add_data(data)

#qr.make(fit=True)
#img = qr.make_image(fill_color = 'red', back_color = 'white')

#img.save('C:/Users/Vanesa/VxneC0de/projects_python/save/myqrcode1.png')



#ThirdCode


img = Image.open('C:/Users/Vanesa/VxneC0de/projects_python/save/myqrcode1.png')

result = decode(img)

print(result)