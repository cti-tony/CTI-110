#
# Goal: Calculate Meal cost, Tip and tax based off user input.
# 16 SEP 2019
# CTI-110 P2HW1 - Meal Tip Tax Calculator
# Anthony Elizalde
#
# Define all questions, it's key word and value in array called Questions
# Start
# Open Run() in Calculator class to start asking for input
# Loop(1) through Questions array asking for input
# Loop(2) validates input is not 0 and is an integer
# Loop(2) stores input as 3rd set of data in each Question array
# Loop(2) continues to next question in Loop(1)
# Run() function calls to ShowMeTheBill()
# ShowMeTheBill() performs calculation based off 'Bill' value
# ShowMeTheBill() outputs calculations for each value as a string
# ShowMeTheBill() outputs calculations for each value as a number
# ShowMeTheBill() prints the receipt
# 
#Importing requires modules
import datetime
import calendar
from datetime import date
BUSINESS_NAME = 'Tony\'s Cafe'                   #Business name
DATE = date.today()                              #Get numerical date
DAYNAME = str(calendar.day_name[DATE.weekday()]) #Get the alphabetical date
Questions = [
	["How much was the cost of your meal?", "Bill", 0],
	["How much is your state theft(tax)? Please enter a percentage.", "Tax", 0],
	["How much would you like to tip? Please enter a percentage.", "Tip", 0],
]
#Name the class
class Calculator:
    #Initializing class
    def __init__(self):
            return
    
    #Main output function
    def ShowMeTheBill(number):
            # Import global variables, defined at top of class
            global BusinessName
            global DAYNAME
            global DATE
            global Questions

            # Generating output, line by line to keep it readable
            output = '\n\n\n' #Set clear string for output
            output += BUSINESS_NAME+'\n'
            output += str(DAYNAME)+' '+str(DATE)+'\n\n'
            total = 0

            # Dumping questions/answers into output
            for each in Questions:
                # Return an ouput for each keyword
                StrSwitch = {
                        "Bill" : '$'+format(each[2], ',.2f'),
                        # Calculating total based off Questions[0][2] which is the original bill
                        "Tip" : '$'+format(Questions[0][2]*(Calculator.GetPercentage(each[2])/100), ',.2f')+' ('+str(Calculator.GetPercentage(each[2]))+'%)',
                        # Calculating total based off Questions[0][2] which is the original bill
                        "Tax" : '$'+format(Questions[0][2]*(Calculator.GetPercentage(each[2])/100), ',.2f')+' ('+str(Calculator.GetPercentage(each[2]))+'%)'
                }
                # Return a number ouput for each keyword to add to total
                IntSwitch = {
                        # Just add the bill to the total
                        "Bill" : each[2],
                        # Add the bill (Questions[0][2]) times the percentage divided by 100(%)
                        "Tip" : Questions[0][2]*(Calculator.GetPercentage(each[2])/100),
                        # Add the bill (Questions[0][2]) times the percentage divided by 100(%)
                        "Tax" : Questions[0][2]*(Calculator.GetPercentage(each[2])/100)
                }
                # Add tax/tip to total bill
                #print('Adding value: '+str(IntSwitch.get(each[1], 0))+'\n') #Debug
                total += float((IntSwitch.get(each[1], 0)))
                output +=  str(each[1])+' '
                # Return the output for each individual case
                output += ': '+str(StrSwitch.get(each[1], "Error calculating number")+'\n')


            #Hardcoded output for calculated totals
            output += '\n\n'
            output += 'Total due today: '
            output += '$'+format(total, ',.2f')+'\n'

            # Print output
            print(output)

    #Turn any number into a percentage
    def GetPercentage(num):
            # Return MAX of 100(%)
            return min(num, 100)
            
    
    #Starts up calculator
    def Run():
            # Check if name input is blank
            global questions
            #print(Questions) #Debugging
            for each in Questions:
                TryAgain = True
                while TryAgain:
                    try:
                        # Ask question
                        CurrentQuestion = input(each[0]+'\n')
                        # Convert input to integer
                        val = int(float(CurrentQuestion))
                        # Check if integer is greater than 0
                        if val > 0:
                                # Setting the 3rd value in each array to
                                # correspond with the question's input
                                each[2] = val
                                #print('IT BLOODY WORKED, MOVE ON LAD') #Debugging
                                TryAgain = False #Stop the loop from repeating
                        else:
                        #If not, prompt again
                        #print('Not >0') #Debugging
                            continue
                    except ValueError: # Not an integer
                        #print('Not int') #Debugging
                        continue
            Calculator.ShowMeTheBill(val)
            #print(Questions) #Debugging





calc = Calculator
#Call to start calculator
calc.Run()



