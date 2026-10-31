class Plant:
    "Plant informations"

    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def show(self):
        print(f"{self.name.capitalize()}: {self.height}cm,"
              f" {self.age} days old")


def main():
    rose = Plant("rose", 25, 30)
    sunf = Plant('sunflower', 80, 45)
    cactus = Plant('cactus', 15, 120)

    print("=== Garden Plant Registry ===")
    rose.show()
    sunf.show()
    cactus.show()


if __name__ == "__main__":
    main()
