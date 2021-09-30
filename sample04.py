import os
from PIL import Image

# 本ソースコードが保存されているフォルダのフルパスを取得
current_dirname = os.path.dirname(__file__) + '\\'

# 色変換
image = Image.open(current_dirname + 'flower01.jpg')

# グレースケール
b_and_w = image.convert('L')
b_and_w.show()

# 90度回転で表示
b_and_w.transpose(Image.ROTATE_90).show()

# 180度回転で表示
b_and_w.transpose(Image.ROTATE_180).show()

# 270度回転で表示
b_and_w.transpose(Image.ROTATE_270).show()

# 左右反転で表示
b_and_w.transpose(Image.FLIP_LEFT_RIGHT).show()

# 上下反転で表示
b_and_w.transpose(Image.FLIP_TOP_BOTTOM).show()