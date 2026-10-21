"""Create a QR code image. Install dependency first: python -m pip install qrcode[pil]"""
try:
    import qrcode
except ImportError:
    print("Missing package. Install it with: python -m pip install \"qrcode[pil]\"")
else:
    text = input("Enter text or a URL for the QR code: ").strip()
    if not text:
        print("Input cannot be empty.")
    else:
        image = qrcode.make(text)
        filename = "my_qr_code.png"
        image.save(filename)
        print(f"QR code saved as {filename}")
