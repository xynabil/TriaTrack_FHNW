# Verfügbare Trainingsarten
WORKOUTS = ["swimming", "cycling", "running"]

# Hauptmenü-Optionen
MAIN_MENU = ["Show stats", "Add new Training", "End Program"]

# CSV Dateiname
TRAINING_FILE = "trainings.csv"

# CSV Header
CSV_HEADER = ["type", "distance_km", "time_min", "avg_pulse", "avg_pace_min_per_km", "score"]

# Disziplin-Spezifische Faktoren
SPORT_FACTORS = {
    "swimming": {
        "distance_multiplier": 50,
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