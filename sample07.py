import os
import codecs

# 本ソースコードが保存されているフォルダのフルパスを取得
current_dirname = os.path.dirname(__file__) + '\\'

# withを付けて自動的にclose(ファイル閉じる)
with codecs.open(current_dirname + 'python_utf8_with.txt', 'w', 'utf-8') as file_obj :
    # UTF-8でテキストファイルを作る
    file_obj.write('Pythonから書き込みwith')
