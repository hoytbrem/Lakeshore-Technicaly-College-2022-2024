"""
This code is designed to figure out someones income with a tax rate applied

Will take the users income and the tax and multiply them together and produce and output
"""

#INPUTS
income = float(input("Enter your income: "))#does a float input to get the users income
tax_rate = float(input("Enter your tax rates: "))#does a float input to get the users tax rates
#INTERNAL MATH
tax_amount = income * tax_rate#takes the users income and tax rate and figures out the total
rounded_tax_amount = round(tax_amount, 2)#rounds whatever number they got for tax_amount and rounds it to the 2nd decimal place
#OUTPUT
print(f"Tax amount is {rounded_tax_amount}")#outputs their total