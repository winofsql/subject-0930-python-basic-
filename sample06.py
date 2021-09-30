import os
import codecs

# 本ソースコードが保存されているフォルダのフルパスを取得
current_dirname = os.path.dirname(__file__) + '\\'

# UTF-8でテキストファイルを作る
file_obj = codecs.open(current_dirname + 'python_utf8.txt', 'w', 'utf-8')
file_obj.write('Pythonから書き込み')
file_obj.close()
