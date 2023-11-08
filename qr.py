import qrcode

# The URL you want to encode in the QR code
url = 'https://twitter.com'

# Create the QR code with the URL
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)

# Save the QR code as an image file
img = qr.make_image(fill_color="black", back_color="white")
img.save("qr_code.png")
