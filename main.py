import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
import pygame  # noqa: E402
import time  # noqa: E402


def play_music(folder, song_name):
    """Play an MP3 file with pause, resume, and stop controls.

    Args:
        folder: Directory containing the music file
        song_name: Name of the MP3 file to play
    """
    file_path = os.path.join(folder, song_name)

    if not os.path.exists(file_path):
        print("File not found!")
        return

    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

    # Set up music end event to detect when song finishes naturally
    pygame.mixer.music.set_endevent(pygame.USEREVENT)

    print(f"\nNow playing: {song_name}")
    print("Commands: [P]ause, [R]esume, [S]top")

    is_paused = False

    while pygame.mixer.music.get_busy() or is_paused:
        # Process pygame events to check for music end
        for event in pygame.event.get():
            if event.type == pygame.USEREVENT:
                print("\nSong finished!")
                return

        command = input("> ").strip().upper()

        if command == "P":
            if not is_paused:
                pygame.mixer.music.pause()
                is_paused = True
                print("Paused")
            else:
                print("Already paused")
        elif command == "R":
            if is_paused:
                pygame.mixer.music.unpause()
                is_paused = False
                print("Resumed")
            else:
                print("Not paused")
        elif command == "S":
            pygame.mixer.music.stop()
            print("Stopped")
            return
        elif command:
            print("Invalid command. Use [P]ause, [R]esume, or [S]top")

        # Small delay to prevent excessive CPU usage when music is playing
        time.sleep(0.05)


def main():
    """Main function to run the MP3 player with menu interface."""
    try:
        pygame.mixer.init()
        pygame.init()  # Initialize pygame for event handling
    except pygame.error as e:
        print("Audio initialization failed!", e)
        return

    folder = "Music"

    if not os.path.isdir(folder):
        print(f"Folder '{folder}' not found")
        return

    try:
        mp3_files = [file for file in os.listdir(folder) if file.endswith(".mp3")]

        if not mp3_files:
            print("No .mp3 files found!")
            return

        # Cache the formatted menu to avoid repeated string operations
        menu_header = "*****MP3 PLAYER******\nMy song list:"

        while True:
            # Display menu efficiently
            print(menu_header)
            for index, song in enumerate(mp3_files, start=1):
                print(f"{index}. {song}")

            choice_input = input("\nEnter the song # to play (or 'Q' to quit): ").strip()

            if choice_input.upper() == 'Q':
                print("Bye!")
                break

            if not choice_input.isdigit():
                print("Enter a valid number")
                continue

            choice = int(choice_input) - 1

            if 0 <= choice < len(mp3_files):
                play_music(folder, mp3_files[choice])
            else:
                print("Invalid choice")
    finally:
        # Proper cleanup of pygame resources
        pygame.mixer.quit()
        pygame.quit()


if __name__ == "__main__":
    main()
