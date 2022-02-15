import pandas as pd

register = pd.read_excel(r'C:\Users\RegistroNacional\Documents\rnabases\rnapython\c.xlsx')
register.columns = [c.replace(' ', '_') for c in register.columns]
registerN = register[register.Nat_o_Jurid == 'N']
print (registerN)