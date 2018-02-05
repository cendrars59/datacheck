from user import User

user1 = User('gus.leroux@yoyo.com', 'Gustave', 'Leroux', None)

print(user1)

print(user1.save_to_db())
