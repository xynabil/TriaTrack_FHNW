from menu_logic import *


WORKOUTS = ["swimming", "cycling", "running"]
MAIN_MENU = ["Show stats", "Add new Training", "End Program"]


def print_main_menu():
    i = 1
    print("\nWelcome to TriaTrack, your tracker for all your triathletic workouts")
    print("-" * 70)
    for menu_point in MAIN_MENU:
        print(f"{i}) {menu_point}")
        i += 1
    print("-" * 70)


def main():
    main_menu_logic()


def main_menu_logic():
    while True:
        print_main_menu()
        try:
            choice_menu = int(input("Choose function: "))
        except ValueError:
            print("Please enter a number.")
            print("-" * 70)
            continue
        if choice_menu == 1:
            stats_menu_logic()
        elif choice_menu == 2:
            new_training_menu_logic()
        elif choice_menu == 3:
            break
        else:
            print("Invalid choice")
            print("-" * 70)
    print("Program ended")


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
        with open("trainings.txt", "a") as datei:
            datei.write(f"{training_type}\n")
            datei.write(f"{training_data[0]}\n")  # distance
            datei.write(f"{training_data[1]}\n")  # time
            datei.write(f"{training_data[2]}\n")  # pulse
            datei.write(f"{training_data[3]}\n")  # avg_speed
        print(f"\nSuccessfully added {training_type}-training of {training_data[0]} km.")
        print("-" * 70)
        input("Press ENTER to continue...")
    except FileNotFoundError:
        print("No trainings file found.")
        print("-" * 70)
        input("Press ENTER to continue...")
    except IOError as e:
        print(f"Error while saving: {e}")
        print("-" * 70)
        input("Press ENTER to continue...")


def print_stats_menu():
    i = 1
    print("\nWhich Stats would you like to show?")
    print("-" * 70)
    for workout in WORKOUTS:
        print(f"{i}) Show {workout} workouts")
        i += 1
    print(f"{i}) Show all workouts")
    print("-" * 70)


def stats_menu_logic():
    print_stats_menu()

    while True:
        try:
            choice_stats = int(input("Which Stats would you like to show?: "))
        except ValueError:
            print("Please enter a number.")
            continue

        if 1 <= choice_stats <= len(WORKOUTS):
            idx = choice_stats - 1
            print("-" * 70)
            print_stats_menu_time_span()
            stats_menu_timespan_logic(WORKOUTS[idx])
            break
        elif choice_stats == len(WORKOUTS) + 1:
            print("-" * 70)
            print_stats_menu_time_span()
            stats_menu_timespan_logic("all")
            break
        else:
            print("Invalid input")


def print_stats_menu_time_span():
    print("\nWorkout Analyser")
    print("-" * 70)


def stats_menu_timespan_logic(workout_type):
    while True:
        try:
            time_span = int(input("How many of your last workouts do you want to analyse: "))
            if time_span > 0:
                load_training(workout_type, time_span)
                break
            else:
                print("Invalid input")
        except ValueError:
            print("Please enter a number.")


def load_training(workout_type, time_span):
    total_distance = 0.0
    sum_pulse = 0.0
    sum_speed = 0.0
    counter = 0

    try:
        with open("trainings.txt", "r") as file:
            print("Reading training data...")
            while counter < time_span:
                discipline = file.readline()
                if discipline == "":
                    break
                discipline = discipline.strip()

                distance_line = file.readline()
                time_line = file.readline()
                pulse_line = file.readline()
                speed_line = file.readline()

                try:
                    distance = float(distance_line.strip())
                    time_val = float(time_line.strip())
                    pulse = float(pulse_line.strip())
                    avg_speed = float(speed_line.strip())
                except ValueError:
                    continue

                # Check if we want all workouts or specific type
                if workout_type == "all" or discipline == workout_type:
                    total_distance += distance
                    sum_pulse += pulse
                    sum_speed += avg_speed
                    counter += 1

    except FileNotFoundError:
        print("No trainings file found.")
        print("-" * 70)
        input("Press Enter to continue...")
        return
    except IOError as e:
        print(f"Error while loading: {e}")
        print("-" * 70)
        input("Press Enter to continue...")
        return

    display_training_stats(workout_type, counter, total_distance, sum_pulse, sum_speed)


def display_training_stats(workout_type, counter, total_distance, sum_pulse, sum_speed):
    if counter > 0:
        workout_display = "all" if workout_type == "all" else workout_type
        avg_pulse = sum_pulse / counter
        avg_speed = sum_speed / counter

        print(f"\nDisplaying your stats for the last {counter} {workout_display}-training(s)")
        print("-" * 70)
        print(f"Total distance: {total_distance:.2f} KM")
        print(f"Average pulse: {avg_pulse:.2f} Beats per Minute")
        print(f"Average speed: {avg_speed:.2f} KM/H")
    else:
        print(f"\nNo {workout_type} trainings found.")

    print("-" * 70)
    input("Press Enter to continue...")


main()