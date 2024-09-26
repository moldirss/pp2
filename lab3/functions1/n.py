# main.py
from conversions import grams_to_ounces, fahrenheit_to_centigrade
from puzzles import solve, filter_prime
from spy_games import has_33, spy_game

# Example function calls:
print(grams_to_ounces(100))  # Convert grams to ounces
print(fahrenheit_to_centigrade(98))  # Convert Fahrenheit to Centigrade
print(solve(35, 94))  # Solve chickens and rabbits puzzle
print(filter_prime([2, 3, 4, 5, 6, 7]))  # Filter prime numbers
print(has_33([1, 3, 3]))  # Check for 33 in list
print(spy_game([1, 0, 2, 0, 7]))  # Check for 007 sequence
