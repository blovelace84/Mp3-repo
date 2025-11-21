# Mp3-repo

This project is a simple MP3 player designed to play five songs located in the `Music` folder. The player is built using Python and utilizes the `os` and `pygame` libraries for its functionality.

## Features

- Plays MP3 songs from the `Music` directory.
- User-friendly script for basic music playback.
- Easy setup across all platforms (Windows, MacOS and Linux)
- **NEW:** Automatic song completion detection - returns to menu when song ends
- **NEW:** Proper resource management - prevents memory leaks
- **NEW:** Enhanced pause/resume controls with state validation
- **NEW:** Comprehensive unit tests and documentation
## Requirements

- Python 3.11
- pip (Python package installer)

The following Python libraries are used:
- `pygame`  
- `os` (standard library)

## Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/blovelace84/Mp3-repo.git
    cd Mp3-repo
    ```

2. **(Optional) Create a virtual environment:**

    ```sh
    python -m venv venv
    source venv/bin/activate      # On macOS/Linux
    .\venv\Scripts\activate       # On Windows
    ```

3. **Install dependencies:**

    ```sh
    pip install pygame
    ```

## Usage

1. Place your mp3 files (named as needed for the script; typically five songs) in the `Music` directory.

2. Run the player with:

    ```sh
    python main.py
    ```

3. Follow on-screen prompts for playback control (if applicable).

## Project Structure

```
Mp3-repo/
│
├── main.py                  # Main program to run the MP3 player (optimized)
├── Music/                   # Folder containing your songs
├── test_main.py             # Unit tests for the MP3 player
├── README.md                # This project documentation
├── OPTIMIZATION_REPORT.md   # Detailed performance optimization report
├── SUMMARY.md               # Before/after code comparison
├── .gitignore               # Git ignore rules for Python
└── .gitattributes
```

## Performance Optimizations

This MP3 player has been optimized for better performance and reliability:

1. **Smart Loop Exit** - Automatically exits playback loop when song finishes
2. **Resource Cleanup** - Proper pygame cleanup prevents memory leaks
3. **Event Detection** - Detects natural song completion and returns to menu
4. **State Validation** - Robust pause/resume with clear user feedback
5. **Code Quality** - PEP 8 compliant, fully tested, documented

See `OPTIMIZATION_REPORT.md` for detailed analysis of all improvements.

## Testing

Run the test suite with:

```sh
python -m unittest test_main.py -v
```

All 7 tests should pass successfully.



## Acknowledgments

- Built with [pygame](https://www.pygame.org/).
- Guide instructed by https://youtu.be/xf71dRBRP6o?si=C6AUA0rakoAMovEW
