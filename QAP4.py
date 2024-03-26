# Description: One Stop Insurance Company program to enter and calculate new insurance policy information for its customers
# Author: Daniel Bowers
# Date: 2024-03-20


# imports
import datetime as DT
# Set up current date
dateNow = DT.datetime.now()


# Constants
POLICY_NUM = 1944
BASIC_PREM = 869.00
ADDIT_CARS_DIS = 0.25
EXTRA_LIAB_COV = 130.00
GLASS_COV_COST = 86.00
LOANER_CARCOV_COST = 58.00
HST_RATE = 0.15
MONTHLY_PAY_PROC_FEE = 39.99


#Start main program while True loop
while True:
 
# Inputs/ Validations (all of these will be their own while True loops, ending on a else: break):
 
# Customer First Name (validation: not blank)
    
    while True:  
        FirstName =      input("Enter the first name (Press 1 to exit program):                 ").title()
        if FirstName == "1":
            exit()
        elif FirstName == "":
            print("Invalid entry - First name can't be empty.")
        else:
            break

 
# Customer Last Name (validation: not blank)
                
    while True:
        LastName =       input("Enter the last name:                                            ").title()
        if LastName == "":
            print("Invalid entry - Last name can't be empty.")
        else:
            break 
 
# Phone Number (validations: not blank, isdigit, must be 10 characters)
    
    while True:
        PhoneNum =       input("Please enter the Customer's Phone Number (0000000000):          ")
 
        if PhoneNum == "":
            print("Customer's Phone Number cannot be Blank - Please Re-enter.")
        elif PhoneNum.isdigit() == False:
            print("Customer's Phone Number can only Contain Numbers (0000000000) - Please Re-enter.")
        elif len(PhoneNum) != 10:
            print("Customer's Phone Number must be 10 Digits Long (0000000000) - Please Re-enter.")
        else:
            break
        
 
# Street Address (validation: not blank)
    while True:
        Address =        input("Enter the address:                                              ").title()
        if Address == "":
            print("Invalid entry - Address can't be empty.")
        else:
            break 
 
# City (validation: not blank)
    while True:
        City =           input("Enter the City:                                                 ").title()
        if City == "":
            print("Invalid entry - City can't be empty.")
        else:
            break 
 
# Province (Copy from Maurice's code)
    
    ProvLst = ["NL", "NS", "NB", "PE", "PQ", "ON", "MB", "AB", "BC", "NT", "YT", "NV", "SK"]
    while True:
        Prov =           input("Enter the customer province (XX):                               ").upper()
        if Prov == "":
            print("Error - cannot be blank.")
        elif len(Prov) != 2:
            print("Error - must be 2 characters only.")
        elif Prov not in ProvLst:
            print("Error - Invalid province.")
        else:
            break
 
# Postal Code (validations: not blank, must be 6 characters)
    while True:
        PostalCode =     input("Enter Postal Code (A1A1A1):                                     ").upper()
 
        if PostalCode == "":
            print("Postal Code cannot be Blank (A1A1A1) - Please Re-enter.")
        elif len(PostalCode) != 6:
            print("Postal Code must be 6 characters - Please Re-enter.")
        else:
            break
 
# Number of Cars (validations: try/except that only allows int, not 0)
    while True:
        try:
            NumCars =    int(input("Enter the number of cars:                                       "))
        except:
            print("Invalid entry - Must be a numeric value")
        else:
            if NumCars == 0:
                print("Number of cars cannot be zero")
            else:
                break
        

# Extra Liability (validations: not blank, must be Y or N)
    while True:
        ExtraLiab =      input("Would you like extra liability insurance? Y/N:                  ").upper()
        if ExtraLiab == "":
            print("Invalid entry - Input cannot be blank: ")
        elif ExtraLiab != "Y" and ExtraLiab != "N":
            print("Invalid entry - Must be Y or N")
        else:
            break
 
# Glass Coverage (validations: not blank, must be Y or N)
    while True:
        GlassCov =       input("Would you like glass coverage? Y/N:                             ").upper()
        if GlassCov == "":
            print("Invalid entry - Input cannot be blank: ")
        elif GlassCov != "Y" and GlassCov != "N":
            print("Invalid entry - Must be Y or N")
        else:
            break
 
# Loaner (validations: not blank, must be Y or N)
    while True:
        OptLoanerCar =   input("Would you like an extra loaner car? Y/N:                        ").upper()
        if OptLoanerCar == "":
            print("Invalid entry - Input cannot be blank: ")
        elif OptLoanerCar != "Y" and OptLoanerCar != "N":
            print("Invalid entry - Must be Y or N")
        else:
            break
 
# Payment Options (validations: not blank, must be F or M)
    PayOptList = ["F", "M", "D"]
    while True:
        PaymentOption =  input("Would you like to pay in full, monthly or down payment? F/M/D:  ").upper()
        if PaymentOption == "":
            print("Invalid entry - Input cannot be blank: ")
        elif PaymentOption not in PayOptList:
            print("Invalid entry - Must be F, M or D")
        elif PaymentOption == "D":
            DwnPayAmt = float(input("Enter the down payment amount: "))
            break
        else:
            break
        
    PriorClaims = []
    while True:
        ClaimNum =       input("Enter a previous claim number or (Press enter to finish):       ")
        if not ClaimNum:
            break
        ClaimDate =      input("Enter the previous claim date, (YYYY-MM-DD):                    ")
        ClaimAmt = float(input("Enter the claim amount:                                         "))
        PriorClaims.append((ClaimNum, ClaimDate, ClaimAmt))
        
# Calculations
    if NumCars == 1:
        InsurancePrem = BASIC_PREM
    else: 
        InsurancePrem = BASIC_PREM + (BASIC_PREM * ADDIT_CARS_DIS) * (NumCars - 1)

    if ExtraLiab == "Y":
        ExtraLiabCost = EXTRA_LIAB_COV * NumCars
        ExtraLiabDSP = "Yes"
    else:
        ExtraLiabCost = 0 
        ExtraLiabDSP = "No"

    if GlassCov == "Y":
        GlassCovCost = GLASS_COV_COST * NumCars
        GlassCovDSP = "Yes"
    else:
        GlassCovCost = 0
        GlassCovCostDSP = "No"
 

    if OptLoanerCar == "Y":
        OptLoanCarCost = LOANER_CARCOV_COST * NumCars
        OptLoanCarDSP = "Yes"
    else:
        OptLoanCarCost = 0
        OptLoanCarDSP = "No"

    ExtraCosts = ExtraLiabCost + GlassCovCost + OptLoanCarCost
    TotPremInsur = InsurancePrem + ExtraCosts
    Hst = TotPremInsur * HST_RATE
    TotalCost = TotPremInsur + Hst

    if PaymentOption == "D":
        MonthlyPayment = (TotalCost + MONTHLY_PAY_PROC_FEE - DwnPayAmt) / 8
    else:
        MonthlyPayment = (TotalCost + MONTHLY_PAY_PROC_FEE) / 8
    
    if PaymentOption == "M":
        TotPayAmt = MonthlyPayment
    else:
        TotPayAmt = TotalCost

    InvoiceDate = dateNow
    NextMonth = InvoiceDate.month + 1
    NextYear = InvoiceDate.year
    if NextMonth > 12:
        NextMonth = 1
        NextYear += 1
    FirstPayDate = DT.datetime(NextYear, NextMonth, 1)
    
# Formatting
    CustName = FirstName + " " + LastName
    PolicyNum = str(POLICY_NUM)
    NumCarsDSP = str(NumCars)
    MonthlyPaymentDSP = "${:,.2f}".format(MonthlyPayment)
    InsurancePremDSP = "${:,.2f}".format(InsurancePrem)
    ExtraLiabCostDSP = "${:,.2f}".format(ExtraLiabCost)
    GlassCovCostDSP = "${:,.2f}".format(GlassCovCost)
    OptLoanCarCostDSP = "${:,.2f}".format(OptLoanCarCost)
    InsurancePremDSP = "${:,.2f}".format(InsurancePrem)
    ExtraCostsDSP = "${:,.2f}".format(ExtraCosts)
    TotPremInsurDSP = "${:,.2f}".format(TotPremInsur)
    HstDSP = "${:,.2f}".format(Hst)
    TotalCostDSP = "${:,.2f}".format(TotalCost)
    TotPayAmtDSP = "${:,.2f}".format(TotPayAmt)
    FirstPayDateDSP = FirstPayDate.strftime("%Y-%m-%d")
  
 
# Display all formatted values, calculations and inputs.
    print()
    print("-" * 46)
    print("      One Stop Insurance Company")
    print(f"          Policy Number: {PolicyNum} ")
    print("-" * 46)
    print(f"Invoice date: {dateNow}")
    print(f"Customer name: {FirstName} {LastName}")
    print(f"Customer address: {Address}")
    print(f"Customer location: {City}, {Prov}, {PostalCode}")
    print("-" * 46)
    print(f"Number of cars: {NumCarsDSP}")
    print(f"Extra liability coverage: {ExtraLiabDSP}")
    print(f"Extra liability cost: {ExtraCostsDSP}")
    print(f"Extra glass coverage: {GlassCovDSP}")
    print(f"Extra glass coverage cost: {GlassCovCostDSP}")
    print(f"Extra loaner car: {OptLoanCarDSP}")
    print(f"Extra loaner car cost: {OptLoanCarCostDSP}")
    print("-" * 46)
    print(f"Payment type: {PaymentOption}")
    print(f"Monthly payment amount: {MonthlyPayment:<2f}")
    print(f"First payment date {FirstPayDateDSP}")
    print(f"Total extra costs: {ExtraCostsDSP}")
    print(f"Insurance premiums cost: {InsurancePremDSP}")
    print("-" * 46)
    print(f"Subtotal: {TotPremInsurDSP}")
    print(f"Taxes {HstDSP}")
    print(f"Total cost: {TotalCostDSP}")

    





    

    print()
    if PaymentOption == "M":
        print(f"Monthy payment {TotPayAmtDSP}")
        print(f" First payment due {FirstPayDateDSP}")
    print("    Claim #   Claim Date   Claim Amount")
    print("-" * 46)
    for claim in PriorClaims:
        print(f"     {claim[0]}      {claim[1]}   {claim[2]}")



    POLICY_NUM += 1
    print()
    

    

 
 
# Update Policy Number
 
# while True loop to process another claim or exit.