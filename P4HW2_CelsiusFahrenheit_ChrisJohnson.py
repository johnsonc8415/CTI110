#Celsius to Fahrenheit Table
#10/28/2018
#CTI-110 P4HW2 - Celsius to Fahrenheit Table
#Chris Johnson
#

#F = ( 9 / 5)C + 32
print( "Celsius temperature\tFahrenheit Equivalent" )
for currentCelsiusTemperature in range(21):
    fahrenheitTemperatureEquivalent = (9 / 5) * currentCelsiusTemperature + 32
    print( currentCelsiusTemperature,"\t\t\t\t", \
           format(fahrenheitTemperatureEquivalent, ".1f") )
