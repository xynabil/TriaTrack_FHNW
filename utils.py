from constants import *

def get_positive_float(prompt):
    # Validate user inputs to get positive float
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
            else:
                print("Please enter a correct number.")
        except ValueError:
            print("Please enter a number.")
        except KeyboardInterrupt:
            print("\nProgram terminated.!")


def calculate_score(distance, time, pulse, training_type):
    # Calculates Score based on discipline

    factors = SPORT_FACTORS.get(training_type, SPORT_FACTORS["running"]) # If no valid training type = take factor for running

    pace_factor = (distance / time) * factors["pace_multiplier"]
    distance_points = distance * factors["distance_multiplier"]
    pulse_penalty = pulse / factors["pulse_divisor"]

    score = distance_points + pace_factor - pulse_penalty
    return round(score, 2)


def get_score_category(score):
    # Puts score store into a category

    for min_score, category in SCORE_CATEGORIES: # Unpacks Tupel into variables
        if score >= min_score:
            return category