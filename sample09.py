import requests
import pprint

# i-seifuの郵便番号5450042
# https://zipcloud.ibsnet.co.jp/api/search?zipcode=5450042
url = 'https://zipcloud.ibsnet.co.jp/api/search?zipcode='
zipcode = '6300245'

# GET形式でネット上のデータ取得
res = requests.get(url + zipcode).json()
pprint.pprint(res)
