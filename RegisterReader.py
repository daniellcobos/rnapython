
from datetime import datetime
import pandas as pd

register = pd.read_excel(r'C:\Users\RegistroNacional\Documents\rnabases\rnapython\c.xlsx')
register.columns = [c.replace(' ', '_') for c in register.columns]
registerN = register[register.Nat_o_Jurid == 'N']
registerN = registerN.dropna(subset=['Cod_URB'])
registerN = registerN[[ 'Matrícula','URB_Otorgamiento', 'URB_Vencimiento',
       'URB_Renovación', 'URB_Vencimiento_2', 'Cod_URB']]
print(registerN)
print('Cod_{type}'.format(type = 'urb'))