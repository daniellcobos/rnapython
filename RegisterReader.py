import pandas as pd

register = pd.read_excel(r'C:\Users\RegistroNacional\Documents\rnabases\rnapython\c.xlsx')
register.columns = [c.replace(' ', '_') for c in register.columns]
registerN = register[register.Nat_o_Jurid == 'N']
registerNexams = registerN[['Especialidad_1', 'URB_Otorgamiento', 'URB_Vencimiento',
       'URB_Renovación', 'URB_Vencimiento_2', 'Cod_URB', 'Especialidad_2',
       'RUR_Otorgamiento', 'RUR_Vencimiento', 'RUR_Renovación',
       'RUR_Vencimiento_2', 'Cod_RUR', 'Especialidad_3', 'MYE_Otorgamiento',
       'MYE_Vencimiento', 'MYE_Renovación', 'MYE_Vencimiento_2', 'Cod_MYE',
       'Especialidad_4', 'Especialidad_5', 'ESP_Otorgamiento',
       'ESP_Vencimiento', 'ESP_Renovación', 'ESP_Vencimiento_2', 'Cod_ESP',
       'Especialidad_6', 'INTES_URB_Otorgamiento', 'INTES_URB_Vencimiento',
       'Cod_INTES_URB', 'INTES_RUR_Otorgamiento', 'INTES_RUR_Vencimiento',
       'Cod_INTES_RUR', 'INTES_MYE_Otorgamiento', 'INTES_MYE_Vencimiento',
       'Cod_INTES_MYE', 'INTES_ESP_Otorgamiento', 'INTES_ESP_Vencimiento',
       'Cod_INTES_ESP']]
print (registerNexams)