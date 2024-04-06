class User:

    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.follower = 0
        self.following = 0

    def follow(self, user):
        user.follower += 1
        self.following += 1


u1 = User("001", "Angela")
u2 = User("002", "Jack")

u1.follow(u2)

print(u1.follower)
print(u1.following)
print(u2.follower)
print(u2.following)

