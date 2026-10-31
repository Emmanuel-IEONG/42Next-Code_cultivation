class Plant:
    "Plant informations"

    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.daily_age = age

    def show(self):
        print(f"{self.name.capitalize()}: {self.height}cm,"
              f" {self.daily_age} days old")

    def age(self):
        self.daily_age += 1

    def grow(self):
        daily_growth = 0.8
        week = 7
        for days in range(week + 1):
            if (days == 0):
                print("=== Garden Plant Growth ===")
                print(f"{self.name.capitalize()}: "
                      f"{round(self.height, 1)}cm, {self.daily_age} days old")
            else:
                self.height += daily_growth
                self.age()
                print(f"=== Day {days} ===")
                print(f"{self.name.capitalize()}: "
                      f"{round(self.height, 1)}cm, {self.daily_age} days old")
        print(f"Growth this week: {round(daily_growth * week, 1)}cm")


def main():
    rose = Plant('rose', 25.0, 30)
    rose.grow()


if __name__ == "__main__":
    main()
