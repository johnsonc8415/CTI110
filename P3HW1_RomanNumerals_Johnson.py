#Python for Roman Numerals
#CTI 110
#P3HW1
#Chris Johnson
#10/5/2018
#
#Write a program that tells the use to enter a number within the range of
#1 through 10. The program should display the Roman numeral version of that
#number. If the number is outside the range of 1 through 10, the program should
#display an error message. The following table shows the Roman numerals for
# the number 1 through 10:

# Number Roman Numeral
# 1              I
# 2              II
# 3              III
# 4              IV
# 5              V
# 6              VI
# 7              VII
# 8              VIII
# 9              IX
# 10             X

userNumber = int( input( "Please enter a number" ) )
if userNumber == 1:
    print( "I" )
elif userNumber == 2:
    print( "II" )
elif userNumber == 3:
    print( "III" )

elif userNumber == 4:
    print( "IV" )
elif userNumber == 5:
    print( "V" )
elif userNumber == 6:
    print( "VI" )
elif userNumber == 7:
    print( "VII" )
elif userNumber == 8:
    print( "VIII" )
elif userNumber == 9:
    print( "X" )
elif userNumber == 10:
    print( "X" )
else:
    print( "Error: Restart the program and enter a number between" + \
           "1 and 10. " )
    

