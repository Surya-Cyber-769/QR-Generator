import qrcode

link = input("Enter your link: ")

if not link.strip():
    print("❌ No link entered")
    exit()

qr = qrcode.QRCode(border=1)
qr.add_data(link)
qr.make()

print("\n📌 Your QR code:\n")
for row in qr.get_matrix():
    print("".join("██" if cell else "  " for cell in row))
print("\n✔ Done!\n")

