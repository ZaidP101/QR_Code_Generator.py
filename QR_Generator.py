# Library required = qrcode Image
import qrcode

def generator(text):

    qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size = 10,
        border = 4,
    )

    qr.add_data(text)
    qr.make(fit = True)
    img = qr.make_image(fill_color = "Black", back_color = "White")
    img.save(save_as)

url = input("Entre your URL : ")
save_as = input("Enter bellow the name of your QRcode's png : ")+ ".png"
generator(url)
