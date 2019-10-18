from person import Person


def main():
    person1 = Person("Marge Simpson", 38)
    person2 = Person("Asterix the Gaul", 55)
    person3 = Person("Leia Organa", 29)

    person1.introduce_self()
    person2.introduce_self()
    person3.introduce_self()

    person1.befriends(person2)
    person1.befriends(person3)

    person1.introduce_self()
    person2.introduce_self()
    person3.introduce_self()


main()
