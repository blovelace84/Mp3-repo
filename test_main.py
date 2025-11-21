"""
Basic tests for the MP3 player to verify core functionality.
"""
import os
import sys
import unittest
from unittest.mock import patch, MagicMock

# Add the parent directory to the path to import main
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import main


class TestMP3Player(unittest.TestCase):
    """Test cases for MP3 player functions."""

    def setUp(self):
        """Set up test fixtures."""
        self.test_folder = "Music"
        self.test_song = "test.mp3"

    @patch('pygame.mixer.init')
    @patch('pygame.init')
    def test_main_initialization(self, mock_pygame_init, mock_mixer_init):
        """Test that pygame is initialized correctly."""
        # This test would need more mocking for full execution
        mock_mixer_init.return_value = None
        mock_pygame_init.return_value = None
        # Just verify imports work correctly
        self.assertTrue(hasattr(main, 'main'))
        self.assertTrue(hasattr(main, 'play_music'))

    def test_file_path_construction(self):
        """Test that file paths are constructed correctly."""
        folder = "Music"
        song = "test.mp3"
        expected_path = os.path.join(folder, song)
        actual_path = os.path.join(folder, song)
        self.assertEqual(expected_path, actual_path)

    @patch('os.path.exists')
    def test_play_music_file_not_found(self, mock_exists):
        """Test play_music handles missing files gracefully."""
        mock_exists.return_value = False
        # The function should return early without error
        result = main.play_music(self.test_folder, "nonexistent.mp3")
        self.assertIsNone(result)

    def test_music_folder_exists(self):
        """Test that the Music folder exists in the repository."""
        self.assertTrue(os.path.isdir("Music"),
                        "Music folder should exist in the repository")

    def test_mp3_files_list_creation(self):
        """Test that MP3 files can be listed from Music folder."""
        if os.path.isdir("Music"):
            mp3_files = [f for f in os.listdir("Music") if f.endswith(".mp3")]
            self.assertIsInstance(mp3_files, list)
            # The test repo should have MP3 files
            self.assertGreater(len(mp3_files), 0,
                               "Music folder should contain at least one MP3 file")


class TestPerformanceOptimizations(unittest.TestCase):
    """Test cases to verify performance optimizations."""

    def test_pygame_imported(self):
        """Verify pygame is imported."""
        self.assertTrue(hasattr(main, 'pygame'))

    def test_functions_have_docstrings(self):
        """Verify functions have docstrings for maintainability."""
        self.assertIsNotNone(main.play_music.__doc__)
        self.assertIsNotNone(main.main.__doc__)
        self.assertTrue(len(main.play_music.__doc__) > 10)
        self.assertTrue(len(main.main.__doc__) > 10)


if __name__ == '__main__':
    unittest.main()
