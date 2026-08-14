import qrcode as qr

url = input("Enter the URL: ")
img = qr.make(url)
img.save("RutaGithubQRCode.png")
print("---QR Code is Generator---")