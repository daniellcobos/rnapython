
from datetime import datetime
import pandas as pd

register = pd.read_excel(r'C:\Users\RegistroNacional\Documents\rnabases\rnapython\c.xlsx')
register.columns = [c.replace(' ', '_') for c in register.columns]
registerJ = register[register.Nat_o_Jurid == 'J']
registerJ = registerJ[['Prefijo',
'Matrícula','Persona_Natural_Apellido_1' 
,'Persona_Jurídica_Nombre','Representante_Legal_Apellido_1','Representante_Legal_Apellido_2'
,'Representante_Legal_Nombres','Celular','Dirección','Consejo_regional'
,'Ciudad']]
print(registerJ)