

class Person: 
    name: str
    last_name: str
    def __init__(self,name,last_name):
        self.name = name
        self.last_name = last_name
        pass

    def whoami(self):
        print(self.name)
        print(self.last_name)

    