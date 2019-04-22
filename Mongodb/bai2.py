import pymongo

client = pymongo.MongoClient("mongodb://admin:admin@ds021182.mlab.com:21182/c4e")

db = client.c4e

hi_posts = {
    'title' : 'Mai yeu anh ',
    'author' :'Hong Nhung',
    'content':'Va neu nhu co mt ngay anh khong thay e..'
    }


db.users.insert_one(hi_posts)