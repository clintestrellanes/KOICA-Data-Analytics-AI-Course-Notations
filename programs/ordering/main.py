from person import Person

def input_name():
    name=input("input name:")
    last_name=input("input lastname:")
    person = Person(name,last_name)

    person.whoami()

    




if __name__ == "__main__":
    input_name()