class Plant:
    "Plant informations"

    def __init__(self, name, height, age):
        self.__name = name
        self.__height = height
        self.__age = age
        print("Created:", end=" ")
        self.show()

    def set_height(self, height):
        if (height < 0):
            print(f"{self.__name.capitalize()}: "
                  "Error, height can’t be negative")
            print("Height update rejected")
        else:
            self.__height = height
            print(f"Height updated: {height}cm")

    def set_age(self, age):
        if (age < 0):
            print(f"{self.__name.capitalize()}: "
                  "Error, age can’t be negative")
            print("Age update rejected")
        else:
            self.__age = age
            print(f"Age updated: {age} days")

    def get_height(self):
        return (self.__height)

    def get_age(self):
        return (self.__age)

    def show(self):
        print(f"{self.__name.capitalize()}: {self.__height}cm,"
              f" {self.__age} days old\n")

    def age(self):
        self.__age += 1

    def grow(self):
        daily_growth = 0.8
        week = 7
        for days in range(week + 1):
            if (days == 0):
                print("=== Garden Plant Growth ===")
                print(f"{self.__name.capitalize()}: "
                      f"{round(self.__height, 1)}cm, {self.__age} days old")
            else:
                self.__height += daily_growth
                self.age()
                print(f"=== Day {days} ===")
                print(f"{self.__name.capitalize()}: "
                      f"{round(self.__height, 1)}cm, {self.__age} days old")
        print(f"Growth this week: {round(daily_growth * week, 1)}cm")


def main():
    print("=== Garden Security System ===")
    rose = Plant('rose', 15.0, 10)

    rose.set_height(25)
    rose.set_age(30)
    print()
    rose.set_height(-20)
    rose.set_age(-10)
    print()
    rose.show()


if __name__ == "__main__":
    main()
