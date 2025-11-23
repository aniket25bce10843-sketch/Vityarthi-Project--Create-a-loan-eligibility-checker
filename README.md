# Vityarthi-Project--Create-a-loan-eligibility-checker
# Create A Loan Eligibility Checker
# 1- Overview of the project
## The loan eligibility checker is a desktop Graphical User Interface (GUI) application developed using python. It helps the users to quickly check whether the user is eligibile for the loan or not based on specific conditions. This system takes various inputs such as age, Loan taken(in last two years), annual income, amount of loan, loan years (the time period of loan) and credit score which helps to give an instant eligibility result.
---
# 2- Features
## There are various features-:
## 1- User Friendly Interface- This is made by using the built in tkinter which is more clean form based layout.
## 2- Error Handling- It detects all the invalid inputs by the use like letters in number fields and also it alerts and notify the user.
## 3- Validation- It also check the multiple conditions like age limit which is between 20 years to 60 years, Loan taken(in last two years), Annual Income, Amount of loan, loan years (the time period of loan) and credit score.
## 4- Fast Feedback- It provides the feedback immediately with the help of messagebox and it also explains exactly why the loan is rejected.
---
# 3- Technologies/Tools Used
## The tools used are as follows-:
## 1- The programming language used is (Python 3.13 64-bit)
## 2- The GUI library used is Tkinter which is a standard Python GUI library
## 3- The module used is 'messagebox' used for alert or to notify 
---
# 4- Steps to Install and Run the Project
## The steps are as follows:
## 1- Essential Condition- You have to ensure that Python is installed in the system. 
## 2- Downloading The Code - You have to copy this repository or download the python file.
## 3- Run the application
## a- Open your command prompt.
## b- Navigate to the folder containing the script.
## c- After that run the code.
---
# 5- Instructions for testing
## Input the data and click on 'Check_Eligibility', it will show the result if all the input variables are in the correct type
## Test Case-1 (Eligible)
## Name- Madhav
## Age- 25
## Loans taken(Last 2 Years)-2
## Annual_Income-2000000
## Desired_Loan_Amount-1000000
## Loan Term(in years)- 10
## Credit_Score- 700
## Result- "Congratulations!!!!, You are Eligible for the loan"
---
## Test Case-2 (Ineligible due to age)
## Name- Aniket Dev
## Age- 18
## Loans taken(Last 2 Years)- 0
## Annual_Income- 1000000
## Desired_Loan_Amount- 500000
## Loan Term(in years)- 5
## Credit_Score-520
## Result- "Sorry, You are ineligible due to either overage or underage"
---
## Test Case-3 (Ineligible due to loans taken)
## Name- Sunil
## Age- 32
## Loans taken(Last 2 Years)- 12
## Annual_Income- 1500000
## Desired_Loan_Amount- 400000
## Loan Term(in years)- 7
## Credit_Score- 650
## Result- "Sorry, You are ineligible since maximum amount of loans taken in last two years reached"
---
## Test Case-4 (Ineligible due to annual income)
## Name- Naman
## Age- 29
## Loans taken(Last 2 Years)- 5
## Annual_Income- 100000
## Desired_Loan_Amount- 400000
## Loan Term(in years)- 10
## Credit_Score- 500
## Result- "Sorry, You are ineligible since your annual income is too low"
---
## Test Case-5 (Ineligible due to desired loan amount)
## Name- Prakhar
## Age- 27
## Loans taken(Last 2 Years)- 0
## Annual_Income- 200000
## Desired_Loan_Amount- 2000000
## Loan Term(in years)- 10
## Credit_Score- 550
## Result- "Sorry, You are ineligible since your requested amount is too high"
---
## Test Case 6 (Ineligible due to loan term)
## Name- Vinay
## Age- 51
## Loans taken(Last 2 Years)- 4
## Annual_Income- 1500000
## Desired_Loan_Amount- 4000000
## Loan Term(in years)- 35
## Credit_Score- 750
## Result- "Sorry, You are ineligible since the maximum loan term exceeded"
---
## Test Case 7 (Ineligible due to credit score)
## Name- Arnav
## Age- 44
## Loans taken(Last 2 Years)- 1
## Annual_Income- 400000
## Desired_Loan_Amount- 250000
## Loan Term(in years)- 20
## Credit_Score- 250
## Result- "Sorry, You are ineligible since your credit score is too low"
---
### Test Case 8 (Input Errors)
## Name- Mridul
## Age- 55
## Loans taken(Last 2 Years)- 5
## Annual_Income- abcd
## Desired_Loan_Amount- 500000
## Loan Term(in years)- 10
## Credit_Score- 450
## Result- "Please enter valid numbers and alphabets in all the given fields"
---
## Screenshot
## <img width="1127" height="523" alt="Screenshot 2025-11-23 153541" src="https://github.com/user-attachments/assets/0f631643-ed04-43da-91d4-5a9f6f6b2df1" />
## <img width="1119" height="533" alt="Screenshot 2025-11-23 153314" src="https://github.com/user-attachments/assets/053df9db-2628-41c9-8bc1-eb00e569c589" />
## <img width="1169" height="598" alt="Screenshot 2025-11-23 153832" src="https://github.com/user-attachments/assets/079e899b-14df-4dae-9a3a-0dbcccb3367d" />
## <img width="1173" height="561" alt="Screenshot 2025-11-24 012422" src="https://github.com/user-attachments/assets/da08ad26-ce7e-4596-b426-61990ac755a0" />
## <img width="1036" height="553" alt="Screenshot 2025-11-23 155136" src="https://github.com/user-attachments/assets/b6480d58-39f5-4dca-a3e7-4dd6c27ec128" />
## <img width="1133" height="597" alt="Screenshot 2025-11-23 155244" src="https://github.com/user-attachments/assets/6c7b513b-4758-4cff-af6f-e856a91f7da4" />
## <img width="1003" height="552" alt="Screenshot 2025-11-23 155358" src="https://github.com/user-attachments/assets/ba503748-b37a-425a-8cc4-e60f182be069" />
## <img width="1085" height="506" alt="Screenshot 2025-11-24 015358" src="https://github.com/user-attachments/assets/924c7468-d44e-48ab-be92-a0a582c5ba2d" />
