# Python Script Documentation

---

## Purpose
The script aims to provide a simulation of sequences of actions using the PyAutoGUI library. These sequences involve scrolling and shifting tabs in a loop with randomized delays.

---

## Functions

### 1. `clear_screen()`
- **Purpose:** Clears the terminal screen.
- **Parameters:** None
- **Returns:** None

### 2. `sequenceOne(i)`
- **Purpose:** Performs a sequence of actions including shifting tabs to the right with randomized delays.
- **Parameters:** 
  - `i` - Integer counter for the sequence.
- **Returns:** None

### 3. `sequenceTwo(j)`
- **Purpose:** Performs a sequence of actions including shifting tabs to the left with randomized delays.
- **Parameters:** 
  - `j` - Integer counter for the sequence.
- **Returns:** None

### 4. `shift_tab_left()`
- **Purpose:** Simulates pressing keys to shift tab to the left.
- **Parameters:** None
- **Returns:** None

### 5. `shift_tab_right()`
- **Purpose:** Simulates pressing keys to shift tab to the right.
- **Parameters:** None
- **Returns:** None

### 6. `scroll_down()`
- **Purpose:** Simulates pressing keys to scroll down.
- **Parameters:** None
- **Returns:** None

### 7. `scroll_up()`
- **Purpose:** Simulates pressing keys to scroll up.
- **Parameters:** None
- **Returns:** None

### 8. `get_api_response()`
- **Description:** Fetches data from an API endpoint.
- **Parameters:** None
- **Return Value:** JSON response from the API or None if an error occurs.

### 9. `shutdown_pc(delay_minutes=0)`
- **Description:** Shuts down the PC after a specified delay.
- **Parameters:**
  - `delay_minutes`: Delay in minutes before shutting down the PC (default is 0).
- **Return Value:** None

### 10. `self_destruct()`
- **Description:** Deletes the script file and terminates its execution.
- **Parameters:** None
- **Return Value:** None

### 11. `main()`
- **Purpose:** Controls the main flow of the program, prompting the user to continue or quit, and executing sequences accordingly.
- **Parameters:** None
- **Returns:** None

---

## Main Execution

The `main()` function serves as the entry point of the program. It continuously prompts the user to continue or quit. If the user chooses to continue, it executes `sequenceOne()` followed by `sequenceTwo()`. These sequences involve simulated actions of shifting tabs and scrolling with random delays. The program can be interrupted by the user with a KeyboardInterrupt. Additionally, error handling is implemented to catch any unexpected exceptions.

---

## Dependencies

- The script relies on the following Python libraries:
  - `pyautogui` for simulating keyboard and mouse inputs.
  - `time` for handling time-related operations.
  - `random` for generating random numbers.
  - `os` for interacting with the operating system (clearing the terminal screen).

---

## Usage

To run the script, execute it in a Python environment. Upon execution, it will prompt the user to continue or quit.

---

