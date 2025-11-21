# Mp3-repo

This project is a simple MP3 player designed to play five songs located in the `Music` folder. The player is built using Python and utilizes the `os` and `pygame` libraries for its functionality.

## Features

- Plays five MP3 songs from the `Music` directory.
- User-friendly script for basic music playback.
- Easy set across all platforms (Windows, MacOS and Linux)
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
├── main.py           # Main program to run the MP3 player
├── Music/            # Folder containing your five songs
├── README.md         # This project documentation
└── .gitattributes
```



## Acknowledgments

- Built with [pygame](https://www.pygame.org/).
- Guide instructed by https://youtu.be/xf71dRBRP6o?si=C6AUA0rakoAMovEW
