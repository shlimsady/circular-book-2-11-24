import os
import random

class TextOrganizer:
    def __init__(self, folder_path):
        self.folder_path = folder_path
        self.lines = []
        self.filtered_lines = []

    def read_text_files(self):
        for root, _, files in os.walk(self.folder_path):
            for file in files:
                if file.endswith('.txt'):
                    file_path = os.path.join(root, file)
                    with open(file_path, 'r') as f:
                        for line in f:
                            self.lines.append(line.strip())

    def filter_lines(self, keyword):
        if keyword:
            self.filtered_lines = [line for line in self.lines if keyword in line]
        else:
            self.filtered_lines = self.lines

    def select_random_line(self):
        if self.filtered_lines:
            return random.choice(self.filtered_lines)
        else:
            return random.choice(self.lines)

    def add_line_to_composition(self, line):
        with open('circular.txt', 'a') as f:
            f.write(line + '\n')

if __name__ == "__main__":
    # Determine the folder path where the script is located
    folder_path = os.path.dirname(os.path.realpath(__file__))

    # Create an instance of the TextOrganizer class
    organizer = TextOrganizer(folder_path)

    # Reading text files
    organizer.read_text_files()

    # Initialize variables for user interaction
    prev_line = None
    keyword = None

    # Main loop
    while True:
        # Filtering lines based on keyword
        organizer.filter_lines(keyword)

        # Selecting a Random Line
        random_line = organizer.select_random_line()

        # Presenting the Randomly Selected Line
        print(random_line)

        # User Interaction
        choice = input()

        # Handling user choice
        if choice.lower() == 'y':
            # Composition Completion: Add previous line to composition
            if prev_line:
                organizer.add_line_to_composition(prev_line)

            # Update previous line and reset keyword
            prev_line = random_line
            keyword = None
        elif choice.lower() == 'n':
            # Discard previous line
            prev_line = None
            keyword = None
        else:
            # Use keyword as filter
            keyword = choice

    print("Program terminated.")
