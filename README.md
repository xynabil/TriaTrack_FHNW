# TriaTrack

A simple command-line tracker for triathlon workouts (swimming, cycling, running).

## Features

- Track swimming, cycling, and running workouts
- Sport-specific performance scoring that accounts for different difficulty levels
- View statistics for individual disciplines or all workouts combined
- Data stored locally in CSV format

## Installation

No external dependencies required - uses only Python standard library.

**Requirements:**
- Python 3.6 or higher

## Usage

Run the program:
```bash
python main.py
```

### Main Menu Options

1. **Show stats** - View your training statistics
2. **Add new Training** - Log a new workout
3. **End Program** - Exit

### Adding a Workout

1. Select training type (swimming, cycling, or running)
2. Enter distance in kilometers
3. Enter time in minutes
4. Enter average pulse (heart rate)

The program automatically calculates your pace and performance score.

### Viewing Stats

- Choose a specific discipline or view all workouts
- Select how many recent workouts to analyze
- See total distance, average pulse, average pace, and scores

## File Structure

```
├── main.py              # Program entry point
├── constants.py         # Configuration and sport-specific factors
├── menu_logic.py        # Menu navigation and UI
├── training_manager.py  # Data handling and CSV operations
├── utils.py             # Utility functions (validation, scoring)
└── trainings.csv        # Data file (created automatically)
```

## Data Storage

All workout data is saved in `trainings.csv` in the same directory as the program.

## Score Calculation

Your workout score is calculated using **sport-specific factors** that account for the different nature of each discipline:

### Scoring Factors

**Swimming** (50 points/km)
- Highest points per kilometer (swimming is the hardest)
- Lower pulse penalty (swimming naturally has lower heart rate)

**Running** (15 points/km)
- Moderate difficulty scoring
- Balanced pace and pulse factors

**Cycling** (5 points/km)
- Lowest points per kilometer (you cover more distance)
- Higher pace bonus (speed matters more)
- Lower pulse penalty (higher heart rates are normal)

### Formula
```
Score = (Distance × Sport Factor) + (Speed × Pace Factor) - (Pulse ÷ Pulse Factor)
```

This ensures that a 2 km swim, 10 km run, and 40 km bike ride are scored fairly relative to their actual effort and difficulty.

---

*Happy training! 🏊 🚴 🏃*