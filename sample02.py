import os
from PIL import Image

# 本ソースコードが保存されているフォルダのフルパスを取得
current_dirname = os.path.dirname(__file__) + '\\'

# 色変換
image = Image.open(current_dirname + 'flower01.jpg')

# 表示(色変換前)
# image.show()

# RGB(RedGreenBlue)
r, g, b = image.split()

# RGB → BGR に置き換えて、画像再作成(merge=合体)
# 赤の所を青に入れ替える、青の所を赤に入れ替える
convert_image = Image.merge("RGB", (b, g, r))

# 画像保存
convert_image.save(current_dirname + 'flower01_convert.jpg')

# 表示(変換後)
convert_image.show()
