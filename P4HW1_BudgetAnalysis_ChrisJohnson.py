#Budget analysis
#10/28/2018
#CTI-110 P4HW1- Budget Analysis
#Chris Johnson
#

userBudget = float(input("Please enter how much you've budgeted" + \
                         "for the month: "))
moreExpenses = "y"
totalExpenses = 0

while moreExpenses == "y":
    userExpense = float(input( "Enter an expense: " ) )
    totalExpenses += userExpense
    moreExpenses = input( "Do you have more expenses?: Type y "+ \
                          "for yes, any key for no: " )
if totalExpenses > userBudget:
    print( "You were over your budget of" ,userBudget,"by",totalExpenses - \
           userBudget )
elif userBudget > totalExpenses:
     print( "You were under your budget of" ,userBudget,"by",userBudget - \
           totalExpenses )
else:
    print( "You used exactly your budget of", userBudget,".")
    
    
    
