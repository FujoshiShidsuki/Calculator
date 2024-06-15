# Simple Calculator

A basic calculator application built with Python and Tkinter that can perform basic arithmetic operations, as well as additional functions like square root and exponentiation. The calculator also includes a delete key, an all clear key, and a last answer key.

## Features

- **Basic Arithmetic Operations**: Addition, subtraction, multiplication, and division.
- **Advanced Functions**: Square root (√) and exponentiation (^).
- **Memory Functions**: Memory add (M+), memory subtract (M-), and memory recall (MR).
- **Error Handling**: Division by zero and invalid input handling.
- **Delete Key**: Delete the last character in the current expression.
- **All Clear Key**: Clear the current expression and any stored memory.
- **Last Answer Key**: Recall the last calculated answer.

## Requirements

- Python 3.x
- Tkinter (comes pre-installed with Python)

## Installation

1. **Clone the Repository**:
    ```sh
    git clone https://github.com/FujoshiShidsuki/Calculator.git
    cd Calculator
    ```

2. **Run the Application**:
    ```sh
    python calculator.py
    ```

## Usage

- **Open the Calculator Application**: After running `calculator.py`, the calculator window will open.
- **Input Calculations**: Use the buttons on the calculator interface to input your calculations.
  - Numbers and basic operations (addition, subtraction, multiplication, division) are supported.
  - Use the square root (√) and exponentiation (^) buttons for advanced calculations.
  - Use the memory functions (M+, M-, MR) to store and recall values.
  - Use the `AC` button to clear the current expression and any stored memory.
  - Use the `Del` button to delete the last character in the current expression.
  - Use the `Ans` button to recall the last calculated answer.

## Code Structure

The main components of the application are as follows:

### 1. Calculator Class

The `Calculator` class handles the creation of the GUI and the logic for the calculator's operations.

#### Methods

- **`__init__(self, root)`**: Initializes the calculator with the main Tkinter window.
- **`create_widgets(self)`**: Creates the entry widgets for displaying operations and answers, and the buttons for input.
- **`create_button(self, text, row, col, width, height)`**: Creates a button and assigns it to the grid.
- **`on_button_click(self, char)`**: Handles the logic for each button click.
- **`update_display(self, answer=None)`**: Updates the display with the current expression and/or answer.

## Error Handling

- **Division by Zero**: Shows an error message when attempting to divide by zero.
- **Invalid Input**: Shows an error message for invalid inputs or expressions.

## Contributing

If you would like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -am 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Create a new Pull Request.
