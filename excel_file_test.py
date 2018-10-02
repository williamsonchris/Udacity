import pandas as pd

file = 'TRQ - Fake Data for Sorting Algorithm.xlsx'

xl = pd.ExcelFile(file)
testing = pd.read_excel('TRQ - Fake Data for Sorting Algorithm.xlsx', sheet_name=None)
test_var = pd.read_csv(xl)

print(testing.head())
