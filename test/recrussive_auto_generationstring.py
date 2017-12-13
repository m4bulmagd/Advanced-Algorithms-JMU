from random import choice
from string import ascii_lowercase
from datetime import datetime


current_time = datetime.now()

lenght_first_string = int(input("enter length for first string   "))

string_val = "".join(choice(ascii_lowercase) for i in range(lenght_first_string))
print("first string auto generated with length " , lenght_first_string,"  :  " , string_val)
_1st=(string_val)

lenght_second_string = int(input("enter length for second string   "))

string_val2 = "".join(choice(ascii_lowercase) for i in range(lenght_second_string))
print("second string auto generated with length  " , lenght_second_string , ": ",string_val2)
_2nd=(string_val2)


def editDistanceRL(str1, str2, m, n):
    # if 1st String is empty ED will be the length of 2nd string ( insert all chars )
    if m == 0:
        return n

    # if 2nd String is empty ED will be the length of 1nd string ( remove all chars )
    if n == 0:
        return m

    # If last characters of two strings are same, move to the next chars .
    if str1[m - 1] == str2[n - 1]:
        return editDistanceRL(str1, str2, m - 1, n - 1)

    # if the two chars are not equal to each other then do the three Opreation and return the minimum cost for all three operations recursivly
    return 1 + min(editDistanceRL(str1, str2, m, n - 1),  # Insert
                   editDistanceRL(str1, str2, m - 1, n),  # Remove
                   editDistanceRL(str1, str2, m - 1, n - 1))  # Replace

print("ED=  ",editDistanceRL(_1st, _2nd, len(_1st), len(_2nd)))
time_finish = datetime.now()
print("processing time =", time_finish - current_time)
