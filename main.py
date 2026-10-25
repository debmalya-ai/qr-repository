import qrcode

# The data or link you want to embed
data = "https://www.xraiga.dev"

# Generate the QR code
img = qrcode.make(data)

# Save it as an image file
img.save("XRaiga.png")
print("QR Code generated successfully!")
