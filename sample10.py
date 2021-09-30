import requests
import pprint

url = 'https://ja.wikipedia.org/w/api.php'

wiki_params = {
    'format' : 'json',
    'action' : 'query',
    'titles' : 'クォークグルーオンプラズマ',
    'prop' : 'revisions',
    'rvprop' : 'content'
}

res = requests.get(url, params=wiki_params).json()
pprint.pprint(res)