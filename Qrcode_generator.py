import qrcode
import subprocess
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data("https://nandana-pradeep33.github.io/HarithamAutoElectricals/")
qr.make(fit=True)

img = qr.make_image(fill_color="rgb(0,171,154)", back_color="black")
img.save('qr1.png')
subprocess.run(['start', 'qr1.png'], shell=True)