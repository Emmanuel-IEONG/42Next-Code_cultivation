class Plant:
    "Plant informations"

    def __init__(self, name, height, age):
        self.__name = name
        self.__height = height
        self.__age = age
        # print("Created:", end=" ")
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

    def get_name(self):
        return (self.__name)

    def get_height(self):
        return (self.__height)

    def get_age(self):
        return (self.__age)

    def show(self):
        print(f"{self.__name.capitalize()}: {round(self.__height, 1)}cm,"
              f" {self.__age} days old")

    def age(self):
        self.__age += 1

    def grow(self, daily_growth, days):
        for _ in range(days):
            self.__height += daily_growth
            self.age()


class Flower(Plant):
    def __init__(self, name, height, age, color, bloomed):
        self.__color = color
        self.__bloomed = bloomed
        super().__init__(name, height, age)

    def set_bloomed(self, bloomed):
        self.__bloomed = bloomed

    def get_color(self):
        return (self.__color)

    def get_bloomed(self):
        return (self.__bloomed)

    def bloom(self):
        print(f"[asking the {self.get_name()} to bloom]")
        self.set_bloomed(True)

    def show(self):
        super().show()
        print(f"Color: {self.get_color()}")
        if (self.get_bloomed()):
            print(f"{self.get_name().capitalize()} is blooming beautifully!")
        else:
            print(f"{self.get_name().capitalize()} has not bloomed yet")


class Tree(Plant):
    def __init__(self, name, height, age, diameter):
        self.__diameter = diameter
        super().__init__(name, height, age)

    def get_diameter(self):
        return (self.__diameter)

    def show(self):
        super().show()
        print(f"Trunk diameter: {self.get_diameter()}cm")

    def produce_shade(self):
        print(f"[asking the {self.get_name()} to produce shade]")
        print(f"Tree {self.get_name().capitalize()} now produces a shade of "
              f"{self.get_height()}cm long and {self.get_diameter()}cm wide")


class Vegetable(Plant):
    def __init__(self, name, height, age, harvest_season, nutritional_value):
        self.__harvest_season = harvest_season
        self.__nutritional_value = nutritional_value
        super().__init__(name, height, age)

    def set_nutritional_value(self, nutritional_value):
        self.__nutritional_value = nutritional_value

    def get_harvest_season(self):
        return (self.__harvest_season)

    def get_nutritional_value(self):
        return (self.__nutritional_value)

    def show(self):
        super().show()
        print(f"Harvest season: {self.get_harvest_season().capitalize()}")
        print(f"Nutritional value: {self.get_nutritional_value()}")

    def grow(self, daily_growth, days):
        print(f"[make {self.get_name()} grow and age for {days} days]")
        super().grow(daily_growth, days)
        self.set_nutritional_value(self.get_nutritional_value() + days)


def test_rose():
    print("=== Flower")
    flower = Flower('rose', 15.0, 10, 'red', False)
    flower.bloom()
    flower.show()


def test_tree():
    print("\n=== Tree")
    tree = Tree('oak', 200.0, 365, 5.0)
    tree.produce_shade()


def test_vege():
    print("\n=== Vegetable")
    vege = Vegetable('tomato', 5.0, 10, 'April', 0)
    vege.grow(2.1, 20)
    vege.show()


def main():
    print("=== Garden Plant Types ===")
    test_rose()
    test_tree()
    test_vege()


if __name__ == "__main__":
    main()
