# GlobalTracker

GlobalTracker is a Python program designed to schedule sleep and wake times for a Windows system. This helps in saving energy and enhancing the longevity of your computer by ensuring it is not unnecessarily active when not in use.

## Features

- Automatically puts the system to sleep at a specified hour.
- Wakes the system at a specified hour.
- Designed to run continuously to manage sleep schedules.
  
## Requirements

- Windows operating system.
- Python 3.x

## Installation

1. Clone the repository or download the `global_tracker.py` file.
2. Ensure Python is installed on your Windows machine.

## Usage

1. Open a command prompt and navigate to the directory containing `global_tracker.py`.
2. Run the script using Python:

   ```bash
   python global_tracker.py
   ```

3. By default, the system is set to sleep at 11 PM and wake at 7 AM. You can modify these settings by changing the `sleep_hour` and `wake_hour` parameters in the script.

## Important Notes

- The script uses Windows API calls to put the system to sleep.
- Waking the system is typically handled by BIOS settings or scheduled tasks in Windows, and the script assumes the system will wake up based on these settings.
- Ensure that your system's power settings allow for sleep mode to be activated and woken as expected.

## Contributing

Feel free to submit issues or pull requests if you have suggestions for improvements or additional features.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.