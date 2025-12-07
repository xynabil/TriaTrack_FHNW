import csv
from constants import TRAINING_FILE, CSV_HEADER
from utils import get_positive_float, calculate_score


def input_training_data():
    # Abfragen der Trainingsdaten über die get_positive_float funktion
    distance = get_positive_float("Distance accomplished (in km): ")
    time = get_positive_float("Time needed in minutes: ")
    pulse = get_positive_float("Average pulse: ")

    # Pace berechnen (Minuten pro Kilometer)
    avg_pace = time / distance

    return distance, time, pulse, avg_pace


def add_training(training_type):
    # Adden von Training in csv
    training_data = input_training_data()

    # Score berechnen (mit Trainingstyp)
    score = calculate_score(training_data[0], training_data[1], training_data[2], training_type)

    try:
        # Prüfen, ob die Datei bereits existiert und Inhalt hat
        file_exists = False
        file_empty = True
        try:
            with open(TRAINING_FILE, "r") as f:
                file_exists = True
                # Erste Zeile lesen um zu prüfen, ob Datei leer ist
                first_line = f.readline()
                if first_line.strip():
                    file_empty = False
        except FileNotFoundError:
            pass

        # Datei im Anfüge-Modus öffnen
        with open(TRAINING_FILE, "a", newline='') as file:
            writer = csv.writer(file)

            # Header nur schreiben, wenn Datei neu oder leer ist
            if not file_exists or file_empty:
                writer.writerow(CSV_HEADER)

            # Trainingsdaten als neue Zeile hinzufügen
            writer.writerow([
                training_type,
                training_data[0],  # distance
                training_data[1],  # time
                training_data[2],  # pulse
                training_data[3],  # avg_pace
                score  # score
            ])
        print(f"\nSuccessfully added {training_type}-training of {training_data[0]} km.")
        print(f"Your score for this training: {score} points")
        print("-" * 70)
        input("Press ENTER to continue...")
    except IOError as e:
        print(f"Error while saving: {e}")
        print("-" * 70)
        input("Press ENTER to continue...")


def load_training(workout_type, time_span):
    # Lädt Trainingsdaten aus der CSV-Datei
    total_distance = 0.0
    sum_pulse = 0.0
    sum_pace = 0.0
    sum_score = 0.0
    counter = 0

    try:
        with open(TRAINING_FILE, "r", newline='') as file:
            reader = csv.reader(file)
            print("Reading training data...")

            # Header-Zeile überspringen
            next(reader, None)

            # Durch alle Trainingszeilen iterieren
            for row in reader:
                # Maximale Anzahl erreicht?
                if counter >= time_span:
                    break

                # Sicherheitsprüfung: Zeile muss genau 6 Spalten haben
                if len(row) != 6:
                    continue

                try:
                    discipline = row[0]
                    distance = float(row[1])
                    time_val = float(row[2])
                    pulse = float(row[3])
                    avg_pace = float(row[4])
                    score = float(row[5])
                except (ValueError, IndexError):
                    continue

                # Prüfen, ob wir alle Trainings oder nur eine bestimmte Art wollen
                if workout_type == "all" or discipline == workout_type:
                    total_distance += distance
                    sum_pulse += pulse
                    sum_pace += avg_pace
                    sum_score += score
                    counter += 1

    except FileNotFoundError:
        print("No trainings file found.")
        print("-" * 70)
        input("Press Enter to continue...")
        return None
    except IOError as e:
        print(f"Error while loading: {e}")
        print("-" * 70)
        input("Press Enter to continue...")
        return None

    return {
        'counter': counter,
        'total_distance': total_distance,
        'sum_pulse': sum_pulse,
        'sum_pace': sum_pace,
        'sum_score': sum_score
    }


def display_training_stats(workout_type, stats):
    # Zeigt die Trainingsstatistiken an
    if stats is None:
        return

    counter = stats['counter']

    if counter > 0:
        workout_display = "all" if workout_type == "all" else workout_type
        # Durchschnittswerte berechnen
        avg_pulse = stats['sum_pulse'] / counter
        avg_pace = stats['sum_pace'] / counter
        avg_score = stats['sum_score'] / counter

        print(f"\nDisplaying your stats for the last {counter} {workout_display}-training(s)")
        print("-" * 70)
        print(f"Total distance: {stats['total_distance']:.2f} KM")
        print(f"Average pulse: {avg_pulse:.2f} Beats per Minute")
        print(f"Average pace: {avg_pace:.2f} Minutes per KM")
        print(f"Average score: {avg_score:.2f} points")
        print(f"Total score: {stats['sum_score']:.2f} points")
    else:
        print(f"\nNo {workout_type} trainings found.")

    print("-" * 70)
    input("Press Enter to continue...")