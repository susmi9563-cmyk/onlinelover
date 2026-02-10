import qrcode

data = "https://navyaramsetty1210-arch.github.io/our-love-story/"

img = qrcode.make(data)
img.save("website_qr.png")