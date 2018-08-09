class Animal:
    def __init__(self, name):
        self.name = name

    def attack(self):
        return __import__("random").random()

def main():
    animal = Animal("Nick")
    print(animal.attack())

if __name__ == "__main__":
    main()
