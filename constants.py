# Verfügbare Trainingsarten
WORKOUTS = ["swimming", "cycling", "running"]

# Hauptmenü-Optionen
MAIN_MENU = ["Show stats", "Add new Training", "End Program"]

# CSV Dateiname
TRAINING_FILE = "trainings.csv"

# CSV Header als 
CSV_HEADER = ["type", "distance_km", "time_min", "avg_pulse", "avg_pace_min_per_km", "score"]

# Disziplin spezifische Faktoren als Dictionary
SPORT_FACTORS = {
    "swimming": {
        "distance_multiplier": 200,
        "pace_multiplier": 20,
        "pulse_divisor": 12
    },
    "running": {
        "distance_multiplier": 15,
        "pace_multiplier": 30,
        "pulse_divisor": 15
    },
    "cycling": {
        "distance_multiplier": 5,
        "pace_multiplier": 40,
        "pulse_divisor": 18
    }
}

# Score Kategorisierung als Tupel
SCORE_CATEGORIES = [
    (200, "Elite"),
    (150, "Excellent"),
    (100, "Good"),
    (60, "Average"),
    (0, "Keep Going")
]
