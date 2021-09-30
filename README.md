# python20210930
2021/09/30(木)の午前に実施したPythonプログラム

## ■ ファイルオブジェクト

```python
import os

# 本ソースコードが保存されているフォルダパス
current_dirname = os.path.dirname(__file__) + '\\'

# 文字化けパターン
file_obj = open(current_dirname + 'python_sjis.txt', 'w')
file_obj.write('Pythonから書き込み')
file_obj.close()

# UTF-8対策
import codecs
file_obj = codecs.open(current_dirname + 'python_utf8.txt', 'w', 'utf-8')
file_obj.write('Pythonから書き込み')
file_obj.close()
```

### withを使ったファイルの書き込み

```python
import codecs
import os

# 本ソースコードが保存されているフォルダパス
current_dirname = os.path.dirname(__file__) + '\\'

# withは、close忘れが無くなる
# withを抜けると自動的にcloseされる
with codecs.open(current_dirname + 'python_with.txt', 'w', 'utf-8') as file_obj:
  file_obj.write('withを使って書き込み')
```

# さまざまな機能を取り込もう

外部ライブラリを追加するコマンド
```bash
# インストール
pip install ライブラリ名
pip install Pillow

# アンインストール
pip uninstall ライブラリ名
pip uninstall Pillow

# 詳細表示
pip show ライブラリ名
pip show Pillow

# モジュール一覧表示
pip list
```

## ■ 外部ライブラリを使ったプログラミング : Pythonで画像処理
```bash
pip install Pillow
```

画像の色変え

```python
import os
from PIL import Image

# 本ソースコードが保存されているフォルダパス
current_dirname = os.path.dirname(__file__) + '\\'

# 色変換
image = Image.open(current_dirname + 'files/flower01.jpg')

# 表示(アプリ起動)
image.show()

# RGB毎に分離できる
r, g, b = image.split()

# RGB → BGR に置き換え再作成(merge=合体)
# 赤と青を入れ替える
convert_image = Image.merge("RGB", (b, g, r))

# 保存
convert_image.save(current_dirname + 'files/flower01_convert.jpg')

# 表示(アプリ起動)
convert_image.show()
```

複数画像の色変え

```python
import os
from PIL import Image

# 本ソースコードが保存されているフォルダパス
current_dirname = os.path.dirname(__file__) + '\\'

# 変換対象画像一覧
images = (
          'flower01.jpg',
          'flower02.jpg',
          'flower03.jpg'
          )

for image in images :
  image_file = Image.open(current_dirname + 'files/' + image)

  # R(Red) G(Green) B(Blue)にそれぞれ分ける
  r, g, b = image_file.split()
  
  # "RGB" → "BGR" (RBをBRを入れ替え、Gはそのまま)
  convert_image = Image.merge("RGB", (b, g, r))
  convert_image.save(current_dirname + 'files/convert_' + image)
  image_file.show()
  convert_image.show()
```

その他画像の加工

```python
import os
from PIL import Image

# 本ソースコードが保存されているフォルダパス
current_dirname = os.path.dirname(__file__) + '\\'

image = Image.open(current_dirname + 'files/flower01.jpg')

# グレースケール
black_and_white = image.convert('L')

# 表示
black_and_white.show()

# 90度回転で表示
black_and_white.transpose(Image.ROTATE_90).show()

# 180度回転で表示
black_and_white.transpose(Image.ROTATE_180).show()

# 270度回転で表示
black_and_white.transpose(Image.ROTATE_270).show()

# 左右反転で表示
black_and_white.transpose(Image.FLIP_LEFT_RIGHT).show()

# 上下反転で表示
black_and_white.transpose(Image.FLIP_TOP_BOTTOM).show()
```

## ■ 外部ライブラリを使ったプログラミング : Pythonでインターネットにアクセス

```bash
pip install requests
```

```python
import requests
import pprint

# GETでデータ取得
res = requests.get('https://yahoo.co.jp')

# ちょっと整形して表示
pprint.pprint(res.text)
```

郵便場号から住所取得

```python
import requests
import pprint

# zipcloud
# http://zipcloud.ibsnet.co.jp/doc/api

url = 'https://zipcloud.ibsnet.co.jp/api/search?zipcode='
zipcode = '5450042'
zipinfo = requests.get(url + zipcode).json()
pprint.pprint(zipinfo)
```

Wikipediaの情報取得

```python
# MediaWiki
# https://www.mediawiki.org/wiki/MediaWiki/ja
# MediaWiki API
# https:www.mediawiki.org/wiki/API:Main_page/ja
# Wikipedia API
# https://ja.wikipedia.org/w/api.php

import requests, pprint
api_url = 'https://ja.wikipedia.org/w/api.php'
api_params = {
  'format' : 'json',
  'action' : 'query',
  'titles' : 'マグロ',
  'prop' : 'revisions',
  'rvprop' : 'content'
}

wiki_data = requests.get(api_url, params=api_params).json()
pprint.pprint(wiki_data)
```

## ■ 外部ライブラリを使ったプログラミング : Pythonで情報収集
- クローリング
  - Webサイトからそのまま情報を取得(スクロールから来てる)
- スクレイピング
  - クローリングしたデータから、必要なデータだけ抽出する
  - scrape(スクレープ)「けずって剥がす」から来てる

- BeautifulSoup4
  - スクレイピング便利モジュール

- インストール
```bash
pip install requests
pip install beautifulsoup4
```

スクレイピングに挑戦

YahooニュースのITカテゴリからニュースを一覧を取得

```python
import requests
from bs4 import BeautifulSoup

# 指定したURL先をGET形式でダウンロード
html_data = requests.get('https://yahoo.co.jp')
print(html_data.text)

# HTMLを解析するためのプログラムの種類
soup = BeautifulSoup(html_data.text, "html.parser")
print(soup.title)

# 「Yahoo!ニュース」をスクレイピング
yahoo_itnews = requests.get('https://news.yahoo.co.jp/rss/topics/it.xml')
soup = BeautifulSoup(yahoo_itnews.text, "html.parser")
print(soup.findAll('item'))

for news in soup.findAll('item') :
  print(news.title.string)
```

## ■ かんたんなアプリケーションを作ってみよう
```bash
pip install qrcode
```

QRコードの画像作成

basic035.py
```python
import qrcode

encode_text = 'https://google.com'
image = qrcode.make(encode_text)
image.show()
```
