#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Simple calculator with the following capabilities
#user input for expression as a string
#parse out numbers and operators from the input into a list
#perform calculations on the list using PEMDAS and return a single value 
#to implement - error handling for multiple operators in a row
#to implement - convert all print errors to raising errors and try-except blocks for functions
#to implement - GUI error outputs at bottom
#to implement - after GUI, some sort of memory - maybe save to a text file to read back?

#import regular expressions
import re

error_out=''

def exponent(express_list):
    """walk through list and perform all exponent operations
    return smaller list with all values and operators replaced with
    unified value of each operation"""
    # print('mult_div list',express_list)
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


def multi_divide(express_list):
    """walk through list and perform all multiplication and division operations
    return smaller list with all values and operators replaced with
    unified value of each operation"""
    # print('mult_div list',express_list)
    i=0
    global error_out
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
            try:
                express_list[i]=first_val/second_val
            except ZeroDivisionError:
                error_out='ERROR: Division by Zero.'
                break
        #if no operation happens, continue loop on the next index
        else:
            i=i+1
            continue
        #remove numbers that have been operated on
        del express_list[i+1]
        del express_list[i-1]
    return express_list


def add_subtract(express_list):
    """walk through list and perform all addition and subtraction operations
    return smaller list with all values and operators replaced with
    unified value of each operation"""
    # print('add_sub list',express_list)
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

def merge_negatives(express_list,all_operators_set):
    """walk through list and check all "-" characters for being a subtraction operator or a negative sign 
    return smaller list with all identified negative signs incorporated with its associated value"""
    #print('merge_negatives list',express_list)
    i=0
    negative_val=0.0
    while i<len(express_list)-1:
        if express_list[i]=="-" or express_list[i]== '-':
            #case of "-" at beginning of the list
            if i==0 and isinstance(express_list[i+1],float): 
                negative_val = express_list[i+1]
                #replace operator with combined number
                express_list[i]=(-1*negative_val)
                del express_list[i+1]
            #check preceeding item for an operator and next item for a number
            elif express_list[i-1] in all_operators_set and isinstance(express_list[i+1],float):
                negative_val = express_list[i+1]
                #replace operator with combined number
                express_list[i]=(-1*negative_val)
                del express_list[i+1]
            else: #item is an operator and will be skipped in the loop
                i=i+1
                continue
        #if '-' not found, continue loop on the next index
        else:
            i=i+1
            continue
    return express_list
    
def parenth_list(express_list,parenth_l,parenth_r):
    """function that creates a slice of the expression between parentheses
    and performs all calculations between those parentheses before returning the
    expression with everything between the parentheses resolved"""
    # print("Parenth input",express_list)
    #define new list as a slice of the original list with just the portion between parentheses
    parenth_slice = express_list[parenth_l:parenth_r+1]
    # print("Parenth slice",parenth_slice)
    #perform operations on slice
    parenth_slice = exponent(parenth_slice)
    parenth_slice = multi_divide(parenth_slice)
    parenth_slice = add_subtract(parenth_slice)
    # print('slice after operations',parenth_slice)
    # #remove parentheses and replace with calculated output 
    del express_list[parenth_l+1:parenth_r+1]
    express_list[parenth_l]=parenth_slice[1]
    # print('full expression after parenth calc',express_list)
    return express_list

def calculator_main(user_input):
    '''call for user input
    user_input = input('Provide the expression you wish to calculate:\nUsable operators are + , - , * , / , ^, ( , )\n--->')
    pull out all numbers, numbers with decimals, and "*","+","-","/","^","(",")" operators and put them in an ordered list'''
    global error_out
    error_out=''
    output_list = re.findall(r'\d+\.?\d*|\d*\.?\d+|[()*/+-^]',user_input)
    #print(f'list:{output_list} length of list: {len(output_list)}')

    #loop through list for further manipulation
    for i in range(0,len(output_list)):
        #convert all numbers in the list from strings to float
        if re.search(r'\d+\.?\d*|\d*\.?\d+',output_list[i]):
            output_list[i]=float(output_list[i])
            
    #sets of operators and all characters for error checking and handling negative numbers
    operator_set = {'*','/','+','-','^'}
    all_character_set = {'0','1','2','3','4','5','6','7','8','9',' ','(',')','.'}|operator_set
    
    #convert all negative signs to negative numbers, leaving subtraction symbols
    output_list = merge_negatives(output_list,operator_set|{'(',')'}) 
    #print(f'List after negatives are merged: {output_list}')
    #Error code checking before doing calculations
    #check for characters outside the scope of the calculator in user input
    for item in user_input:
        #print(item)
        if isinstance(item,str) and item not in all_character_set:
            error_out='ERROR: Unexpected characters.'
            break 
    #check for consecutive operators
    for i, item in enumerate(output_list):
        if i>0:
            prev_item = output_list[i-1]
            #print(f"item: {item} prev_item:{prev_item}")
            if item in operator_set and prev_item in operator_set:
                error_out='ERROR: Consecutive operators.'
                #return error_out
    #check for equal brackets
    if output_list.count(')')!=output_list.count('('):
        error_out="ERROR: Unequal parenthesis."
    #check for something to calculate in the list 
    elif len(output_list)<1:
        error_out="ERROR: Nothing to calculate."
    #check for operators at beginning or end besides parentheses and throw an error 
    elif output_list[0] in operator_set or output_list[len(output_list)-1] in operator_set: 
        error_out="ERROR: Invalid operator at start or end."
    if not error_out.startswith('ERROR:'):
        #find first right bracket and then its associated left bracket
        #perform calculation on the resulting slice 
        output_list_rev_slice=[]
        pareth_index_r=0
        parenth_index_l=0
        while ')' in output_list:
            parenth_index_r = output_list.index(')')
            output_list_rev_slice=output_list[:parenth_index_r]
            output_list_rev_slice.reverse()
            try:
                parenth_index_l=parenth_index_r-output_list_rev_slice.index('(')-1
            except ValueError:
                error_out='ERROR: Inproperly paired parenthesis.'
                break
            else: 
                output_list = parenth_list(output_list,parenth_index_l,parenth_index_r)
        output_list = add_subtract(multi_divide(exponent(output_list)))
        if len(output_list)==1:
            #print("The answer is: ",float(output_list[0]))
            output_txt=output_clean_convert(output_list)
            return (output_txt, error_out)
        else:
            #print("ERROR: The answer could not be fully calculated. Please review your input.")
            #print(error_out)
            output_txt=output_clean_convert(output_list)
            return (output_txt, error_out)
    else:
        output_txt=user_input#output_clean_convert(output_list)
        return (output_txt, error_out)
    
def output_clean_convert(output_list):
    clean_output=[]
    for item in output_list:
        if isinstance(item,float):
            if item.is_integer():
                item=int(item)
        clean_output.append(item)
    text_out=''.join(map(str,clean_output))
    return text_out

if __name__ == "__main__": 
    user_input_calc = input('Provide the expression you wish to calculate:\nUsable operators are + , - , * , / , ^, ( , )\n--->')
    out,error=calculator_main(user_input_calc)
    #print(out)
    #print(error)


# In[ ]:




