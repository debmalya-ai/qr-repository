import qrcode

# The data or link you want to embed
data = "https://google.com"

# Generate the QR code
img = qrcode.make(data)

# Save it as an image file
img.save("basic_qr.png")
print("QR Code generated successfully!")
