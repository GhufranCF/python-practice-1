from sort_dictionaries import sort_dictionaries
from weather.weather import get_weather
print("Testing for Dictionary Function:\n")
people = [
    {"name": "Alice", "age": 30, "roll_no":"003"},
    {"name": "Bob", "age": 25, "roll_no": "001"},
    {"name": "Charlie", "age": 35, "roll_no": "027"},
]

print(sort_dictionaries(people, "age"))
print(sort_dictionaries(people, "roll_no"))
print(sort_dictionaries(people, "marks"))


print("\n\nTesting for Weather Function:\n")

print(get_weather("New York"))
print(get_weather("Karachi"))
print(get_weather("Lahore"))
print(get_weather("No city"))

