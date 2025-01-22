import pyautogui
import pytesseract
import time
import json
from datetime import datetime
from PIL import ImageGrab
import re

class CaptionMatcher:
    def __init__(self, dictionary_path, output_path):
        """
        Initialize the CaptionMatcher with paths for the dictionary and output file.
        
        Args:
            dictionary_path (str): Path to JSON file containing key-value pairs
            output_path (str): Path where matched outputs will be written
        """
        self.dictionary = self._load_dictionary(dictionary_path)
        self.output_path = output_path
        self.last_text = ""
        
    def _load_dictionary(self, path):
        """Load and return the dictionary from JSON file."""
        with open(path, 'r') as f:
            return json.load(f)
    
    def _capture_captions_area(self):
        """
        Capture the area where Google Live Captions appear.
        Adjust these coordinates based on your screen setup.
        """
        # These coordinates need to be adjusted for your specific setup
        # Format: left, top, right, bottom
        bbox = (100, 800, 800, 900)  
        screenshot = ImageGrab.grab(bbox=bbox)
        return screenshot
    
    def _extract_text(self, image):
        """Extract text from image using OCR."""
        text = pytesseract.image_to_string(image)
        return text.strip()
    
    def _find_matches(self, text):
        """Find all matching keys from dictionary in the text."""
        matches = []
        for key, value in self.dictionary.items():
            # Case insensitive search
            if re.search(r'\b' + re.escape(key) + r'\b', text, re.IGNORECASE):
                matches.append((key, value))
        return matches
    
    def _write_to_file(self, text, matches):
        """Write matched text and corresponding values to output file."""
        if matches:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open(self.output_path, 'a', encoding='utf-8') as f:
                f.write(f"\n=== {timestamp} ===\n")
                f.write(f"Caption: {text}\n")
                f.write("Matches:\n")
                for key, value in matches:
                    f.write(f"- {key}: {value}\n")
    
    def run(self, interval=1.0):
        """
        Main loop to continuously monitor captions.
        
        Args:
            interval (float): Time between captures in seconds
        """
        print(f"Starting caption monitoring. Output will be written to {self.output_path}")
        try:
            while True:
                # Capture and process image
                image = self._capture_captions_area()
                current_text = self._extract_text(image)
                
                # Only process if text has changed
                if current_text != self.last_text and current_text.strip():
                    matches = self._find_matches(current_text)
                    if matches:
                        self._write_to_file(current_text, matches)
                    self.last_text = current_text
                
                time.sleep(interval)
                
        except KeyboardInterrupt:
            print("\nMonitoring stopped by user")
        except Exception as e:
            print(f"An error occurred: {str(e)}")

# Example usage
if __name__ == "__main__":
    # Example dictionary file structure:
    # {
    #     "hello": "greeting",
    #     "weather": "environmental conditions",
    #     "meeting": "scheduled gathering"
    # }
    
    config = {
        "dictionary_path": "dictionary.json",
        "output_path": "caption_matches.txt"
    }
    
    matcher = CaptionMatcher(config["dictionary_path"], config["output_path"])
    matcher.run()