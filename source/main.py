from cow import Cow
from sheep import Sheep
from chicken import Chicken
from utils import *
import pprint


def main() -> None:
    farm = {
        "Chicken": Chicken(weight=1, growth_rate=0.1, food_need=1, water_need=1, name="Steve"),
        "Cow": Cow(weight=1000, growth_rate=50, food_need=30, water_need=30, name="John"),
        "Sheep": Sheep(weight=150, growth_rate=10, food_need=15, water_need=15, name="Qasim")
    }

    non_stop = True
    
    while non_stop:
        print()
        print("Your options:")
        print("1. Report about your farm")
        print("2. Grow an animal in your farm")
        print("3. Slaughter an animal in your farm")
        print("0. Quit")
        print("")

        option = input_int(message="Your choice (0-3): ", error_message="Please, enter a valid option", predicate=lambda value: 0 <= value <= 3)

        match option:
            case 1:
                for animal in farm:
                    pprint.pprint(farm[animal].report())
                    print()
            case 2:
                print("Which animal you want to grow?")
                for animal in farm:
                    if farm[animal].report()["_status"] != "Dead":
                        print(farm[animal]._type)
                
                print()

                choice = str.title(input_str(message="Your choice: ", error_message="Please, enter a valied choice", predicate=lambda animal: str.title(animal) in farm.keys()))

                water = input_int(message="Water need: ", error_message="Please, enter a valid value", predicate=lambda value: value >= 0)
                food = input_int(message="Food need: ", error_message="Please, enter a valid value", predicate=lambda value: value >= 0)
                
                farm[choice].grow(food=food, water=water)
            case 3:
                print("Which animal you want to slaughter?")
                for animal in farm:
                    if farm[animal].report()["_status"] != "Dead":
                        print(farm[animal]._type)
                
                choice = str.title(input_str(message="Your choice: ", error_message="Please, enter a valied choice", predicate=lambda animal: str.title(animal) in farm.keys()))

                print()           
                farm[choice].slaughter()
                farm.pop(choice)
            case 0:
                non_stop = False

    
    print("Thank you for using our program")



if __name__ == "__main__":
    main()
