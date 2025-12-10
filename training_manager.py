import csv
from constants import TRAINING_FILE, CSV_HEADER
from utils import get_positive_float, calculate_score, get_score_category


def input_training_data():
    # Asks for training data via get_positive_float
    distance = get_positive_float("Distance accomplished (in km): ")
    time = get_positive_float("Time needed in minutes: ")
    pulse = get_positive_float("Average pulse: ")

    # Calculate Pace (min/km)
    avg_pace = time / distance

    return distance, time, pulse, avg_pace

def add_training(training_type):
    # Stores user input into list training_data
    training_data = input_training_data()

    # Calculates score with based on training type
    score = calculate_score(training_data[0], training_data[1], training_data[2], training_type)

    try:
        # Checks if file exists and has content or not
        file_exists = False
        file_empty = True

        try:
            with open(TRAINING_FILE, "r", encoding='utf-8') as f:
                file_exists = True
                first_line = f.readline()
                if first_line.strip():
                    file_empty = False
        except FileNotFoundError:
            print("File has not been found.")
        except PermissionError:
            print("No Permissions to read training data")

        # Opens csv in append-mode
        with open(TRAINING_FILE, "a", newline='', encoding='utf-8') as file:
            writer = csv.writer(file)

            # Only write header when file is new or empty
            if not file_exists or file_empty:
                writer.writerow(CSV_HEADER)

            # Trainingsdaten als neue Zeile hinzufügen
            writer.writerow([
                training_type,
                training_data[0],  # distance
                training_data[1],  # time
                training_data[2],  # pulse
                training_data[3],  # avg_pace
                score
            ])

        print(f"\nSuccessfully added {training_type}-training of {training_data[0]} km.")
        print(f"Your score for this training: {score} points")
        print(f"Performance rating: {get_score_category(score)}")

    except PermissionError:
        print("Error: No permission to write to file. Check file permissions.")
    except OSError as e:
        print(f"Error while saving: {e}")
    finally:
        print("-" * 70)
        input("Press ENTER to continue...")


def load_training(workout_type, time_span):
    # Loads Trainingdata from csv
    total_distance = 0.0
    sum_pulse = 0.0
    sum_pace = 0.0
    sum_score = 0.0
    counter = 0

    try:
        with open(TRAINING_FILE, "r", newline='', encoding='utf-8') as file: # utf-8 for üäö to be read
            reader = csv.reader(file) # csv.reader object created into reader variable
            print("Reading training data...")

            # Skip header
            next(reader, None)

            # Iterates through each row
            for row in reader:
                # If counter has been reached --> break
                if counter >= time_span:
                    break

                # Check, if there are not exactly 6 entries --> skip row
                if len(row) != 6:
                    continue

                try:
                    discipline = row[0]
                    distance = float(row[1])
                    time_val = float(row[2])
                    pulse = float(row[3])
                    avg_pace = float(row[4])
                    score = float(row[5])
                except (ValueError, IndexError): # Except for unexpected values and/or indexerror
                    continue

                # Analyse all trainings or only specific discipline
                if workout_type == "all" or discipline == workout_type:
                    total_distance += distance
                    sum_pulse += pulse
                    sum_pace += avg_pace
                    sum_score += score
                    counter += 1

    except FileNotFoundError:
        print("No trainings file found.")
        return None
    except PermissionError:
        print("Error: No permission to read file. Check file permissions.")
        return None
    except OSError as e:
        print(f"Error while loading: {e}")
        return None

    return {
        'counter': counter,
        'total_distance': total_distance,
        'sum_pulse': sum_pulse,
        'sum_pace': sum_pace,
        'sum_score': sum_score
    }


def display_training_stats(workout_type, stats):
    # Shows stats
    if stats is None:
        return

    counter = stats['counter']

    if counter > 0:
        workout_display = "all" if workout_type == "all" else workout_type # When workout_type equals "all" store into workout_display
        # Calculate avg
        avg_pulse = stats['sum_pulse'] / counter
        avg_pace = stats['sum_pace'] / counter
        avg_score = stats['sum_score'] / counter

        print(f"\nDisplaying your stats for the last {counter} {workout_display}-training(s)")
        print("-" * 70)
        print(f"Total distance: {stats['total_distance']:.2f} KM")
        print(f"Average pulse: {avg_pulse:.2f} Beats per Minute")
        print(f"Average pace: {avg_pace:.2f} Minutes per KM")
        print(f"Average score: {avg_score:.2f} points")
        print(f"Average performance rating: {get_score_category(avg_score)}")
        print(f"Total score: {stats['sum_score']:.2f} points")
    else:
        print(f"\nNo {workout_type} trainings found.")

    print("-" * 70)
    input("Press Enter to continue...")