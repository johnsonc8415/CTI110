#CTI-110
#P3HW2-Shipping Charges
#Chris Johnson
#10/5/2018
#

#The Fast Freight Shipping Company charges the following rates:
# Weight of Package                             Rate per Pound
# 2 pounds or less                                  $1.50
# Over 2 pounds but not more than 6 pounds          $3.00
# Over 6 pounds but not more than 10 pounds         $4.00
# Over 10 pounds                                    $4.75

# Write a program that asks the user to enter the weight of a package and then
#display the shipping charges.

userWeightOfPackage = int( input( "Please enter the weight of the package: " ))

if userWeightOfPackage <= 2:
    shippingCharges = 1.50
elif userWeightOfPackage < 7:
    shippingCharges = 3.00
elif userWeightOfPackage < 11:
    shippingCharges = 4.00
else:
    shippingCharges = 4.75
print( "For a package weighing " + str(userWeightOfPackage ) + \
       ", you'll pay $" + format( shippingCharges, ",.2f" ) )
    
