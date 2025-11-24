import tkinter
from tkinter import messagebox

#Definining the check eligibility box
def check_eligibility():

    try:
        name = entry_name.get()
        age = int(entry_age.get())
        loans_taken = int(entry_loans_taken.get())
        annual_income = float(entry_annual_income.get())
        amount_of_loan = int(entry_amount_of_loan.get())
        loan_years = int(entry_loan_years.get())
        credit_score = int(entry_credit_score.get())
        #All the conditions for loan eligibility
        #Loan Eligibility Checker
        if age < 20 or age > 60 :
            result = "Sorry, You are ineligible due to either overage or underage"
        elif loans_taken > 10:
            result = "Sorry, You are ineligible since maximum amount of loans taken in last two years reached"
        elif annual_income < 150000:
            result = "Sorry, You are ineligible since your annual income is too low"
        elif amount_of_loan > 5 * annual_income:
            result = "Sorry, You are ineligible since your requested amount is too high"
        elif loan_years > 30:
            result = "Sorry, You are ineligible since the maximum loan term exceeded"
        elif credit_score < 400:
            result = "Sorry, You are ineligible since your credit score is too low"
        else:
            result = "Congratulations!!!!, You are Eligible for the loan"
        messagebox.showinfo("Result Of Loan Eligibility", result)
    except (ValueError, NameError):
            messagebox.showerror("Input Error", "Please enter valid numbers and alphabets in all the given fields")
root = tkinter.Tk()
root.title("Loan Eligibilty Checker")

# Assigning the rows and columns for all the conditions
tkinter.Label(root, text="Name-").grid(row=0, column=0, padx=7, pady=7)
entry_name = tkinter.Entry(root)
entry_name.grid(row=0, column=1, padx=7, pady=7)
tkinter.Label(root, text="Age-").grid(row=1, column=0, padx=7, pady=7)
entry_age = tkinter.Entry(root)
entry_age.grid(row=1, column=1, padx=7, pady=7)
tkinter.Label(root, text="Loans taken(Last 2 Years)-").grid(row=2, column=0, padx=7, pady=7)
entry_loans_taken = tkinter.Entry(root)
entry_loans_taken.grid(row=2, column=1, padx=7, pady=7)
tkinter.Label(root, text="Annual_Income-").grid(row=3, column=0, padx=7, pady=7)
entry_annual_income = tkinter.Entry(root)
entry_annual_income.grid(row=3, column=1, padx=7, pady=7)
tkinter.Label(root, text="Desired_Loan_Amount-").grid(row=4, column=0, padx=7, pady=7)
entry_amount_of_loan = tkinter.Entry(root)
entry_amount_of_loan.grid(row=4, column=1, padx=7, pady=7)
tkinter.Label(root, text="Loan Term(in years)-").grid(row=5, column=0, padx=7, pady=7)
entry_loan_years = tkinter.Entry(root)
entry_loan_years.grid(row=5, column=1, padx=7, pady=7)
tkinter.Label(root, text="Credit_Score-").grid(row=6, column=0, padx=5, pady=5)
entry_credit_score = tkinter.Entry(root)
entry_credit_score.grid(row=6, column=1, padx=5, pady=5)
tkinter.Button(root, text="Check_Eligibility", command=check_eligibility).grid(row=7, columnspan=3, pady=12)
root.mainloop()                                
