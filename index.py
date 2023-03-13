

# Income
    #rental income -$2000
    #laundry  income -$0
    #storage -$0
        # Total Inmcome $2000 per month


    #purchase home $200,000

# Expenses
    # Tax - $150 pm
    # Insurance -$100 pm
    # Utilitiews $0.00
        # electeric, weater, sewer, gas
    # HOA - $0.00
    # Lawn/Snow - $0.00
    # Vacanmcy - $100.00 pm
    # Repairs - $100.00 pm
    # CapEX (Large items likle roof or water heater) - $100.00
    # property management - $ 200.00 pm
    # Mortgage - $860 pm 5% interest for $160,000 mortgage
        # Total monthly expenses $1,610 per month\
    
# Cash Flow
    # Income +$2000
    # Expenses - $1610
        # Total Cash Flow $390

# Cash on Cash ROI
    #Add all money put in on deal
        # Down payment - $40,000
        # Closing Cost - $3,000
        # Rehab Budget - $7,000
        # Misc. other - $ 0

        # Total Investment - $50,000

        # AnnuaL Cash Flow 390 * 12 = 4,680
        # AnnuaL Cash Flow  / Total Investment = 9.36%
            # Cash on Cash ROI = 9.36%



class calculator():

    def __init__ (self, income, expenses, cash_flow, cash_on_cash):
        self.income = {}:
        self.expenses = ():
        self.cashflow = ():
        self.cash_on_cash = ():

    def income():
        iTypes= input("Enter your type of income"):
        iAmount = input("Enter Monthly Income Amount"):
        self.income[iType] = iAmount

    
    def expenses():
        iType = input("Enter your type of expenses"):
        iAmount2 = input("Enteryour monthly expense amount"):
        self.expenses[iType] = iAmount2

    def cash_flow():
        self.cash_flow = iAmount - iAmount2


    def cash_on_cash
        sub_invest = list(self.investment.values())
        sub_invest = list(map(int, sub_invest))
        total_invest = sum(sub_invest)
        annual_cash_flow = self.cash_flow * 12
        self.roi = (annual_cash_flow / total_invest)*100

    def clearTotals(self): 
        self.income = {}
        self.expenses = {}
        self.cash_flow = {}
        self.cash_on_cash = {}
    
    def printTotals(self):
        print(f"Income: {self.income}")
        print(f"Expenses: {self.expenses}")
        print(f"Cash Flow: {self.cash_flow}")
        print(f"Cash on Cash Return on Investment: {self.cash_on_cash}% \n")

rental = calculator({}, {}, {}, {})

    def ROI(): 
    while True: 
        ask = input("\nSelect an option.\nOptions:\n{C} Clear Totals\n{I} Enter Income\n{E} Enter Expense\n{IN} Cash_on_Cash ROI\n{P} Print Totals\n{Q} Quit\n")
        if ask.lower() == "q":
            clear_output()
            print("Latest Information: ")
            rental.printTotals()
            print("Analyzer Cancelled")
            break
        elif ask.lower() == "c":
            clear_output()
            rental.clearTotals()
            rental.printTotals()
        elif ask.lower() == "i":
            clear_output()
            rental.inIncome()
        elif ask.lower() == "e":
            clear_output()
            rental.inExpenses()
        elif ask.lower() == "in":
            clear_output()
            rental.inInvest()
        elif ask.lower() == "a":
            clear_output()
            rental.calcCash()
            rental.calcROI()
            rental.printTotals()
        elif ask.lower() == "p":
            clear_output()
            rental.printTotals()
        else:
            clear_output()
            print("Try another command")


ROI()