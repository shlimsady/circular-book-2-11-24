# circular-book-2-11-24

Text manipulation tool where the user can filter and select random lines from text files, potentially building or modifying a composition in the process.

1. **Initialization**:
    - The program begins by defining a class called `TextOrganizer`. This class is designed to handle operations on text files within a specified folder.

2. **Reading Text Files**:
    - The `read_text_files` method within the `TextOrganizer` class reads all the text files within a specified folder and stores each line of text in a list called `lines`.

3. **Filtering Lines**:
    - The `filter_lines` method filters the lines based on a provided keyword. If a keyword is given, it selects only those lines that contain the keyword. If no keyword is provided, it retains all lines.

4. **Selecting a Random Line**:
    - The `select_random_line` method selects a random line from either the filtered lines (if there are any) or from all lines if no filtering has been applied.

5. **Adding Lines to Composition**:
    - The `add_line_to_composition` method appends a given line to a file called `circular.txt`. This file presumably serves as a composition being built or modified over time.

6. **Main Loop**:
    - The program enters a loop where it continues to interact with the user until terminated.
    - Within each iteration:
        - It filters the lines based on a keyword provided by the user (or none if not provided).
        - It selects a random line from the filtered lines (or all lines if there's no filtering).
        - It presents the random line to the user and awaits their input.
        - Based on the user's input:
            - If the user confirms (by inputting 'y'), the previous line (if exists) is added to the composition, the current line becomes the previous line, and the keyword is reset.
            - If the user denies (by inputting 'n'), the previous line is discarded, and the keyword is reset.
            - Otherwise, the user's input is treated as a keyword for further filtering.

7. **Termination**:
    - The program will continue this loop until terminated manually. After termination, it prints a message indicating the program's end.
