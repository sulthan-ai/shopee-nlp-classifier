from google_play_scraper import app, reviews, Sort
import pandas as pd

# Mengambil data app Shopee di PlayStore
scrap = reviews(
    'com.shopee.id',
    lang='id',
    country='id',
    sort=Sort.MOST_RELEVANT,
    count=11000
)[0]

dataset = pd.DataFrame(scrap)[['content']]
dataset.to_csv('dataset.csv', index=False)