import csv

# with open('accounts.csv',newline='') as csv_file:
#     off_reader = csv.reader(csv_file, delimiter=',')
#     #csv reader iterates through the csv file one line at a time
#     print(next(off_reader))

import sys
sys.path
import pandas as pd 

df = pd.read_csv('accounts.csv')

print(df['Amount'])