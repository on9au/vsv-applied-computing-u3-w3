"""Task 3a: Write a function that contains a match statement that returns the correct message for that choice."""

ROOT = "Here is your"

# Approach 1: Strings and match case
def respond_to_order_str(drink: str) -> str:
    match drink.lower():
        case "lemonade":
            return ROOT + " lemonade"
        case "orange squash":
            return ROOT + " orange squash"
        case "cola":
            return ROOT + " cola"
        case "ginger beer":
            return ROOT + " ginger beer"
        case _:
            raise ValueError("Invalid drink")

# Test cases
print(respond_to_order_str("lemonade"))
print(respond_to_order_str("orange squash"))
print(respond_to_order_str("cola"))
print(respond_to_order_str("ginger beer"))

# Error case
try:
    print(respond_to_order_str("water")) # Error
except ValueError as e:
    print(e)

# ====================================================================================================

# Another unrelated approach: Using enums

# Unrelated to the task, but representing the drinks as an enum is a good idea.
# definitely not because i'm a rust programmer and i'm used to enums

from enum import Enum, auto

# I dislike using magic numbers or strings in code, so I use enums to represent them.
class Drink(Enum):
    LEMONADE = auto()
    ORANGE_SQUASH = auto()
    COLA = auto()
    GINGER_BEER = auto()
    
    # Enum variant to string
    def __str__(self) -> str:
        return self.name.lower().replace("_", " ")

def respond_to_order_enum(drink: Drink) -> str:
    if not isinstance(drink, Drink):
        raise ValueError("Invalid drink") # error as string for simplicity
    return f"{ROOT} {drink}" # using same ROOT as above

# # Test cases
# print(respond_to_order_enum(Drink.LEMONADE))
# print(respond_to_order_enum(Drink.ORANGE_SQUASH))
# print(respond_to_order_enum(Drink.COLA))
# print(respond_to_order_enum(Drink.GINGER_BEER))

# # Error case
# try:
#     print(respond_to_order_enum("water")) # Error
# except ValueError as e:
#     print(e)