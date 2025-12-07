from constants import WORKOUTS, MAIN_MENU
from training_manager import add_training, load_training, display_training_stats


def print_main_menu():
    # Printet das Hauptmenü
    i = 1
    print("\nWelcome to TriaTrack, your tracker for all your triathletic workouts")
    print("-" * 70)
    for menu_point in MAIN_MENU:
        print(f"{i}) {menu_point}")
        i += 1
    print("-" * 70)


def main_menu_logic():
    # Logik für das Main Menü
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
    # Zeigt Menü für neue Trainings an
    print("-" * 40)
    print("\nAdd new training")
    print("-" * 40)


def new_training_menu_logic():
    # Logik für hinzufügen neues Training
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


def print_stats_menu():
    # Zeigt das Statistik-Menü an
    i = 1
    print("\nWhich Stats would you like to show?")
    print("-" * 70)
    for workout in WORKOUTS:
        print(f"{i}) Show {workout} workouts")
        i += 1
    print(f"{i}) Show all workouts")
    print("-" * 70)


def stats_menu_logic():
    # Logik für die Statistik-Anzeige
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
    # Zeigt den Header für Zeitspannen-Analyse an
    print("\nWorkout Analyser")
    print("-" * 70)


def stats_menu_timespan_logic(workout_type):
    # Logik für die Auswahl der Zeitspanne
    while True:
        try:
            time_span = int(input("How many of your last workouts do you want to analyse: "))
            if time_span > 0:
                stats = load_training(workout_type, time_span)
                display_training_stats(workout_type, stats)
                break
            else:
                print("Invalid input")
        except ValueError:
            print("Please enter a number.")