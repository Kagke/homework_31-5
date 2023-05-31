def return_10():
    return 10

def add(num_1,num_2):
    sum = num_1 + num_2
    return sum

def subtract(num_1,num_2):
    sum = num_1 - num_2
    return sum

def multiply(num_1,num_2):
    sum = num_1 * num_2
    return sum

def divide(num_1,num_2):
    sum = num_1 / num_2
    return sum

def length_of_string(string):
    length=len(string)

    return int(length)

def join_string(str_1,str_2):
    joined_strs= str_1 + str_2
    return joined_strs

def add_string_as_number(string1 , string2):
    result_of_strings=int(string1) + int(string2)
    return result_of_strings

def number_to_full_month_name(number):
    months=["January","Febuary","March","April","May","June","July","August","September","Octomber","November","December"]
    finale_month=months[number -1]
    return finale_month

def number_to_short_month_name(number):
    months=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sept","Oct","Nov","Dec"]
    finale_month=months[number -1]
    return finale_month