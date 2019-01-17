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
        'title': 'Python and MongoDB',
        'content': 'PyMongo is fun, you guys',
        'author': 'Scott'
    }
    result = posts.insert_one(post_data)
    pprint(result)
    print('One post: {0}'.format(result.inserted_id))

    post_1 = {
    'title': 'Python and MongoDB',
    'content': 'PyMongo is fun, you guys',
    'author': 'Scott'
    }
    post_2 = {
        'title': 'Virtual Environments',
        'content': 'Use virtual environments, you guys',
        'author': 'Scott'
    }
    post_3 = {
        'title': 'Learning Python',
        'content': 'Learn Python, it is easy',
        'author': 'Bill'
    }
    result = posts.insert_many([post_1, post_2, post_3])
    print('Multiple posts: {0}'.format(result.inserted_ids))

    #Retrieve data
    retrive_post = posts.find_one({"author": "Bill"})
    print(retrive_post)

if __name__ == "__main__":
    main()