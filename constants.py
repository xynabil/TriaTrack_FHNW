# Available Disciplines
WORKOUTS = ["swimming", "cycling", "running"]

# Main-Menu options
MAIN_MENU = ["Show stats", "Add new Training", "End Program"]

# CSV Filename
TRAINING_FILE = "trainings.csv"

# CSV Header
CSV_HEADER = ["type", "distance_km", "time_min", "avg_pulse", "avg_pace_min_per_km", "score"]

# Discipline Factors
SPORT_FACTORS = {
    "swimming": {
        "distance_multiplier": 80,
        "pace_multiplier": 40, # highest (slowest pace IR)
        "pulse_divisor": 12
    },
    "running": {
        "distance_multiplier": 15,
        "pace_multiplier": 25, # middle (middle pace IR)
        "pulse_divisor": 15
    },
    "cycling": {
        "distance_multiplier": 5,
        "pace_multiplier": 15, # lowest (fastest pace IR)
        "pulse_divisor": 18
    }
}

# Scare Categories
SCORE_CATEGORIES = [
    (200, "Elite"),
    (150, "Excellent"),
    (100, "Good"),
    (60, "Average"),
    (0, "Keep Going")
]