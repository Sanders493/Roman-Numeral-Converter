'''
- Author: Sanders Tshinyama
- Project Title: Sanders93 Roman Numeral Calculator
- Purpose: The program gets two inputs as roman numbers and an other one as one of five algebric operators(*,/,+,-,^),
converts both numbers into integers, apply the operator on the integers, and convert the result as a Roman Numeral. 
If the operator is division, the program will also ouput a remainder as a Roman Numral.
- Contributor : Abenezer Getachew
- Date: November 6, 2022
'''
import math  #import the math module to allow the prgoram to use math methods(such as 'ceil()' )

# Creating a dict that contains the values of all Numeral Numbers used in this program
values = {                                 
    'I': 1,
    'IV': 4,
    'V': 5,
    'IX': 9,
    'X': 10,
    'XL': 40,
    'L': 50,
    'XC': 90,
    'C': 100,
    'CD': 400,
    'D': 500,
    'CM': 900,
    'M': 1000
}
# Creating a list that contains all the operators used in this program
op_list = ['*', '/', '+', '-', '^']

def get_roman_num():
    ''' This function asks for a string input, gets rid of whitespaces and capitalizes every characters, 
        and makes sure that it is a valid Roman Numeral if not, it asks for an other input until it gets a valid
        Roman Numeral, and then it returns that valid roman numeral.
    '''
    sentinal1 = ''
    while sentinal1 != 'q':      #this loop that will keep asking for an input as long as that input is not a valid roman numeral
        roman_number = input('Enter a Roman Numeral (no spaces) : ').upper().strip()
        if roman_number == '':   
                print('Invalid Roman numeral!'\
                      '\nYou did not to type any character.')    
                continue
        for i in range(0, len(roman_number)):  
            list_5s = ['V','L','D']     #list of all elements that can appear more than one time in a roman numeral
            list_49 = ['V', 'X', 'I']      #list of only elements that can appear after 'I' in a roman nunelar
            for i in range(0, len(roman_number)):
                r = 0
                if roman_number[i] not in values:
                    print('Invalid Roman numeral!'\
                         '\nYou have entered an invalid Roman numeral chararcter.')
                    r -= 1
                elif r == 0:
                    break   
            else:
                break
            if ('I' in roman_number) and (i < len(roman_number) - 1):   
                if roman_number.index('I') != -1 and len(roman_number) >= 2 and roman_number[i] == 'I':   #if 'I' is not the last character, it can only be followed by one of the character in list_49
                    if roman_number[i + 1] not in list_49:
                        print('Invalid Roman numeral!'\
                              '\nYou need to enter a valid Roman numeral.')
                        break
            if len(roman_number) >= 4:
                for i in range(len(roman_number)):
                    if len(roman_number) - i >= 4:      #checks if there are they are not 4 consecutive roman characters in the input
                        r = 0
                        if (roman_number[i] == roman_number[i + 1]) and  (roman_number[i] == roman_number[i + 2]) and (roman_number[i]== roman_number[i + 3]):
                            print('Invalid Roman numeral!'\
                                  '\nYou need to enter a valid Roman numeral.')
                            r = r - 1
                        elif len(roman_number) > 4:
                            continue
                    elif r != -1:
                        break                     
                else:
                    break    
            if roman_number[i] in list_5s and roman_number.count(roman_number[i]) >= 2:    #checks if the character in the list_5s are not encountered twice or more in the input
                print('Invalid Roman numeral!'\
                      '\nYou need to enter a valid Roman numeral.')
                break
            if (i < len(roman_number) - 1):     #makes sure that we don't go out of index 
                if (values[roman_number[i]] < values[roman_number[i + 1]]):   #Check if the character at index i is less than the character preceding it  
                    c_letter = roman_number[i] + roman_number[i + 1]          # If so, concatenate them together and assign them to the variable c_letter
                    if (c_letter not in values) or (roman_number.count(c_letter) >= 2):
                        print('Invalid Roman numeral!'\
                            '\nYou need to enter a valid Roman numeral.')
                        break 
                    if values[c_letter] > values[roman_number[i - 1]]:       
                        print('Invalid Roman numeral!'\
                            '\nYou need to enter a valid Roman numeral.')
                        break     
        else:
            sentinal1 = 'q'
    return roman_number  
def convert_roman_num(roman_num):
    ''' This function takes a valid Roman Numeral(roman_num) as argument, and return a decimal number.
        While making sure that the number is not equal to 0 or more than 3999.
    '''
    decimal_num = 0
    for i in range(len(roman_num) - 1, -1, -1):             # Loop through each character of the Roman Numeral starting from the last character going downward to the first character  
        if i > 0:                                       # Check if the index given is not negative
            if values[roman_num[i]] > values[roman_num[i - 1]]: # Check if the character at index i is less than the character preceding it
                c_letter = roman_num[i - 1] + roman_num[i]      # If so, concatenate them together and assign them to the variable c_letter
                decimal_num += values[c_letter]           # Add the integer value at the key c_letter from the dict values to the integer f_num_int
                continue
        if i < (len(roman_num) - 1):                        # Check if the index is not out of range
            if (values[roman_num[i]] >= values[roman_num[i + 1]]):  # Check if the character at index i is more or equal to the character following it 
                decimal_num += values[roman_num[i]]           # Add the integer value at the key of the character at the index i from the dict values to the integer f_num_int    
        else:
            decimal_num += values[roman_num[i]]  
    print(f'Value of {roman_num} : {decimal_num}')
    return decimal_num
def get_operator():
    ''' This function asks one of this five algebric operators(*,/,+,-,^), and return it.
        If it receives an invalid operator it asks for another one until it gets a valid one.
    '''
    i_operator = input('Enter an operator(*,/,+,-,^): ')
    while i_operator not in op_list:
        print('Invalid operator entered!')
        i_operator = input('You can only enter one of the following operator(*,/,+,-,^):')
        
    print(f'Operator : {i_operator}')
    return i_operator
def do_arithmetic(num1, num2, operator):
    ''' This function takes three arguments, two decimal numbers and an operator. 
        Then It applies the operation entered to the two numbers and returns the result and the remainder.
    '''
    decimal_result = 0
    decimal_remainder = 0   
    if operator == '+':
        decimal_result += (num1 + num2) 
        return decimal_result, decimal_remainder, num1, num2       
    elif operator == '-':
        decimal_result += (num1 - num2) 
        return decimal_result, decimal_remainder, num1, num2  
    elif operator == '/':
        decimal_result += (num1 // num2) 
        decimal_remainder += num1 % num2 
        return decimal_result, decimal_remainder, num1, num2  
    elif operator == '*':
        decimal_result += (num1 * num2)
        return decimal_result, decimal_remainder, num1, num2
    elif operator == '^':
        decimal_result += (num1 ** num2)
        return decimal_result, decimal_remainder, num1, num2
def d_result_print(result, remainder, operator, num1 = None, num2 = None):
    ''' This function takes as arguments two integers a result and a remainder, a string(operator),
        and two other integers(num1, num2). It first check if the result is in the result is in the 
        range from  1 to 3999. If it is not it prints an error message and exits the function. If it is
        it prints the result and the remainder accordingly.
    '''
    if (result < 0):
        print('This arithmetic operation will result in a negative number'\
              '\nNegative numbers cannot be expressed as a Roman numeral. ')
        return None
    elif (result == 0):
        print('This arithmetic operation will result in zero'\
              '\nZero cannot be expressed as a Roman numeral')
        return None
    elif (result > 3999):
        print('This arithmetic operation will result in a number out of range'\
              '\nThis program can only convert numbers from 1 to 3999.')
        return None
    if operator == '+' or operator == '-':
        print(f'Decimal sum is: {result}')
    elif operator == '/':
        if remainder > 0:
            print(f'Decimal quotient is: {result} and the remainder is: {math.ceil(remainder)}') 
        else:
            print(f'Decimal quotient is: {result}')
    elif operator == '*':
        print(f'Decimal product is: {result}')
    elif operator == '^':
        print(f'Decimal result for {num1} raised to the power of {num2 }: {result}')
def convert_to_roman(num):
    ''' This function takes in an integer num, converts it into Roman numerals, and return it.
    '''
    roman_result = ''
    while (num > 0) and (num <= 3999):             
        while num >= 1000:
            roman_result += 'M'
            num -= 1000
        while num < 1000 and num >= 900:
            roman_result += 'CM'
            num -= 900
        while num >= 500:
            roman_result += 'D'
            num -= 500
        while num < 500 and num >= 400:
            roman_result += 'CD'
            num -= 400
        while num >= 100:
            roman_result += 'C'
            num -= 100
        while num < 100 and num >= 90:
            roman_result += 'XC'
            num -= 90
        while num >= 50:
            roman_result += 'L'
            num -= 50
        while num < 50 and num >= 40:
            roman_result += 'XL'
            num -= 40
        while num >= 10:
            roman_result += 'X'
            num -= 10
        while num >= 9:
            roman_result += 'IX'
            num -= 9
        while num >= 5:
            roman_result += 'V'
            num -= 5
        while num == 4:
            roman_result += 'IV'
            num -= 4
        while num >= 1:
            roman_result += 'I'
            num -= 1
    return roman_result
def return_roman(num1, num2):
    ''' This function takes in two integers num1 and num2, converts them into Roman numerals,
        and return them.
    '''
    if num1 == '':         #If the result is an empty string(meaning the algebric operation resulted in an error), stop the function
        return 
    else:
        return convert_to_roman(num1), convert_to_roman(num2)
def r_num_print(result, remainder, operator):
    ''' This function takes in three strings, two Roman numerals and an operator.
        And it outputs the result and remainder according to the operator.
    '''
    if result == '':       #If the result is an empty string(meaning the algebric operation resulted in an error), stop the function
        return 
    if operator == '+' or operator == '-' :
        print(f'Roman sum is: {result}')
    elif operator == '/':
        if remainder != '':
            print(f'Roman quotient is: {result} and Roman remainder is: {remainder}')
        else:
            print(f'Roman quotient is: {result}')
    elif operator == '*':
        print(f'Roman product is: {result}')
    elif operator == '^':
        print(f'Roman result: {result}')
    
sentinal = ''  

while sentinal != 'q':

    roman_num1 = get_roman_num()
    decimal1 = convert_roman_num(roman_num1)
    roman_num2 = get_roman_num()
    decimal2 = convert_roman_num(roman_num2)
    operation = get_operator()
    op_result, op_remainder, num1, num2 = do_arithmetic(decimal1, decimal2, operation)
    if do_arithmetic(decimal1, decimal2, operation) == None:    #If the algebric operation result to an error, restart the program
        break
    d_result_print(op_result, op_remainder, operation, num1, num2)
    roman_result, roman_remainder = return_roman(op_result, op_remainder)
    r_num_print(roman_result, roman_remainder, operation)
    
    sentinal = input('Type "c" to restart the program or type "q" to quit: ')