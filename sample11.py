# pip install qrcode
import qrcode

encode_text = 'http://google.com'
image = qrcode.make(encode_text).show()
image.show()

# この一行だけでもQRコード作成可能
qrcode.make('http://google.com').show()