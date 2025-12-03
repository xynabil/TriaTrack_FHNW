import csv
WORKOUTS = ["swimming", "cycling", "running"]

def print_new_training_menu():
    print("-" * 40)
    print("\nAdd new training")
    print("-" * 40)


def new_training_menu_logic():
    print_new_training_menu()
    i = 1
    for workout in WORKOUTS:
        print(f"{i}) {workout} ")
        i += 1

    while True:
        try:
            choice_training = int(input("Choose training: "))
        except ValueError:
            print("Please enter a number.")
            continue

        if 1 <= choice_training <= len(WORKOUTS):
            idx = choice_training - 1
            print("-" * 40)
            print(f"\nCreating new {WORKOUTS[idx]} workout")
            print("-" * 40)
            add_training(WORKOUTS[idx])
            break
        else:
            print("Invalid input")


def get_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
            else:
                print("Please enter a correct number.")
        except ValueError:
            print("Please enter a number.")







def input_training_data():
    distance = get_positive_float("Distance accomplished (in km): ")
    time = get_positive_float("Time needed in minutes: ")
    pulse = get_positive_float("Average pulse: ")

    avg_speed = distance / (time / 60)

    return distance, time, pulse, avg_speed


def add_training(training_type):
    training_data = input_training_data()

    try:
        with open("trainings.csv", "a", newline='') as file:
            writer = csv.writer(file)
            writer.writerow([
                training_type,
                round(training_data[0], 2),  # distance
                round(training_data[1], 2),  # time
                round(training_data[2], 2),  # pulse
                round(training_data[3], 2)   # avg_speed
            ])
        print(f"\nSuccessfully added {training_type}-training of {training_data[0]} km.")
        print("-" * 70)
        input("Press ENTER to continue...")
    except IOError as e:
        print(f"Error while saving: {e}")
        print("-" * 70)
        input("Press ENTER to continue...")
