# Project Name: Interactive Calculator GUI

## Project Overview
A comprehensive calculator application demonstrating advanced Python programming techniques, featuring a user-friendly Tkinter GUI, robust error handling, and thorough unit testing. Mathematical expression input is through either GUI button presses or keyboard input.

## Technologies Used
- Python
- Tkinter
- Regular Expressions
- Unit Testing (pytest)

## Project Objectives
- Demonstrate Python syntax proficiency and OOP Python practices
- Showcase GUI development skills
- Implement comprehensive error handling
- Provide robust unit testing

## Features
- comprehensive PEMDAS operations
    - Any amount or configuration of nested parenthesis
    - Operators: Add (+), Subtract (-), Multiply (*), Divide (/), Exponent (^)
    - handles float and integer operations
- Interactive GUI
- Selection for decimal places to display
- Error handling and display
    - Checks for correct Parenthesis pairing
    - Checks for unexpected character inputs
    - Checks for duplicate operators or decimals
    - Checks for divide by zero or overflow
- Comprehensive unit tests using pytest

## Prerequisites
- Python 3.x
- Virtual Environment
- Required dependencies (list in requirements.txt)

## Installation

### Clone the Repository
git clone https://github.com/Jollyfalcon/Calculator
cd project-directory

### Set Up Virtual Environment
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

### Install Dependencies
pip install -r requirements.txt

### Running the Application
interact with the calculator through either a GUI or a command line interface
#### GUI interaction
python Calculator_GUI.py
#### CLI interaction
python Calculator.py

### Running Tests
pytest test_calculator.py

### Project Structure
project-directory/  
│  
├── Calculator.py  
├── Calculator_GUI.py  
├── test_calculator.py  
├── requirements.txt  
└── README.md

## Learning Outcomes
Advanced Python programming  
GUI development with Tkinter  
Regular expression manipulation  
Comprehensive error handling  
Unit testing strategies  

## License
MIT License

## Contact
Joshua Stuckey
email: stuckeyjp1@gmail.com
LinkedIn: https://www.linkedin.com/in/joshua-stuckey/
