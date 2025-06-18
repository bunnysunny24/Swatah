import qrcode

# Replace with your actual deployed website URL
website_url = "https://swatah.vercel.app/"

# Create QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)
qr.add_data(website_url)
qr.make(fit=True)

# Create and save the image
img = qr.make_image(fill_color="black", back_color="white")
img.save("website_qr.png")

print(f"QR code generated for {website_url}")
print("Saved as website_qr.png")