import requests as r
import pandas as pd
from pprint import pprint
import json
import csv

url = 'https://www.googleapis.com/books/v1/volumes?q=cabana+intitle&printType=books&key=AIzaSyDrd_xrf20ypyItPUZT_K4jfYVJxECDIyA'
requisicao = r.get (url)
r = requisicao.content
data = json.loads(r)
df = pd.json_normalize(data['items'])



if requisicao.status_code == 200:
    print(df)
    
else:
    print ('Erro de requisição na API')


