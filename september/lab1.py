#James Galante


print("problem 1")
#this problem prints my name, address, telephone number, and major
print("""James Galante
5 Smith Ct, Westville, NJ, 09834
908-555-4567
Computer Engineering""")

print()
print("problem 2")
#This problem asks the user to enter an amount of total sales, and then
#does the math to find the profit
tSales = input("Enter Total Sales: ")
float(tSales) 
print("Your profit is ", "$",format(float(tSales) * 0.23,',.2f'), sep='')

print()
print('Problem 3')
#this program lets the user input the total square they have and then
#converts it to aches with a simple math eqation
oneAcre = 43560
sqFeet = input("Enter total squre feet: ")
print("You have", format(float(sqFeet) / oneAcre, ',.6f'), "acres of Land")

print()
print('Problem 4')
#this program asks the user to input 5 items and then it tell them the
#amount of tax and the total price
item1 = input("What is the price of item 1 ")
item2 = input("What is the price of item 2 ")
item3 = input("What is the price of item 3 ")
item4 = input("What is the price of item 4 ")
item5 = input("What is the price of item 5 ")
tax = 0.07
salesTaxAndTotal = 1.07

subTotal = format((float(item1) + float(item2) + float(item3) + float(item4)
                   + float(item5)), ',.2f')
justTax = format(((float(item1) + float(item2) + float(item3) + float(item4)
                   + float(item5)) * tax), ',.2f')
totalWithTax = format(((float(item1) + float(item2) + float(item3)
                  + float(item4) + float(item5)) * salesTaxAndTotal), ',.2f')
print("your subtotal is ", '$', subTotal,sep='')
print("The cost of tax is ",'$', justTax ,sep='')
print("your total with tax is ",'$',totalWithTax,sep='')

print()
print('Problem 6')
#This program asks the user the price of his purchase
#then prints the state and county tax and then the final price
purchase = input("what is the price of your purchase? ")
stateTax = format(0.05 * float(purchase), '.2f')
countyTax = format(0.025 * float(purchase), '.2f')
totalTax1 = format(float(stateTax) + float(countyTax), ',.2f')
print("State Sales Tax on this is ",'$', format(float(stateTax), ',.2f'), sep='')
print("County sales tax on this is ",'$', format(float(countyTax), ',.2f'), sep='')
print("Total sales tax on this purchase is ",'$', totalTax1, sep='')
finalPrice = float(purchase) + float(stateTax) + float(countyTax)
print("Your total Cost is ", "$", format(float(finalPrice), ',.2f'),sep="")

print()
print("Problem 8")
#this program asks the user to enter the charge for the food and then
#shows the user what the tax and food are and the tax food and tip
foodMenuPrice = input("what was the price of your meal? ")
salesTax = 1.07
taxPlusFood = format(float(foodMenuPrice) * float(salesTax), '.2f')
print("tax is ", '$', format(float(foodMenuPrice) * 0.07,',.2f'), sep='')
print("Food and tax is ", '$', format(float(taxPlusFood), ',.2f'), sep='')
tip = 1.18
print("Tip is ", '$', format(float(foodMenuPrice) * 0.18,',.2f'), sep='')
taxFoodAndTip = format(float(taxPlusFood) * float(tip), ',.2f')
print("Food and tax and tip is ", '$', taxFoodAndTip, sep='')

print()
print('Problem 10')
#this program detremines the amount of ingrediants based on 48 cookie
#recipe and then displays it for the user
sugarPer48 = 1.5
butterPer48 = 1
flourPer48 = 2.75
cookiesInABatch = 48
disiredCookies = input("How many cookies do you want? ")
multiplyFactor = float(disiredCookies) / float(cookiesInABatch)
amountSugar = format(float(sugarPer48) * float(multiplyFactor), ',.2f')
amountButter = format(float(butterPer48) * float(multiplyFactor), ',.2f')
amountFlour = format(float(flourPer48) * float(multiplyFactor), ',.2f')
print("The ingrediant amounts you need are: ")
print(amountSugar, "cups of sugar")
print(amountButter, "cups of Butter")
print(amountFlour, "cups of Flour")


print()
print('Problem 11')
#this program asks the user for the amount of males and females
#in a class and then prints out the percentage of each
totalMales = input('How many males are in your Class? ')
totalFemales = input('How many females are in your Class? ')
totalStudents = int(totalMales) + int(totalFemales)
percentMale = format((int(totalMales) / int(totalStudents)) * 100, '.2f')
percentFemale = format((int(totalFemales) / int(totalStudents)) * 100, '.2f')
print(percentMale,"%", " males in your class", sep='')
print(percentFemale, "%", " females in your class", sep='')




