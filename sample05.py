import os

# 本ソースコードが保存されているフォルダのフルパスを取得
current_dirname = os.path.dirname(__file__) + '\\'

# Shift_JISでテキストファイルを作る(文字化けするパターン)
file_obj = open(current_dirname + 'python_sjis.txt', 'w')
file_obj.write('Pythonから書き込み')
file_obj.close()

