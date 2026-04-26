import random

def get_new_user():
    random_number = random.randint(10000, 99999)

    return {
        "name": f"TestUser{random_number}",
        "email": f"testuser{random_number}@gmail.com",
        "password": "123456",
        "avatar": "https://picsum.photos/800"
    }
