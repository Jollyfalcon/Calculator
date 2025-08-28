#!/usr/bin/env python
# coding: utf-8

"""
Calculator Module

This module provides a comprehensive calculator functionality with support for:
- Basic arithmetic operations (+, -, *, /, ^)
- Parenthetical expressions
- Error handling
- Parsing mathematical expressions using regular expressions

Key Features:
- Supports PEMDAS order of operations
- Handles negative numbers
- Comprehensive error checking
"""

import re
from typing import List, Union, Tuple

class CalculatorError:
    """Predefined error messages for calculator operations."""

    ERROR_TYPES = {
        'CONSECUTIVE_OPERATORS': 'Invalid: Consecutive operators',
        'DECIMAL_ERROR': 'Invalid: Excess decimal points',
        'CONSECUTIVE_NUMBERS': 'Invalid: Consecutive numbers',
        'EMPTY_EXPRESSION': 'Invalid: No expression',
        'UNEQUAL_PARENTHESIS': 'Invalid: Unbalanced parentheses',
        'INVALID_OPERATOR_PLACEMENT': 'Invalid: Operators at start/end',
        'UNEXPECTED_CHARACTERS': 'Invalid: Unexpected characters',
        'DIVISION_BY_ZERO': 'Error: Division by zero',
        'CALCULATION_INCOMPLETE': 'Error: Calculation incomplete',
        'IMPROPER_PARENTHESIS': 'Invalid: Improperly paired parenthesis',
        'CALCULATION_FAILED': 'Fatal Error: See print output'
    }
    @classmethod
    def get_error_message(cls, error_key: str) -> str:
        """Retrieve standardized error message."""
        return cls.ERROR_TYPES.get(error_key, 'Unknown Error')


class Calculator:
    """
    Comprehensive calculator class with advanced parsing and calculation capabilities.
    """

    def __init__(self):
        """
        Initialize calculator with predefined operator and character sets.
        """
        self.OPERATOR_SET = {'*','/','+','-','^'}
        self.ALL_OPERATOR_SET = {'(',')'}|self.OPERATOR_SET
        self.ALL_CHARACTER_SET = {'0','1','2','3','4','5','6','7','8','9',' ','.'}|self.ALL_OPERATOR_SET

    def parse_input(
            self,
            user_input: str
            ) -> List[Union[float, str]]:
        """
        Parse and preprocess the input expression.
        
        Args:
            user_input (str): Mathematical expression to parse
        
        Returns:
            List of tokens (numbers and operators)
        """
         #remove whitespaces and parse input
        user_input_no_whitespace = re.sub(r'\s+', '', user_input)
        output_list = re.findall(r'\d+\.?\d*|\d*\.?\d+|[()*/+-^]',user_input_no_whitespace)

        #convert numbers to float
        output_list = [
        float(token) if re.search(r'\d+\.?\d*|\d*\.?\d+',token)
        else token for token in output_list
        ]

        return output_list
    
    def merge_negatives(
            self,
            express_list: List[Union[float,str]]
            ) -> List[Union[float, str]]:
        """
        Process and merge negative signs in the expression list.
        
        Args:
            express_list (list): List of expressions to process
        
        Returns:
            list: Processed list with negative signs resolved
        """
        i=0
        while i<len(express_list) - 1:
            if express_list[i]=='-':
                #check for "-" at beginning of the list
                #check preceeding item for an operator and next item for a number
                #combine "-" with number, append to new list, and skip number in sequence
                if (i==0 or express_list[i-1] in self.ALL_OPERATOR_SET) \
                    and isinstance(express_list[i+1],float):
                    negative_val = express_list[i+1]
                    express_list[i] = -1 * negative_val
                    del express_list[i+1]
                else: #"-" is an operator and will be skipped in the loop
                    i+=1
            #if '-' not found, continue loop on the next index
            else:
                i+=1
        return express_list
    
    def validate_input(
            self,
            output_list: List[Union[float, str]],
            user_input: str
            ) -> str:
        """
        Perform comprehensive input validation.
        
        Args:
            output_list (list): Processed expression list
            user_input (str): Original input expression
        
        Returns:
            str: Error message (empty string if no error)
        """
        #check for characters outside the scope of the calculator in user input
        unexpected_chars = set(user_input) - self.ALL_CHARACTER_SET
        if unexpected_chars:
            return CalculatorError.get_error_message('UNEXPECTED_CHARACTERS') 
        
        #check for empty list
        if len(output_list)<1:
            return CalculatorError.get_error_message('EMPTY_EXPRESSION')
    
       #check for consecutive operators, decimal points, or numbers
        for i, item in enumerate(output_list[1:],1):
            prev_item = output_list[i-1]
            if item in self.OPERATOR_SET and prev_item in self.OPERATOR_SET:
                return CalculatorError.get_error_message('CONSECUTIVE_OPERATORS')
            if item == '.':
                return CalculatorError.get_error_message('DECIMAL_ERROR')
            if isinstance(item,float) and isinstance(prev_item,float):
                return CalculatorError.get_error_message('CONSECUTIVE_NUMBERS')

        #check for equal brackets
        if output_list.count(')')!=output_list.count('('):
            return CalculatorError.get_error_message('UNEQUAL_PARENTHESIS')
        #check for start/end operators besides parentheses
        if output_list[0] in self.OPERATOR_SET or output_list[-1] in self.OPERATOR_SET: 
            return CalculatorError.get_error_message('INVALID_OPERATOR_PLACEMENT')
        
    def parenth_list(
            self,
            express_list: List[Union[float, str]],
            parenth_l: int,
            parenth_r: int
            ) -> List[Union[float, str]]:
        """
        Calculate expression within parentheses.
        
        Args:
            express_list (list): Full expression list
            parenth_l (int): Left parenthesis index
            parenth_r (int): Right parenthesis index
        
        Returns:
            list: Updated expression list
        """
        #slice out the portion between parentheses
        parenth_slice = express_list[parenth_l:parenth_r+1]
        #perform operations on slice
        parenth_slice = self.exponent(parenth_slice)
        parenth_slice = self.multi_divide(parenth_slice)
        parenth_slice = self.add_subtract(parenth_slice)
        # #remove parentheses and replace with calculated output 
        del express_list[parenth_l+1:parenth_r+1]
        express_list[parenth_l]=parenth_slice[1]
        return express_list

    def exponent(
            self,
            express_list: List[Union[float, str]]
            ) -> List[Union[float, str]]:
        """Perform exponentiation operations."""
        i=0
        while i<=len(express_list)-1:
            #exponent 
            if express_list[i]=="^" or express_list[i]=='^':
                #retrieve numbers to be operated
                first_val = float(express_list[i-1])
                second_val = float(express_list[i+1])
                #replace operator with combined number
                express_list[i]=first_val**second_val
            #if no operation happens, continue loop on the next index
            else:
                i=i+1
                continue
            #remove numbers that have been operated on
            del express_list[i+1]
            del express_list[i-1]
        return express_list


    def multi_divide(
            self,
            express_list: List[Union[float, str]]
            ) -> List[Union[float, str]]:
        """Perform multiplication and division operations."""
        i=0
        while i<=len(express_list)-1:
            #multiplication 
            if express_list[i]=="*" or express_list[i]== '*':
                #retrieve numbers to be operated
                first_val = float(express_list[i-1])
                second_val = float(express_list[i+1])
                #replace operator with combined number
                express_list[i]=first_val*second_val
            #division
            elif express_list[i]=="/" or express_list[i]== '/':
                #retrieve numbers to be operated
                first_val = float(express_list[i-1])
                second_val = float(express_list[i+1])
                #replace operator with combined number
                # try:
                express_list[i]=first_val/second_val
                # except ZeroDivisionError:
                #     error_out='ERROR: Division by Zero.'
                #     break
            #if no operation happens, continue loop on the next index
            else:
                i=i+1
                continue
            #remove numbers that have been operated on
            del express_list[i+1]
            del express_list[i-1]
        return express_list


    def add_subtract(
            self,
            express_list: List[Union[float, str]]
            ) -> List[Union[float, str]]:
        """Perform addition and subtraction operations."""
        i=0
        while i<=len(express_list)-1:
            #addition 
            if express_list[i]=="+" or express_list[i]== '+':
                #retrieve numbers to be operated
                first_val = float(express_list[i-1])
                second_val = float(express_list[i+1])
                #replace operator with combined number
                express_list[i]=first_val+second_val
            #subtraction
            elif express_list[i]=="-" or express_list[i]== '-':
                #retrieve numbers to be operated
                first_val = float(express_list[i-1])
                second_val = float(express_list[i+1])
                #replace operator with combined number
                express_list[i]=first_val-second_val
            #if no operation happens, continue loop on the next index
            else:
                i=i+1
                continue
            #remove numbers that have been operated on
            del express_list[i+1]
            del express_list[i-1]
        return express_list
    
    def output_clean_convert(
            self,
            output_list: List[Union[float, str]],
            decimal_places: int
            ) -> str:
        """
        Convert calculation result to clean string representation.
        
        Args:
            output_list (list): Final calculation result
            decimal_places (int): decimal places for display
        
        Returns:
            str: Formatted output string
        """
        clean_output=[]
        # convert whole number float to int
        # and floats with a large amount of decimals to 

        decimal_places_str='{'+f'{decimal_places}'+'}'
        for item in output_list:
            if isinstance(item,float):
                if re.search(fr'\.\d{decimal_places_str}',str(item)):
                    item = f'{item:.{decimal_places}f}'
                    item = float(item)
                if item.is_integer():
                    item=int(item)

            clean_output.append(item)
        #join list into string
        text_out=''.join(map(str,clean_output))
        return text_out

    def calculate(self, user_input: str, decimal_places: int) -> Tuple[str, str]:
        """
        Main calculation method.
        
        Args:
            user_input (str): Mathematical expression to calculate
            decimal_places (int): number of decimal places to return
        
        Returns:
            Tuple of (result, error_message)
        """
        try:
            # Parse input
            output_list = self.parse_input(user_input)
            # Merge negative numbers
            output_list = self.merge_negatives(output_list)
            
            # Validate input
            error_out = self.validate_input(output_list, user_input)
            if error_out:
                return user_input, error_out
            
            # Handle parenthetical expressions
            while ')' in output_list:
                parenth_index_r = output_list.index(')')
                output_list_rev_slice = output_list[:parenth_index_r]
                output_list_rev_slice.reverse()
                try:
                    parenth_index_l = parenth_index_r - output_list_rev_slice.index('(') - 1
                except ValueError:
                    return user_input, CalculatorError.get_error_message('IMPROPER_PARENTHESIS')
                
                output_list = self.parenth_list(output_list, parenth_index_l, parenth_index_r)
            
            # Perform calculations
            output_list = self.add_subtract(
                self.multi_divide(
                    self.exponent(output_list)
                )
            )
            
            # Verify final result
            if len(output_list) == 1:
                output_txt = self.output_clean_convert(output_list, decimal_places)
                return output_txt, ''
            else:
                return user_input, CalculatorError.get_error_message('CALCULATION_INCOMPLETE')
        
        except ZeroDivisionError:
            return user_input, CalculatorError.get_error_message('DIVISION_BY_ZERO')
        # except Exception as ex:
        #     print(str(ex))
        #     return user_input, CalculatorError.get_error_message('CALCULATION_FAILED')

if __name__ == "__main__": 
    user_input_calc = input('Provide the expression you wish to calculate:\nUsable operators are + , - , * , / , ^, ( , )\n--->')
    calculator = Calculator()
    out,error=calculator.calculate(user_input_calc,4)
    print(f'Results: {out}\nError: {error}')





