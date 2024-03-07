import qrcode as qr

img = qr.make("https://www.instagram.com/aseeeem_12/")

img.save("insta-profile.png")