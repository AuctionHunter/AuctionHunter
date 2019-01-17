from pymongo import MongoClient
from pprint import pprint

def main():
    #Establish connection
    client = MongoClient("localhost", 27017)
    #Access Database
    db = client.admin
    #post data
    posts = db.posts
    post_data = {
        'make': 'Ford',
        'model': 'Focus',
        'year': '2012',
        'color': 'Red',
        'damage': 'lots'
    }
    result = posts.insert_one(post_data)
    pprint(result)
    print('One post: {0}'.format(result.inserted_id))

    post_1 = {
        'make': 'Honda',
        'model': 'Civic',
        'year': '2014',
        'color': 'Black',
        'damage': 'none'
    }
    post_2 = {
        'make': 'Toyota',
        'model': 'Corolla',
        'year': '2013',
        'color': 'Blue',
        'damage': 'minimal'
    }
    result = posts.insert_many([post_1, post_2])
    print('Multiple posts: {0}'.format(result.inserted_ids))

    #Retrieve data
    retrive_post = posts.find_one({"author": "Honda"})
    print(retrive_post)

if __name__ == "__main__":
    main()