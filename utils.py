from constants import *

def get_positive_float(prompt):
    # Validierung für positive Float-Werte
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
            else:
                print("Please enter a correct number.")
        except ValueError:
            print("Please enter a number.")


def calculate_score(distance, time, pulse, training_type):
    # Berechnet Score mit Disziplin-Konstanten

    factors = SPORT_FACTORS.get(training_type, SPORT_FACTORS["running"])

    pace_factor = (distance / time) * factors["pace_multiplier"]
    distance_points = distance * factors["distance_multiplier"]
    pulse_penalty = pulse / factors["pulse_divisor"]

    score = distance_points + pace_factor - pulse_penalty
    return round(score, 2)


def get_score_category(score):
    # Ratet den Score anhand den Konstanten

    for min_score, category in SCORE_CATEGORIES:
        if score >= min_score:
            return category
