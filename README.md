# TriaTrack - Triathlon Training Tracker

TriaTrack is a command-line application for tracking and analyzing triathlon training sessions across three disciplines: swimming, cycling, and running.

## Features

- **Add Training Sessions**: Record workouts with distance, time, and heart rate data
- **Performance Scoring**: Automatic calculation of performance scores based on discipline-specific metrics
- **Statistics Analysis**: View aggregated statistics for your recent workouts
- **Multi-Discipline Support**: Track swimming, cycling, and running separately or combined
- **Performance Ratings**: Categorized performance levels from "Keep Going" to "Elite"

## Project Structure

```
TriaTrack/
│
├── main.py                 # Entry point of the application
├── menu_logic.py           # User interface and menu navigation
├── training_manager.py     # Training data management (CRUD operations)
├── utils.py                # Utility functions (validation, calculations)
├── constants.py            # Configuration constants and sport-specific factors
└── trainings.csv           # Data storage (auto-generated)
```

## Installation

1. Ensure you have Python 3.x installed on your system
2. Download all project files to a directory
3. No external dependencies required - uses only Python standard library

## Usage

### Starting the Application

Run the main program:
```bash
python main.py
```

### Main Menu

Upon starting, you'll see three options:

1. **Show stats** - View statistics for your training sessions
2. **Add new Training** - Record a new workout
3. **End Program** - Exit the application

### Adding a New Training

1. Select "Add new Training" from the main menu
2. Choose your discipline (swimming, cycling, or running)
3. Enter the following data:
   - Distance in kilometers
   - Training duration in minutes
   - Average heart rate (beats per minute)
4. The system automatically calculates:
   - Average pace (minutes per kilometer)
   - Performance score
   - Performance rating

### Viewing Statistics

1. Select "Show stats" from the main menu
2. Choose which discipline to analyze (or select "all workouts")
3. Specify how many of your most recent workouts to include
4. View aggregated statistics including:
   - Total distance covered
   - Average heart rate
   - Average pace
   - Average performance score
   - Total score across all sessions
   - Overall performance rating

## Performance Scoring System

TriaTrack uses discipline-specific formulas to calculate performance scores:

### Score Calculation

The score considers three factors:
- **Distance points**: Rewards longer distances
- **Pace factor**: Rewards faster speeds
- **Heart rate penalty**: Penalizes higher heart rates (indicating less efficiency)

Each discipline uses different multipliers optimized for that sport's characteristics.

### Performance Categories

| Score Range | Category |
|-------------|----------|
| 200+ | Elite |
| 150-199 | Excellent |
| 100-149 | Good |
| 60-99 | Average |
| 0-59 | Keep Going |

### Discipline-Specific Factors

**Swimming:**
- Emphasizes distance (80x multiplier)
- Moderate pace consideration (40x)
- Lower heart rate expectations (÷12)

**Running:**
- Balanced approach (15x distance)
- Strong pace emphasis (25x)
- Standard heart rate consideration (÷15)

**Cycling:**
- Lower distance multiplier (5x) due to longer typical distances
- Highest pace multiplier (15x)
- Most lenient heart rate expectation (÷18)

## Configuration Constants

The application uses centralized constants defined in `constants.py`:

### Available Workouts
```python
WORKOUTS = ["swimming", "cycling", "running"]
```
Defines the three supported triathlon disciplines.

### Main Menu Options
```python
MAIN_MENU = ["Show stats", "Add new Training", "End Program"]
```
The three primary functions accessible from the main menu.

### CSV Configuration
```python
TRAINING_FILE = "trainings.csv"
CSV_HEADER = ["type", "distance_km", "time_min", "avg_pulse", "avg_pace_min_per_km", "score"]
```
Defines the data storage file name and the structure of stored training data.

### Sport-Specific Factors
```python
SPORT_FACTORS = {
    "swimming": {
        "distance_multiplier": 80,
        "pace_multiplier": 40,
        "pulse_divisor": 12
    },
    "running": {...},
    "cycling": {...}
}
```
Each discipline has unique multipliers that reflect its characteristics. Swimming has the highest distance multiplier because pool distances are typically shorter. Cycling has the lowest distance multiplier but highest pace multiplier because cyclists cover longer distances at higher speeds.

### Score Categories
```python
SCORE_CATEGORIES = [
    (200, "Elite"),
    (150, "Excellent"),
    (100, "Good"),
    (60, "Average"),
    (0, "Keep Going")
]
```
Stored as tuples with minimum score thresholds and category names. The system checks from highest to lowest to assign the appropriate rating.

## Data Storage

Training data is stored in `trainings.csv` with the following structure:

```
type,distance_km,time_min,avg_pulse,avg_pace_min_per_km,score
running,5.0,25.0,150,5.0,95.5
```

The CSV file is automatically created on first use and appended with each new training session.

## Input Validation

The application includes comprehensive input validation:
- Only positive numerical values accepted for measurements
- Menu choices must be valid integers
- Automatic error handling for file operations
- Graceful handling of invalid CSV data

## Error Handling

- **File Not Found**: Creates new file automatically
- **Permission Errors**: Displays clear error messages
- **Invalid Input**: Prompts user to re-enter correct data
- **Keyboard Interrupt**: Allows clean program termination

## Technical Notes

- Encoding: UTF-8 for international character support
- CSV delimiter: Comma (,)
- Decimal separator: Period (.)
- All calculations rounded to 2 decimal places

## Troubleshooting

**Issue**: "File has not been found" message
- **Solution**: This is normal on first run; the file will be created automatically

**Issue**: Invalid score calculations
- **Solution**: Verify that distance, time, and heart rate are entered correctly

**Issue**: Cannot write to file
- **Solution**: Check that you have write permissions in the program directory