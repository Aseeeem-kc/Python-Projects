import qrcode as qr
from PIL import Image

my_qr = qr.QRCode(version=1, 
                  error_correction=qr.constants.ERROR_CORRECT_H, 
                  box_size=10, border=4)

my_qr.add_data("https://www.instagram.com/aseeeem_12/")
my_qr.make(fit=True)

img = my_qr.make_image(fill_color="black", back_color="white")
img.save("myinsta.png")
