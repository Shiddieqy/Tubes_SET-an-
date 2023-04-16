import CoolProp.CoolProp as CP

#kondisi inlet dan outlet
T_inlet = 12
# T_outlet = 7
# T_outlet = 7 + 0.4
T_outlet = 7 - 0.4

#Suhu lingkungan (jakarta)
T_env = 34


#Parameter titik 1
T1 = T_env + 10 + 273.15
P1 = CP.PropsSI('P', 'T', T1, 'Q', 0, 'R134a')
H1 = CP.PropsSI('H', 'T', T1, 'Q', 0, 'R134a')

#Parameter titik 3
T3 = T_outlet-3+273.15
P3 = CP.PropsSI('P', 'T', T3, 'Q', 1, 'R134a')
H3 = CP.PropsSI('H', 'T', T3, 'Q', 1, 'R134a')
S3 = CP.PropsSI('S', 'T', T3, 'Q', 1, 'R134a')

#Parameter titik 2
H2 = H1
P2 = P3

#Parameter titik 4
S4 = S3
P4 = P1
H4 = CP.PropsSI('H', 'P', P4, 'S', S4, 'R134a')

#Kalkulasi COP dan kW/ton
ER = H3-H2
Wcp = H4-H3
Q = H4-H1
COP = ER/Wcp
KWton = 12/(COP*3.412)




print("h1 :",H1, "P1 = ",P1)
print("h2 :",H2, "P2 = ",P2)
print("h3 :",H3, "P3 = ",P3)
print("h4 :",H4, "P4 = ",P4)
print("COP :",COP)
print("kW/ton :",KWton)
print(ER)
