class Person:
    """
    A class representing a person
    """
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.friends = []

    def befriend(self, new_friend):
        """
        Adds a new person to the list of friends
        """
        print(self.name, "befriends", new_friend.name)
        self.add_friend(new_friend)
        new_friend.add_friend(self)

    def add_friend(self, new_friend):
        self.friends.append(new_friend)

    def introduce_self(self):
        """
        Introduce self
        """
        print("Hi, I'm", self.name, "and I'm", self.age, "years old.")
        if len(self.friends) > 0:
            self.introduce_friends()
        print()

    def introduce_friends(self):
        print("\tMy friends are:")
        for friend in self.friends:
            print("\t\t" + friend.name)
