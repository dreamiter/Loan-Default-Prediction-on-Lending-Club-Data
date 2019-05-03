import os 
import pandas as pd

#mypath = '/Users/timxie/Downloads/Issued Loan/'
mypath = '/Users/timxie/Downloads/Rejected Loan/'

os.chdir(mypath)
df_list = []

for file in os.listdir(mypath):
    df = pd.read_csv(file, skiprows=1)
    df_list.append(df)

final_df = pd.concat(df_list)

#final_df.to_csv('issued_loan_final.csv', index=False)
final_df.to_csv('rejected_loan_final.csv', index=False)

