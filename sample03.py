import os
from PIL import Image

# 本ソースコードが保存されているフォルダのフルパスを取得
current_dirname = os.path.dirname(__file__) + '\\'

# 変換対象の画像一覧
images = (
    'flower01.jpg',
    'flower02.jpg',
    'flower03.jpg'
)

for image in images :
    image_file = Image.open(current_dirname + image)
    
    # RGB(RedGreenBlue)
    r, g, b = image_file.split()

    # RGB → BGR に置き換えて、画像再作成(merge=合体)
    # 赤の所を青に入れ替える、青の所を赤に入れ替える
    convert_image = Image.merge("RGB", (g, r, b))

    # 画像保存
    convert_image.save(current_dirname + 'convert_' + image)

    # 表示(変換後)
    convert_image.show()
