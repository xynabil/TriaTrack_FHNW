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
   # Berechnet Score für Training mit Disziplin-Spezifischen Faktoren aus den Konstanten
    from constants import SPORT_FACTORS

    factors = SPORT_FACTORS.get(training_type, SPORT_FACTORS["running"]) # Sollte ein Falscher Training Type vorhanden sein wird Running genommen

    pace_factor = (distance / time) * factors["pace_multiplier"]
    distance_points = distance * factors["distance_multiplier"]
    pulse_penalty = pulse / factors["pulse_divisor"]

    score = distance_points + pace_factor - pulse_penalty # Berechnung des Scores
    return round(score, 2)