from person import Person


def main():
    person1 = Person("Marge Simpson", 38)
    person2 = Person("Asterix the Gaul", 55)
    person3 = Person("Leia Organa", 29)
    # person4 = Person("Bob Parr", 45)

    person1.introduce_self()
    person2.introduce_self()

    person1.befriend(person2)
    person1.befriend(person3)

    person1.introduce_self()
    person2.introduce_self()


main()
