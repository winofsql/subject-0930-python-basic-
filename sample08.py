# pip install requests
import requests
import pprint

# GET形式でネット上のデータ取得
res = requests.get('https://www.yahoo.co.jp/')

# ステータスコード表示
# https://developer.mozilla.org/ja/docs/Web/HTTP/Status
pprint.pprint(res)

# レスポンスデータ表示(HTMLデータ)
pprint.pprint(res.text)

# i-seifuの郵便番号5450042
# https://zipcloud.ibsnet.co.jp/api/search?zipcode=5450042
