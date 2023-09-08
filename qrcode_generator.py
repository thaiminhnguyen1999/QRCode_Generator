import qrcode

qrcode_image_data = input("Enter the data you want to create a QR code (Text, Link, Phone Number, ...): ")

qrcode_image_name = input("Name for your QR code image file (Default is qrcode.png): ")
img = qrcode.make(qrcode_image_data)

if qrcode_image_name == "":
    img.save("./output/qrcode.png")
    print("Your QR code image is saved in: ./output/qrcode.png")
else:
    img.save("./output/" + qrcode_image_name + ".png")
    print("Your QR code image is saved in: ./output/" + qrcode_image_name + ".png")