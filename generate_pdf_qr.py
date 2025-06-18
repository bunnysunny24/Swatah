import qrcode
import os
from urllib.parse import quote

def generate_pdf_qr(pdf_path, qr_output_path="pdf_qr.png", qr_size=10):
    """
    Generate a QR code that links to a PDF document.
    
    Parameters:
    - pdf_path: Path to the PDF file (can be a local file path or URL)
    - qr_output_path: Where to save the QR code image
    - qr_size: Size of the QR code (higher number = larger QR)
    
    Returns:
    - Path to the generated QR code image
    """
    # Check if the path is a URL or local file
    if pdf_path.startswith(('http://', 'https://')):
        # It's already a URL, use it directly
        pdf_url = pdf_path
    else:
        # It's a local file, convert to file:// URL
        # First get the absolute path
        abs_path = os.path.abspath(pdf_path)
        # Convert to URL format with proper encoding
        pdf_url = f"file://{quote(abs_path)}"
    
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
    
    return qr_output_path

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description='Generate QR code for a PDF document')
    parser.add_argument('pdf_path', help='Path to the PDF file or URL')
    parser.add_argument('--output', '-o', default='pdf_qr.png', help='Output path for QR code image')
    parser.add_argument('--size', '-s', type=int, default=10, help='Size of QR code')
    
    args = parser.parse_args()
    
    qr_path = generate_pdf_qr(args.pdf_path, args.output, args.size)
    print(f"QR code generated and saved to: {qr_path}")