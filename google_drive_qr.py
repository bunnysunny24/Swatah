import qrcode
from datetime import datetime

# Your Google Drive PDF URL
pdf_url = "https://drive.google.com/file/d/1eM6RTY0fyS5lijjuiz7ys77JT4c3R2Fv/view?usp=sharing"

# Output file name for the QR code
qr_output_path = "pdf_qr.png"

# QR code size (higher = larger)
qr_size = 10

# Create QR code instance
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=qr_size,
    border=4,
)

# Add data to the QR code
qr.add_data(pdf_url)
qr.make(fit=True)

# Create an image from the QR code
img = qr.make_image(fill_color="black", back_color="white")

# Save the image
img.save(qr_output_path)

# Display information
username = "bunnysunny24"
timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")

print(f"QR code generated by {username} on {timestamp} UTC")
print(f"QR code saved to: {qr_output_path}")
print(f"The QR code points to: {pdf_url}")
print("When someone scans this QR code, they will be directed to your PDF on Google Drive.")