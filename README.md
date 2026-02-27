# Simple Text Editor
A command‑line text editor that supports adding characters, deleting the last character, and undoing previous actions. The editor maintains a history stack to reverse operations and provides a minimal, easy‑to‑use interface for practicing stack‑based undo functionality.

## Features
- Add a character to the end of the text
- Delete the last character
- Undo the most recent add or delete
- Display the current text
- Exit the program safely
- History stack to support undo operations
- Graceful handling of invalid or empty operations

## How It Works
The editor uses two core components:
- TextEditor class — stores the current text and a history stack
- TextOperation objects — record each action (add or delete) and the affected character
Undoing an action simply performs the opposite of the last recorded operation.




## Running the Program

python TextEditor.py

Running Tests
This project uses Python’s built‑in unittest framework.
Run all tests:
python test_TextEditor.py



## Time & Space Complexity
Each operation modifies a Python string, which is immutable.
This means modifying the text requires creating a new string.
- Add: O(n)
- Delete: O(n)
- Undo: O(n)
- Space: O(n) for the text + O(n) for the history stack

## Edge Cases Handled
- Deleting when text is empty
- Undoing with no history
- Adding invalid input (more than one character)
- Multiple undos in a row
- Undoing a delete restores the removed character

## Testing Overview
The test suite includes:
- Adding one or multiple characters
- Undoing add
- Undoing delete
- Deleting characters
- Handling empty deletes
- Handling empty undo
- Long word construction
- Multiple undo operations


