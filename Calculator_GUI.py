#!/usr/bin/env python
# coding: utf-8

"""
Calculator GUI Module

This module provides a graphical user interface for the Calculator application.
Features:
- Interactive button-based input or keyboard input through cursor
- Decimal place display selection
- Real-time calculation
- Error handling

Dependencies:
- tkinter
- Calculator module
"""

import tkinter as tk
import Calculator as calc

#Initialize calculator object
calculator = calc.Calculator()

def main() -> None:
    """
    Create and initialize the calculator GUI application.
    
    Sets up the main window, input fields, buttons, 
    and event handling for calculator interactions.
    """
    # Create the main window
    root = tk.Tk()
    #root.geometry("300x400")
    root.title('Calculator')

    #variable for user entry field 
    entry_string=tk.StringVar()

    # Create Calculation Window
    entry_screen=tk.Entry(root,font=('Times New Roman',20),justify='right',relief='sunken',textvariable=entry_string) 
    entry_screen.grid(columnspan=4,row=0, padx = 5, pady = 5)
    entry_screen.focus() 

    # Create Decimal Place Drop-down
    decimal_text='Decimals to display:'
    decimal_label=tk.Label(root, text=decimal_text,font=('Times New Roman',12),height=1)
    decimal_label.grid(columnspan = 2,row=1,column=1,padx=0,pady=3)
    decimal_place_options = [1, 2, 3, 4, 5, 6]
    decimal_value = tk.IntVar()
    decimal_value.set(4)
    decimal_dropdown = tk.OptionMenu(root, decimal_value, *decimal_place_options)
    decimal_dropdown.grid(columnspan = 1 ,row=1,column=3,padx=3,pady=3)

    # Create buttons 
    calculate_button='='
    clear_button='CLR'
    button_list=(
        ('(',')','^','/'),
        ('7','8','9','*'),
        ('4','5','6','-'),
        ('1','2','3','+'),
        (clear_button,'0','.',calculate_button)
        )
    for row_index, row_value in enumerate(button_list): 
        for column_index, column_value in enumerate(row_value):
            button = tk.Button(
                root, 
                text=column_value,
                font=('Times New Roman',16),
                width=4,
                height=2,
                command=lambda x=column_value: character_click(x)
                )
            button.grid(column = column_index, row = row_index+2, padx = 3, pady = 3)

    #define set to be used for button press logic
    flattened_button_list=[item for sublist in button_list for item in sublist]
    character_input=set(flattened_button_list)-{calculate_button, clear_button}

    #error message
    max_buttons = len(flattened_button_list)
    max_rows = len(button_list)
    max_columns = max_buttons//max_rows
    error_message=''
    error_text=tk.Label(root, text=error_message,font=('Times New Roman',12),height=1)
    error_text.grid(columnspan = max_columns,row=max_rows+2,column=0,padx=3,pady=3)
    
    #Function for button presses of character inputs
    def character_click(value):
        cursor_position=entry_screen.index(tk.INSERT)
        if value in character_input:
            entry_string.set(
                entry_string.get()[:cursor_position]+
                value+
                entry_string.get()[cursor_position:]
                )
            entry_screen.icursor(cursor_position+1)
        elif value==calculate_button:
            calc_output,calc_error=calculator.calculate(entry_string.get(),decimal_value.get())
            error_text.config(text=calc_error)
            entry_string.set(calc_output)
            entry_screen.icursor(len(entry_string.get()))
        elif value==clear_button:
            entry_string.set('')
            error_text.config(text='')

    #Function for key press 
    def on_key_press(event): 
        if event.keysym == "Return":
            character_click('=')
    #call for keypress function 
    root.bind("<KeyPress>",on_key_press)
            
    
    # Start the GUI event loop
    root.mainloop()

if __name__ == "__main__":
    main()