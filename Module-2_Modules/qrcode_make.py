import qrcode

url="https://www.tops-int.com/"

x=qrcode.make(url)
x.save('tops.png')