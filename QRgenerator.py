import qrcode

qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H)

qr.add_data("https://youtu.be/BBJa32lCaaY?si=Fpj8ai7hoHqr-wou")
    
qr.make(fit=True)

img = qr.make_image(fill_color="blue", back_color="white")  

img.show()
