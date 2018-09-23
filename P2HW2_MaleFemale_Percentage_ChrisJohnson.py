#Tutorial male and female percentages
#9/23/18
#CTI-110 P2HW2 - Male Female Percentage
#Chris Johnson
#
# Ask for the user to input the number of males and females in a class
# The program will display the percentage of males and females in the class

males = int( input( "Enter the number of males in the class: ") )
females = int( input( "Enter the number of females in the class: ") )
totalStudents = males + females

malePercentage = ( males / totalStudents ) * 100
femalePercentage = ( females / totalStudents ) * 100

print( "Male percentage: " + str( malePercentage ) )
print( "Female percentage: " + str( femalePercentage ) )



