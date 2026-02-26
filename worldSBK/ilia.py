# generate qr code 
import qrcode
url = input("Enter the URL: ").strip()
file_path = "C:\\Users\\Student\\Desktop\\qr_code.png"



qr = qrcode.QRCode()
qr.add_data(url)


img = qr.make_image()
img.save(file_path)



print("QR CODE GENERATED SUCCESSFULLY")
