class Plant:
    "Plant informations"

    class Statistics:
        def __init__(self):
            self.__grow_calls = 0
            self.__age_calls = 0
            self.__show_calls = 0

        def count_grow(self):
            self.__grow_calls += 1

        def count_age(self):
            self.__age_calls += 1

        def count_show(self):
            self.__show_calls += 1

        def display(self):
            print(f"Stats: {self.__grow_calls} grow, "
                  f"{self.__age_calls} age, {self.__show_calls} show")

    @staticmethod
    def is_year_old(age):
        return (age > 365)

    @classmethod
    def anonymous(cls, height, age):
        return (cls("Unknown plant", height, age))

    def __init__(self, name, height, age):
        self.__stats = self.Statistics()
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

    def get_statistics(self):
        return (self.__stats)

    def show(self):
        self.__stats.count_show()
        print(f"{self.__name.capitalize()}: {round(self.__height, 1)}cm,"
              f" {self.__age} days old")

    def age(self):
        self.__stats.count_age()
        self.__age += 1

    def grow(self, daily_growth, days):
        self.__stats.count_grow()
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
    class Statistics(Plant.Statistics):
        def __init__(self):
            super().__init__()
            self.__shade_calls = 0

        def count_shade(self):
            self.__shade_calls += 1

        def display(self):
            super().display()
            print(f"{self.__shade_calls} shade")

    def __init__(self, name, height, age, diameter):
        self.__diameter = diameter
        super().__init__(name, height, age)

    def get_diameter(self):
        return (self.__diameter)

    def show(self):
        super().show()
        print(f"Trunk diameter: {self.get_diameter()}cm")

    def produce_shade(self):
        self.get_statistics().count_shade()
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


class Seed(Flower):
    def __init__(self, name, height, age, color, bloomed, seeds):
        self.__seeds = seeds
        super().__init__(name, height, age, color, bloomed)

    def bloom(self):
        super().bloom()
        self.__seeds = 42

    def show(self):
        super().show()
        print(f"Seeds: {self.__seeds}")


def display_stats(plant):
    print(f"[statistics for {plant.get_name().capitalize()}]")
    plant.get_statistics().display()


def check_year():
    print("=== Check year-old")
    print("Is 30 days more than a year? ->", Plant.is_year_old(30))
    print("Is 400 days more than a year? ->", Plant.is_year_old(400))


def test_rose():
    print("\n=== Flower")
    flower = Flower('rose', 15.0, 10, 'red', False)
    display_stats(flower)
    flower.bloom()
    flower.grow(2.0, 5)
    flower.show()
    display_stats(flower)


def test_tree():
    print("\n=== Tree")
    tree = Tree('oak', 200.0, 365, 5.0)
    display_stats(tree)
    tree.produce_shade()
    display_stats(tree)


def test_vege():
    print("\n=== Vegetable")
    vege = Vegetable('tomato', 5.0, 10, 'April', 0)
    vege.grow(2.1, 20)
    vege.show()


def test_seed():
    print("\n=== Seed")
    sunflower = Seed("sunflower", 80.0, 45, "yellow", False, 0)
    sunflower.grow(2.0, 20)
    sunflower.bloom()
    sunflower.show()
    display_stats(sunflower)


def test_anonymous():
    print("\n=== Anonymous")
    ano = Plant.anonymous(105.0, 400)
    display_stats(ano)


def main():
    print("=== Garden statistics ===")
    check_year()
    test_rose()
    test_tree()
    test_vege()
    test_seed()
    test_anonymous()


if __name__ == "__main__":
    main()
