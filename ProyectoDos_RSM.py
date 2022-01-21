import matplotlib
import matplotlib.pyplot as plt
import re 

#Si era ingresando los datos desde la terminal
apig = int ( input("Ingresa los grados API: ") )
visc = int ( input("Ingresa la viscosidad [cP]: ") )
comp = int ( input("Ingresa la clasificación de la composición: ") )
so = int ( input("Ingresa la saturación de aceite [PV]: ") )
tf = str ( input("Ingresa el tipo de formación: ") )
hn = int (input("Ingresa el espesor neto [m]: ") )
k = int ( input("Ingresa la permeabilidad: ") )
prof = int ( input("Ingresa la profundidad [m]: ") )
t = int ( input("Ingresa la temperatura [°C]: ") )

#Inyección de Hidrocarburo
coincidenciaHC = 0
PtHC = 0
coincidenciaHC1 = 0
PtHC1 = 0
coincidenciaHC2 = 0
PtHC2 = 0
coincidenciaHC3 = 0
PtHC3 = 0
coincidenciaHC4 = 0
PtHC4 = 0

#Inyección de CO2
coincidenciaCO = 0
PtCO = 0
coincidenciaCO1 = 0
PtCO1 = 0
coincidenciaCO2 = 0
PtCO2 = 0
coincidenciaCO3 = 0
PtCO3 = 0
coincidenciaCO4 = 0
PtCO4 = 0


#Inyección Micelar, polímeros, ASP
coincidenciaMPASP = 0
PtMPASP = 0
coincidenciaMPASP1 = 0
PtMPASP1 = 0
coincidenciaMPASP2 = 0
PtMPASP2 = 0
coincidenciaMPASP3 = 0
PtMPASP3 = 0
coincidenciaMPASP4 = 0
PtMPASP4 = 0


#Datos Campo A
apiga = 31.8
visca = 0.6892
compa = 2
soa = 68.5
tfa = "arena"
espa = 242
ka = 50
profa = 2529.1069 #En metros
tempa = 75 #En °C

#Datos Campo B
apigb = 40.6
viscb = 0.094
compb = 1
sob = 80
tfb = "carbonatos"
espb = 492 
kb = 75
profb = 5698.5408 #En metros
tempb = 150 #En °C

#Datos Campo C
apigc = 18.7
viscc = 19
compc = 2
soc = 80
tfc = "carbonatos"
espc = 1705.6
kc = 1220
profc = 3254.1667 #En metros
tempc = 121 #En °C

#Datos Campo D
apigd = 37
viscd = 0.55
compd = 1
sod = 65
tfd = "Carbonatos"
espd = 98.4
kd = 2000
profd = 549.8323 #En metros
tempd = 43.1 #En °C

#Datos Campo E
apige = 9.6
visce = 1691
compe = 4
soe = 70
tfe = "Arena"
espe = 255.84
ke = 950
profe = 784.7607 #En metros
tempe = 43 #En °C

#Inyección de gas
#Coincidencias API
#Campo A
#Hidrocarburo
if (apiga >= 23 and apiga <= 54):

    apiHC = 30
    print("Coincidencia Hidrocarburo Campo A °API, valor: ",apiHC)
    coincidenciaHC = coincidenciaHC + 1
    PtHC = PtHC + apiHC

#CO2    
elif (apiga >= 22 and apiga <= 44):

    apiCO = 30
    print("Coincidencia CO2 Campo A °API, valor: ", apiCO)
    coincidenciaCO = coincidenciaCO + 1
    PtCO = PtCO + apiCO

#Micelar, polímeros, ASP
elif (apiga >=20 and apiga <= 35):

    apiMPA = 30
    print("Coincidencia Micelar, polímeros, ASP Campo A °API, valor: ", apiMPA)
    coincidenciaMPASP = coincidenciaMPASP + 1
    PtMPASP = PtMPASP + apiMPA

#Campo B
#Hidrocarburo
if (apigb >= 23 and apigb <= 54):

    apiHC1 = 30
    print("Coincidencia Hidrocarburo Campo B °API, valor: ",apiHC1)
    coincidenciaHC1 = coincidenciaHC1 + 1
    PtHC1 = PtHC1 + apiHC1

#CO2    
elif (apigb >= 22 and apigb <= 44):

    apiCO1 = 30
    print("Coincidencia CO2 Campo B °API, valor: ", apiCO1)
    coincidenciaCO1 = coincidenciaCO1 + 1
    PtCO1 = PtCO1 + apiCO1

#Micelar, polímeros, ASP
elif (apigb >=20 and apigb <= 35):

    apiMPA1 = 30
    print("Coincidencia Micelar, polímeros, ASP Campo B °API, valor: ", apiMPA1)
    coincidenciaMPASP1 = coincidenciaMPASP1 + 1
    PtMPASP1 = PtMPASP1 + apiMPA1

#Campo C
#Hidrocarburo
if (apigc >= 23 and apigc <= 54):

    apiHC2 = 30
    print("Coincidencia Hidrocarburo Campo C °API, valor: ",apiHC2)
    coincidenciaCO2 = coincidenciaCO2 + 1
    PtHC2 = PtHC2 + apiHC2

#CO2    
elif (apigc >= 22 and apigc <= 44):

    apiCO2 = 30
    print("Coincidencia CO2 Campo C °API, valor: ", apiCO2)
    coincidenciaCO2 = coincidenciaCO2 + 1
    PtCO2 = PtCO2 + apiCO2

#Micelar, polímeros, ASP
elif (apigc >=20 and apigc <= 35):

    apiMPA2 = 30
    print("Coincidencia Micelar, polímeros, ASP Campo C °API, valor: ", apiMPA2)
    coincidenciaMPASP2 = coincidenciaMPASP2 + 1
    PtMPASP2 = PtMPASP2 + apiMPA2

#Campo D
#Hidrocarburo
if (apigd >= 23 and apigd <= 54):

    apiHC3 = 30
    print("Coincidencia Hidrocarburo Campo D °API, valor: ",apiHC3)
    coincidenciaHC3 = coincidenciaHC3 + 1
    PtHC3 = PtHC3 + apiHC3

#CO2    
elif (apigd >= 22 and apigd <= 44):

    apiCO3 = 30
    print("Coincidencia CO2 Campo D °API, valor: ", apiCO3)
    coincidenciaCO3 = coincidenciaCO3 + 1
    PtCO3 = PtCO3 + apiCO3

#Micelar, polímeros, ASP
elif (apigd >=20 and apigd <= 35):

    apiMPA3 = 30
    print("Coincidencia Micelar, polímeros, ASP Campo D °API, valor: ", apiMPA3)
    coincidenciaMPASP3 = coincidenciaMPASP3 + 1
    PtMPASP3 = PtMPASP3 + apiMPA3 

#Campo E
#Hidrocarburo
if (apige >= 23 and apige <= 54):

    apiHC4 = 30
    print("Coincidencia Hidrocarburo Campo E °API, valor: ",apiHC4)
    coincidenciaHC4 = coincidenciaHC4 + 1
    PtHC4 = PtHC4 + apiHC4

#CO2    
elif (apige >= 22 and apige <= 44):

    apiCO4 = 30
    print("Coincidencia CO2 Campo E °API, valor: ", apiCO4)
    coincidenciaCO4 = coincidenciaCO4 + 1
    PtCO4 = PtCO4 + apiCO4

#Micelar, polímeros, ASP
elif (apige >=20 and apige <= 35):

    apiMPA4 = 30
    print("Coincidencia Micelar, polímeros, ASP Campo E °API, valor: ", apiMPA4)
    coincidenciaMPASP4 = coincidenciaMPASP4 + 1
    PtMPASP4 = PtMPASP4 + apiMPA4

#Coincidencias viscosidad
#Campo A
#Viscosidad Hidrocarburo
if (visca > 0.04 and visca < 3):

    fpv = 10
    print("Coincidencias Hidrocarburo viscosidad Campo A, valor: ",fpv)
    coincidenciaHC = coincidenciaHC + 1
    PtHC = PtHC + fpv 

#CO2
elif (visca > 0.3 and visca < 10):

    fpvCO = 10
    print("Coincidencias CO2 viscosidad Campo A, valor: ",fpvCO)
    coincidenciaCO = coincidenciaCO + 1
    PtCO = PtCO + fpvCO

#Micelar, polímeros, ASP
elif (visca == 13 and visca < 35):

    fpvMPASP = 5
    print("Coincidencias Micelar, polímeros, ASP Campo A, valor: ", fpvMPASP)
    coincidenciaMPASP = coincidenciaMPASP + 1
    PtMPASP = PtMPASP + fpvMPASP

#Campo B
#Hidrocarburo
if (viscb > 0.04 and viscb < 3):
    fpv1 = 10
    print("Coincidencias Hidrocarburo viscosidad Campo B, valor: ",fpv1)
    coincidenciaHC1 = coincidenciaHC1 + 1
    PtHC1 = PtHC1 + fpv1 

#CO2
elif (viscb > 0.3 and viscb < 10):

    fpvCO1 = 10
    print("Coincidencias CO2 viscosidad Campo B, valor: ",fpvCO1)
    coincidenciaCO1 = coincidenciaCO1 + 1
    PtCO1 = PtCO1 + fpvCO1

#Micelar, polímeros, ASP
elif (viscb == 13 and viscb < 35):

    fpvMPASP1 = 5
    print("Coincidencias Micelar, polímeros, ASP Campo B, valor: ", fpvMPASP1)
    coincidenciaMPASP1 = coincidenciaMPASP1 + 1
    PtMPASP1 = PtMPASP1 + fpvMPASP1

#Campo C
#Hidrocarburo
if (viscc > 0.04 and viscc < 3):
    fpv2 = 10
    print("Coincidencias Hidrocarburo viscosidad Campo C, valor: ",fpv2)
    coincidenciaHC2 = coincidenciaHC2 + 1
    PtHC2 = PtHC2 + fpv2 

#CO2
elif (viscc > 0.3 and viscc < 10):

    fpvCO2 = 10
    print("Coincidencias CO2 viscosidad Campo C, valor: ",fpvCO2)
    coincidenciaCO2 = coincidenciaCO2 + 1
    PtCO2 = PtCO2 + fpvCO2

#Micelar, polímeros, ASP
elif (viscc == 13 and viscc < 35):

    fpvMPASP2 = 5
    print("Coincidencias Micelar, polímeros, ASP Campo C, valor: ", fpvMPASP2)
    coincidenciaMPASP2 = coincidenciaMPASP2 + 1
    PtMPASP2 = PtMPASP2 + fpvMPASP2

#Campo D
#Hidrocarburo
if (viscd > 0.04 and viscd < 3):
    fpv3 = 10
    print("Coincidencias Hidrocarburo viscosidad Campo D, valor: ",fpv3)
    coincidenciaHC3 = coincidenciaHC3 + 1
    PtHC3 = PtHC3 + fpv3 

#CO2
elif (viscd > 0.3 and viscd < 10):

    fpvCO3 = 10
    print("Coincidencias CO2 viscosidad Campo D, valor: ",fpvCO3)
    coincidenciaCO3 = coincidenciaCO3 + 1
    PtCO3 = PtCO3 + fpvCO3

#Micelar, polímeros, ASP
elif (viscd == 13 and viscd < 35):

    fpvMPASP3 = 5
    print("Coincidencias Micelar, polímeros, ASP viscosidad Campo D, valor: ", fpvMPASP3)
    coincidenciaMPASP3 = coincidenciaMPASP3 + 1
    PtMPASP3 = PtMPASP3 + fpvMPASP3

#Campo E
#Hidrocarburo
if (visce > 0.04 and visce < 3):
    fpv4 = 10
    print("Coincidencias Hidrocarburo viscosidad Campo E, valor: ",fpv4)
    coincidenciaHC4 = coincidenciaHC4 + 1
    PtHC4 = PtHC4 + fpv4 

#CO2
elif (visce > 0.3 and visce < 10):

    fpvCO4 = 10
    print("Coincidencias CO2 viscosidad Campo E, valor: ",fpvCO4)
    coincidenciaCO4 = coincidenciaCO4 + 1
    PtCO4 = PtCO4 + fpvCO4

#Micelar, polímeros, ASP
elif (visce == 13 and visce < 35):

    fpvMPASP4 = 5
    print("Coincidencias Micelar, polímeros, ASP viscosidad Campo E, valor: ", fpvMPASP4)
    coincidenciaMPASP4 = coincidenciaMPASP4 + 1
    PtMPASP4 = PtMPASP4 + fpvMPASP4

#Coincidencias composición
#Campo A
#Composición Hidrocarburo
if (compa == 1):
    
    com = 5
    print("Coincidencia Hidrocarburo composición Campo A, valor: ",com)
    PtHC = PtHC + com
    coincidenciaHC = coincidenciaHC + 1

#CO2
elif (compa == 2):

    com = 2.5
    print("Coincidencia CO2 composición Campo A, valor: ", com)
    PtCO = PtCO + com
    coincidenciaCO = coincidenciaCO + 1

#Micelar, polímero, ASP
elif (compa == 3):
    com = 2.5
    print("Coincidencia Micelar, polímero, ASP composición Campo A, valor: ",com)
    PtMPASP = PtMPASP + com
    coincidenciaMPASP = coincidenciaMPASP + 1

#Campo B
#Hidrocarburo
if (compb == 1):

    com1 = 5
    print("Coincidencia Hidrocarburo composición Campo B, valor: ",com1)
    PtHC1 = PtHC1 + com1
    coincidenciaHC1 = coincidenciaHC1 + 1

#CO2
elif (compb == 2):

    com1 = 2.5
    print("Coincidencia CO2 composición Campo B, valor: ", com1)
    PtCO1 = PtCO1 + com1
    coincidenciaCO1 = coincidenciaCO1 + 1

#Micelar, polímero, ASP
elif (compb == 3):

    com1 = 2.5
    print("Coincidencia Micelar, polímero, ASP composición Campo B, valor: ",com1)
    PtMPASP1 = PtMPASP1 + com1
    coincidenciaMPASP1 = coincidenciaMPASP1 + 1

#Campo C
#Hidrocarburo
if (compc == 1):

    com2 = 5
    print("Coincidencia Hidrocarburo composición Campo C, valor: ",com2)
    PtHC2 = PtHC2 + com2
    coincidenciaHC2 = coincidenciaHC2 + 1

#CO2
elif (compc == 2):

    com2 = 2.5
    print("Coincidencia CO2 composición Campo C, valor: ", com2)
    PtCO2 = PtCO2 + com2
    coincidenciaCO2 = coincidenciaCO2 + 1

#Micelar, polímero, ASP
elif (compc == 3):

    com2 = 2.5
    print("Coincidencia Micelar, polímero, ASP composición Campo C, valor: ",com2)
    PtMPASP2 = PtMPASP2 + com2
    coincidenciaMPASP2 = coincidenciaMPASP2 + 1

#Campo D
#Hidrocarburo
if (compd == 1):
    com3 = 5
    print("Coincidencia Hidrocarburo composición Campo D, valor: ",com3)
    PtHC3 = PtHC3 + com3
    coincidenciaHC3 = coincidenciaHC3 + 1

#CO2
elif (compd == 2):

    com3 = 2.5
    print("Coincidencia CO2 composición Campo D, valor: ", com3)
    PtCO3 = PtCO3 + com3
    coincidenciaCO3 = coincidenciaCO3 + 1

#Micelar, polímero, ASP
elif (compd == 3):
    com3 = 2.5
    print("Coincidencia Micelar, polímero, ASP composición Campo D, valor: ",com3)
    PtMPASP3 = PtMPASP3 + com3
    coincidenciaMPASP3 = coincidenciaMPASP3 + 1

#CO2
elif (compd == 2):

    com3 = 2.5
    print("Coincidencia CO2 composición Campo D, valor: ", com3)
    PtCO3 = PtCO3 + com3
    coincidenciaCO3 = coincidenciaCO3 + 1

#Micelar, polímero, ASP
elif (compd == 3):
    com3 = 2.5
    print("Coincidencia Micelar, polímero, ASP Campo A, valor: ",com3)
    PtMPASP3 = PtMPASP3 + com3
    coincidenciaMPASP3 = coincidenciaMPASP3 + 1

#Campo D
#Hidrocarburo
if (compe == 1):
    com4 = 5
    print("Coincidencia Hidrocarburo composición Campo E, valor: ",com4)
    PtHC4 = PtHC4 + com4
    coincidenciaHC4 = coincidenciaHC4 + 1
#CO2
elif (compe == 2):

    com4 = 2.5
    print("Coincidencia CO2 composición Campo E, valor: ", com4)
    PtCO4 = PtCO4 + com4
    coincidenciaCO4 = coincidenciaCO4 + 1

#Micelar, polímero, ASP
elif (compe == 3):

    com4 = 2.5
    print("Coincidencia Micelar, polímero, ASP composición Campo A, valor: ",com4)
    PtMPASP4 = PtMPASP4 + com4
    coincidenciaMPASP4 = coincidenciaMPASP4 + 1

#Coincidencias Saturación de aceite
#Campo A
#Saturación Hidrocarburo
if (soa > 30 and soa < 98):
    sao = 20
    print("Coincidencia Hidrocarburo saturación de aceite Campo A, valor: ",sao)
    PtHC = PtHC + sao 
    coincidenciaHC = coincidenciaHC + 1

#CO2
elif (soa > 20 and soa < 70):
    sao = 20
    print("Coincidencia CO2 saturación de aceite Campo A, valor: ",sao)
    PtCO = PtCO + sao
    coincidenciaCO = coincidenciaCO + 1

#Micelar, polímero, ASP
elif (soa > 35 and soa < 53):
    sao = 20
    print("Coincidencia Micelar, polímero, ASP saturación de aceite Campo A, valor: ",sao)
    PtMPASP = PtMPASP + sao
    coincidenciaMPASP = coincidenciaMPASP + 1

#Campo B 
#Hidrocarburo
if (sob > 30 and sob < 98):
    sao1 = 20
    print("Coincidencia Hidrocarburo saturación de aceite Campo B, valor: ",sao1)
    PtHC1 = PtHC1 + sao1 
    coincidenciaHC1 = coincidenciaHC1 + 1

#CO2
elif (sob > 20 and sob < 70):
    sao1 = 20
    print("Coincidencia CO2 saturación de aceite Campo B, valor: ",sao1)
    PtCO1 = PtCO1 + sao1
    coincidenciaCO1 = coincidenciaCO1 + 1

#Micelar, polímero, ASP
elif (sob > 35 and sob < 53):
    sao1 = 20
    print("Coincidencia Micelar, polímero, ASP saturación de aceite Campo B, valor: ",sao1)
    PtMPASP1 = PtMPASP1 + sao1
    coincidenciaMPASP1 = coincidenciaMPASP1 + 1

#Campo C
#Hidrocarburo
if (soc >30 and soc < 98):
    sao2 = 20
    print("Coincidencia Hidrocarburo saturación de aceite Campo C, valor: ",sao2)
    PtHC2 = PtHC2 + sao2 
    coincidenciaHC2 = coincidenciaHC2 + 1

#CO2
elif (soc > 20 and soc < 70):
    sao2 = 20
    print("Coincidencia CO2 saturación de aceite Campo C, valor: ",sao2)
    PtCO2 = PtCO2 + sao2
    coincidenciaCO2 = coincidenciaCO2 + 1

#Micelar, polímero, ASP
elif (soc > 35 and soc < 53):
    sao2 = 20
    print("Coincidencia Micelar, polímero, ASP saturación de aceite Campo C, valor: ",sao2)
    PtMPASP2 = PtMPASP2 + sao2
    coincidenciaMPASP2 = coincidenciaMPASP2 + 1

#Campo D
#Hidrocarburo
if (sod >30 and sod < 98):
    sao3 = 20
    print("Coincidencia Hidrocarburo saturación de aceite Campo D, valor: ",sao3)
    PtHC3 = PtHC3 + sao3 
    coincidenciaHC3 = coincidenciaHC3 + 1

#CO2
elif (sod > 20 and sod < 70):
    sao3 = 20
    print("Coincidencia CO2 saturación de aceite Campo D, valor: ",sao3)
    PtCO3 = PtCO3 + sao3
    coincidenciaCO3 = coincidenciaCO3 + 1

#Micelar, polímero, ASP
elif (sod > 35 and sod < 53):
    sao3 = 20
    print("Coincidencia Micelar, polímero, ASP saturación de aceite Campo D, valor: ",sao3)
    PtMPASP3 = PtMPASP3 + sao3
    coincidenciaMPASP3 = coincidenciaMPASP3 + 1

#Campo E
#Hidrocarburo
if (soe >30 and soe < 98):
    sao4 = 20
    print("Coincidencia Hidrocarburo saturación de aceite Campo E, valor: ",sao4)
    PtHC4 = PtHC4 + sao4 
    coincidenciaHC4 = coincidenciaHC4 + 1

#CO2
elif (soe > 20 and soe < 70):
    sao4 = 20
    print("Coincidencia CO2 saturación de aceite Campo E, valor: ",sao4)
    PtCO4 = PtCO4 + sao4
    coincidenciaCO4 = coincidenciaCO4 + 1

#Micelar, polímero, ASP
elif (soe > 35 and soe < 53):
    sao4 = 20
    print("Coincidencia Micelar, polímero, ASP saturación de aceite Campo E, valor: ",sao4)
    PtMPASP4 = PtMPASP4 + sao4
    coincidenciaMPASP4 = coincidenciaMPASP4 + 1

#Coincidencias tipo de formación
#Campo A
#Regex Hidrocarburo
if(re.search('(arenas)|(carbonatos)|(arena)|(carbonato)',tfa)):
    tfo = 5
    print("Coincidencia Hidrocarburo tipo de formación Campo A, valor: ",tfo)
    PtHC = PtHC + tfo
    coincidenciaHC = coincidenciaHC + 1

#Regex CO2
if(re.search('(arenas)|(carbonatos)|(arena)|(carbonato)',tfa)):
    tfo = 2.5
    print("Coincidencia CO2 tipo de formación Campo A, valor: ",tfo)
    PtCO = PtCO + tfo
    coincidenciaCO = coincidenciaCO + 1

#Regex Micelar, polímero, ASP
if(re.search('(arenas)|(arena)',tfa)):
    tfo = 2.5
    print("Coincidencia Micelar, polímero,ASP tipo de formación Campo A, valor: ",tfo)
    PtMPASP = PtMPASP + tfo
    coincidenciaMPASP = coincidenciaMPASP + 1

#Campo B
#Regex Hidrocarburo
if(re.search('(arenas)|(carbonatos)|(arena)|(carbonato)',tfb)):
    tfo1 = 5
    print("Coincidencia Hidrocarburo tipo de formación Campo B, valor: ",tfo1)
    PtHC1 = PtHC1 + tfo1
    coincidenciaHC1 = coincidenciaHC1 + 1

#Regex CO2
if(re.search('(arenas)|(carbonatos)|(arena)|(carbonato)',tfb)):
    tfo1 = 2.5
    print("Coincidencia Hidrocarburo tipo de formación Campo B, valor: ",tfo1)
    PtCO1 = PtCO1 + tfo1
    coincidenciaCO1 = coincidenciaCO1 + 1

#Regex Micelar, polímero, ASP
if(re.search('(arenas)|(arena)',tfb)):
    tfo1 = 2.5
    print("Coincidencia Micelar, polímero,ASP tipo de formación Campo B, valor: ",tfo1)
    PtMPASP1 = PtMPASP1 + tfo1
    coincidenciaMPASP1 = coincidenciaMPASP1 + 1

#Campo C
#Regex hidrocarburo
if(re.search('(arenas)|(carbonatos)|(arena)|(carbonato)',tfc)):
    tfo2 = 5
    print("Coincidencia Hidrocarburo tipo de formación Campo C, valor: ",tfo2)
    PtHC2 = PtHC2 + tfo2
    coincidenciaHC2 = coincidenciaHC2 + 1

#Regex CO2
if(re.search('(arenas)|(carbonatos)|(arena)|(carbonato)',tfc)):
    tfo2 = 2.5
    print("Coincidencia Hidrocarburo tipo de formación Campo C, valor: ",tfo2)
    PtCO2 = PtCO2 + tfo2
    coincidenciaCO2 = coincidenciaCO2 + 1

#Regex Micelar, polímero, ASP
if(re.search('(arenas)|(arena)',tfc)):
    tfo2 = 2.5
    print("Coincidencia Micelar, polímero,ASP tipo de formación Campo C, valor: ",tfo2)
    PtMPASP2 = PtMPASP2 + tfo2
    coincidenciaMPASP2 = coincidenciaMPASP2 + 1

#Campo D
#Regex Hidrocarburo
if(re.search('(arenas)|(carbonatos)|(arena)|(carbonato)',tfd)):
    tfo3 = 5
    print("Coincidencia Hidrocarburo tipo de formación Campo D, valor: ",tfo3)
    PtHC3 = PtHC3 + tfo3
    coincidenciaHC3 = coincidenciaHC3 + 1

#Regex CO2
if(re.search('(arenas)|(carbonatos)|(arena)|(carbonato)',tfd)):
    tfo3 = 2.5
    print("Coincidencia Hidrocarburo tipo de formación Campo D, valor: ",tfo3)
    PtCO3 = PtCO3 + tfo3
    coincidenciaCO3 = coincidenciaCO3 + 1

#Regex Micelar, polímero, ASP
if(re.search('(arenas)|(arena)',tfd)):
    tfo3 = 2.5
    print("Coincidencia Micelar, polímero,ASP tipo de formación Campo D, valor: ",tfo3)
    PtMPASP3 = PtMPASP3 + tfo3
    coincidenciaMPASP3 = coincidenciaMPASP3 + 1

#Campo E
#Regex Hidrocarburo
if(re.search('(arenas)|(carbonatos)|(arena)|(carbonato)',tfe)):
    tfo4 = 5
    print("Coincidencia Hidrocarburo tipo de formación Campo E, valor: ",tfo4)
    PtHC4 = PtHC4 + tfo4
    coincidenciaHC4 = coincidenciaHC4 + 1

#Regex CO2
if(re.search('(arenas)|(carbonatos)|(arena)|(carbonato)',tfe)):
    tfo4 = 2.5
    print("Coincidencia Hidrocarburo tipo de formación Campo E, valor: ",tfo4)
    PtCO4 = PtCO4 + tfo4
    coincidenciaCO4 = coincidenciaCO4 + 1

#Regex Micelar, polímero, ASP
if(re.search('(arenas)|(arena)',tfe)):
    tfo4 = 2.5
    print("Coincidencia Micelar, polímero,ASP tipo de formación Campo E, valor: ",tfo4)
    PtMPASP4 = PtMPASP4 + tfo4
    coincidenciaMPASP4 = coincidenciaMPASP4 + 1

#Coincidencias espesor
#Se concideró el espesor delgado hasta 300 m
#Campo A
#Hidrocarburo
if (espa < 300):
    espva = 5
    print("Coincidencia Hidrocarburo espesor Campo A, valor: ",espva)
    PtHC = PtHC + espva
    coincidenciaHC = coincidenciaHC + 1

#CO2
elif (espa > 0):
    espva = 2.5
    print("Coincidencia CO2 espesor Campo A, valor: ", espva)
    PtCO = PtCO + espva
    coincidenciaCO = coincidenciaCO + 1

#Micelar, polímero,ASP
elif (espa > 0):
    espva = 2.5
    print("Coincidencia Micelar, polímero, ASP Campo A, valor: ",espva)
    PtMPASP = PtMPASP + espva
    coincidenciaMPASP = coincidenciaMPASP + 1  

#Campo B
#Hidrocarburo
if (espb < 300):
    espvb = 5
    print("Coincidencia Hidrocarburo espesor Campo B, valor: ",espvb)
    PtHC1 = PtHC1 + espvb
    coincidenciaHC1 = coincidenciaHC1 + 1 
#CO2
elif (espb > 0):
    espvb = 2.5
    print("Coincidencia CO2 espesor Campo B, valor: ", espvb)
    PtCO1 = PtCO1 + espvb
    coincidenciaCO1 = coincidenciaCO1 + 1

#Micelar, polímero,ASP
elif (espb > 0):
    espvb = 2.5
    print("Coincidencia Micelar, polímero, ASP Campo B, valor: ",espvb)
    PtMPASP1 = PtMPASP1 + espvb
    coincidenciaMPASP1 = coincidenciaMPASP1 + 1  


#Campo C
#Hidrocarburo
if (espc < 300):
    espvc = 5
    print("Coincidencia Hidrocarburo espesor Campo C, valor: ",espvc)
    PtHC2 = PtHC2 + espvc
    coincidenciaHC2 = coincidenciaHC2 + 1 

#CO2
elif (espc > 0):
    espvc = 2.5
    print("Coincidencia CO2 espesor Campo C, valor: ", espvc)
    PtCO2 = PtCO2 + espvc
    coincidenciaCO2 = coincidenciaCO2 + 1

#Micelar, polímero,ASP
elif (espc > 0):
    espvc = 2.5
    print("Coincidencia Micelar, polímero, ASP Campo C, valor: ",espvc)
    PtMPASP2 = PtMPASP2 + espvc
    coincidenciaMPASP2 = coincidenciaMPASP2 + 1  


#Campo D
#Hidrocarburo
if (espd < 300):
    espvd = 5
    print("Coincidencia Hidrocarburo espesor Campo D, valor: ",espvd)
    PtHC3 = PtHC3 + espvd
    coincidenciaHC3 = coincidenciaHC3 + 1 

#CO2
elif (espd > 0):
    espvd = 2.5
    print("Coincidencia CO2 espesor Campo D, valor: ", espvd)
    PtCO3 = PtCO3 + espvd
    coincidenciaCO3 = coincidenciaCO3 + 1

#Micelar, polímero,ASP
elif (espd > 0):
    espvd = 2.5
    print("Coincidencia Micelar, polímero, ASP Campo D, valor: ",espvd)
    PtMPASP3 = PtMPASP3 + espvd
    coincidenciaMPASP3 = coincidenciaMPASP3 + 1  


#Campo E
#Hidrocarburo
if (espe < 300):
    espve = 5
    print("Coincidencia Hidrocarburo espesor Campo E, valor: ",espve)
    PtHC4 = PtHC4 + espve
    coincidenciaHC4 = coincidenciaHC4 + 1 

#CO2
elif (espe > 0):
    espve = 2.5
    print("Coincidencia CO2 espesor Campo E, valor: ", espve)
    PtCO4 = PtCO4 + espve
    coincidenciaCO4 = coincidenciaCO4 + 1

#Micelar, polímero,ASP
elif (espe > 0):
    espve = 2.5
    print("Coincidencia Micelar, polímero, ASP Campo E, valor: ",espve)
    PtMPASP4 = PtMPASP4 + espve
    coincidenciaMPASP4 = coincidenciaMPASP4 + 1  

#Coincidencias permeabilidad promedio
#Hidrocarburo
#Como no es crítica para la inyección de Hidrocarburo se suman los valores de ponderación
#Campo A
if (ka > 0):

    kpva = 5
    print("Coincidencia Hidrocarburo permeabilidad promedio Campo A, valor: ", kpva)
    PtHC = PtHC + kpva
    coincidenciaHC = coincidenciaHC + 1 

#CO2
elif (ka > 0):
    kpva = 10
    print("Coincidencia CO2 permeabilidad promedio Campo A, valor: ", kpva)
    PtCO = PtCO + kpva
    coincidenciaCO = coincidenciaCO + 1 

#Micelar
elif (ka > 10 and ka < 500):
    kpva = 2.5
    print("Coincidencia Micelar, polímero, ASP, permeabilidad promedio Campo A, valor: ", kpva)
    PtMPASP = PtMPASP + kpva
    coincidenciaMPASP = coincidenciaMPASP + 1 

#Campo B
#Hidrocarburo
if (kb > 0):
    kpvb = 5
    print("Coincidencia Hidrocarburo permeabilidad promedio Campo B, valor: ", kpvb)
    PtHC1 = PtHC1 + kpvb
    coincidenciaHC1 = coincidenciaHC1 + 1 

#CO2
elif (kb > 0):
    kpvb = 10
    print("Coincidencia CO2 permeabilidad promedio Campo B, valor: ", kpvb)
    PtCO1 = PtCO1 + kpvb
    coincidenciaCO1 = coincidenciaCO1 + 1 

#Micelar
elif (kb > 10 and kb < 500):
    kpvb = 2.5
    print("Coincidencia Micelar, polímero, ASP, permeabilidad promedio Campo B, valor: ", kpvb)
    PtMPASP1 = PtMPASP1 + kpvb
    coincidenciaMPASP1 = coincidenciaMPASP1 + 1 

#Campo C
#Hidrocarburo
if (kc > 0):
    kpvc = 5
    print("Coincidencia Hidrocarburo permeabilidad promedio Campo C, valor: ", kpvc)
    PtHC2 = PtHC2 + kpvc
    coincidenciaHC2 = coincidenciaHC2 + 1 

#CO2
elif (kc > 0):
    kpvc = 10
    print("Coincidencia CO2 permeabilidad promedio Campo C, valor: ", kpvc)
    PtCO2 = PtCO2 + kpvc
    coincidenciaCO2 = coincidenciaCO2 + 1 

#Micelar
elif (kc > 10 and kc < 500):
    kpvc = 2.5
    print("Coincidencia Micelar, polímero, ASP, permeabilidad promedio Campo C, valor: ", kpvc)
    PtMPASP2 = PtMPASP2 + kpvc
    coincidenciaMPASP2 = coincidenciaMPASP2 + 1 

#Campo D
#Hidrocarburo
if (kd > 0):
    kpvd = 5
    print("Coincidencia Hidrocarburo permeabilidad promedio Campo D, valor: ", kpvd)
    PtHC3 = PtHC3 + kpvd
    coincidenciaHC3 = coincidenciaHC3 + 1

#CO2
elif (kd > 0):
    kpvd = 10
    print("Coincidencia CO2 permeabilidad promedio Campo D, valor: ", kpvd)
    PtCO3 = PtCO3 + kpvd
    coincidenciaCO3 = coincidenciaCO3 + 1 

#Micelar
elif (kd > 10 and kd < 500):
    kpvd = 2.5
    print("Coincidencia Micelar, polímero, ASP, permeabilidad promedio Campo D, valor: ", kpvd)
    PtMPASP3 = PtMPASP3 + kpvd
    coincidenciaMPASP3 = coincidenciaMPASP3 + 1 

#Campo E
#Hidrocarburo 
if (ke > 0):
    kpve = 5
    print("Coincidencia Hidrocarburo permeabilidad promedio Campo E, valor: ", kpve)
    PtHC4 = PtHC4 + kpve
    coincidenciaHC4 = coincidenciaHC4 + 1 

#CO2
elif (ke > 0):
    kpve = 10
    print("Coincidencia CO2 permeabilidad promedio Campo E, valor: ", kpve)
    PtCO4 = PtCO4 + kpve
    coincidenciaCO4 = coincidenciaCO4 + 1 

#Micelar
elif (ke > 10 and ke < 500):
    kpve = 2.5
    print("Coincidencia Micelar, polímero, ASP, permeabilidad promedio Campo E, valor: ", kpve)
    PtMPASP4 = PtMPASP4 + kpve
    coincidenciaMPASP4 = coincidenciaMPASP4 + 1 

#Coincidencias profundidad
#Campo A
#Hidrocarburo
if (profa > 1219 and profa < 4847):
    profav = 15
    print("Coincidencia Hidrocarburo profundidad Campo A, valor: ", profav)
    PtHC = PtHC + profav
    coincidenciaHC = coincidenciaHC + 1 

#CO2
if (profa > 762):
    profav = 30
    print("Coincidencia CO2 profundidad Campo A, valor: ", profav)
    PtCO = PtCO + profav
    coincidenciaCO = coincidenciaCO + 1

#Micelar
if (profa > 10 and profa < 500):
    profav = 5
    print("Coincidencia Micelar, polímero, ASP, Campo A, valor: ", profav)
    PtMPASP = PtMPASP + profav
    coincidenciaMPASP = coincidenciaMPASP + 1

#Campo B
#Hidrocarburo
if (profb > 1219 and profb < 4847):
    profav1 = 15
    print("Coincidencia Hidrocarburo profundidad Campo B, valor: ", profav1)
    PtHC1 = PtHC1 + profav1
    coincidenciaHC1 = coincidenciaHC1 + 1 

#CO2
if (profb > 762):
    profav1 = 30
    print("Coincidencia CO2 profundidad Campo B, valor: ", profav1)
    PtCO1 = PtCO1 + profav1
    coincidenciaCO1 = coincidenciaCO1 + 1

#Micelar
if (profb > 10 and profb < 500):
    profav1 = 5
    print("Coincidencia Micelar, polímero, ASP, Campo B, valor: ", profav1)
    PtMPASP1 = PtMPASP1 + profav1
    coincidenciaMPASP1 = coincidenciaMPASP1 + 1

#Campo C
#Hidrocarburo
if (profc > 1219 and profc < 4847):
    profav2 = 15
    print("Coincidencia Hidrocarburo profundidad Campo C, valor: ", profav2)
    PtHC2 = PtHC2 + profav2
    coincidenciaHC2 = coincidenciaHC2 + 1 

#CO2
if (profc > 762):
    profav2 = 30
    print("Coincidencia CO2 profundidad Campo C, valor: ", profav2)
    PtCO2 = PtCO2 + profav2
    coincidenciaCO2 = coincidenciaCO2 + 1

#Micelar
if (profc > 10 and profc < 500):
    profav2 = 5
    print("Coincidencia Micelar, polímero, ASP, Campo C, valor: ", profav2)
    PtMPASP2 = PtMPASP2 + profav2
    coincidenciaMPASP2 = coincidenciaMPASP2 + 1


#Campo D
#Hidrocarburo
if (profd > 1219 and profd < 4847):
    profav3 = 15
    print("Coincidencia Hidrocarburo profundidad Campo D, valor: ", profav3)
    PtHC3 = PtHC3 + profav3
    coincidenciaHC3 = coincidenciaHC3 + 1 

#CO2
if (profd > 762):
    profav3 = 30
    print("Coincidencia CO2 profundidad Campo D, valor: ", profav3)
    PtCO3 = PtCO3 + profav3
    coincidenciaCO3 = coincidenciaCO3 + 1

#Micelar
if (profd > 10 and profd < 500):
    profav3 = 5
    print("Coincidencia Micelar, polímero, ASP, Campo D, valor: ", profav3)
    PtMPASP3 = PtMPASP3 + profav3
    coincidenciaMPASP3 = coincidenciaMPASP3 + 1


#Campo E
#Hidrocarburo
if (profe > 1219 and profe < 4847):
    profav4 = 15
    print("Coincidencia Hidrocarburo profundidad Campo E, valor: ", profav4)
    PtHC4 = PtHC4 + profav4
    coincidenciaHC4 = coincidenciaHC4 + 1 

#CO2
if (profe > 762):
    profav4 = 30
    print("Coincidencia CO2 profundidad Campo E, valor: ", profav4)
    PtCO4 = PtCO4 + profav4
    coincidenciaCO4 = coincidenciaCO4 + 1

#Micelar
if (profe > 10 and profe < 500):
    profav4 = 5
    print("Coincidencia Micelar, polímero, ASP, Campo A, valor: ", profav4)
    PtMPASP4 = PtMPASP4 + profav4
    coincidenciaMPASP4 = coincidenciaMPASP4 + 1

#Coincidencias temperatura
#Hidrocarburo
#Como no es crítica solo se suma la ponderación
#Campo A
#Hidrocarburo
if (tempa > 0):

    tav = 5
    print("Coincidencia Hidrocarburo temperatura Campo A, valor: ", tav)
    PtHC = PtHC + tav
    coincidenciaHC = coincidenciaHC + 1 

#CO2
if (tempa > 0):
    tav = 5
    print("Coincidencia CO2 temperatura Campo A, valor: ", tav)
    PtCO = PtCO + tav
    coincidenciaCO = coincidenciaCO + 1

#Micelar
if (tempa == 26 and tempa < 121):
    tav = 30
    print("Coincidencia Micelar, polímero, ASP Campo A temperatura, valor: ", tav)
    PtMPASP = PtMPASP + tav
    coincidenciaMPASP = coincidenciaMPASP + 1

#Campo B
#Hidrocarburo
if (tempb > 0):

    tbv = 5
    print("Coincidencia Hidrocarburo temperatura Campo B, valor: ", tbv)
    PtHC1 = PtHC1 + tbv
    coincidenciaHC1 = coincidenciaHC1 + 1 

#CO2
if (tempb > 0):
    tbv = 5
    print("Coincidencia CO2 temperatura Campo B, valor: ", tbv)
    PtCO1 = PtCO1 + tbv
    coincidenciaCO1 = coincidenciaCO1 + 1

#Micelar
if (tempb == 26 and tempb < 121):
    tbv = 30
    print("Coincidencia Micelar, polímero, ASP Campo B temperatura, valor: ", tbv)
    PtMPASP1 = PtMPASP1 + tbv
    coincidenciaMPASP1 = coincidenciaMPASP1 + 1

#Campo C
#Hidrocarburo
if(tempc > 0):
    tcv = 5
    print("Coincidencia Hidrocarburo temperatura Campo C, valor: ", tcv)
    PtHC2 = PtHC2 + tcv
    coincidenciaHC2 = coincidenciaHC2 + 1 

#CO2
if (tempc > 0):
    tcv = 5
    print("Coincidencia CO2 temperatura Campo C, valor: ", tcv)
    PtCO2 = PtCO2 + tcv
    coincidenciaCO2 = coincidenciaCO2 + 1

#Micelar
if (tempc == 26 and tempc < 121):
    tcv = 30
    print("Coincidencia Micelar, polímero, ASP Campo C temperatura, valor: ", tcv)
    PtMPASP2 = PtMPASP2 + tcv
    coincidenciaMPASP2 = coincidenciaMPASP2 + 1

#Campo D
#Hidrocarburo
if(tempd > 0):
    tdv = 5
    print("Coincidencia Hidrocarburo temperatura Campo D, valor: ", tdv)
    PtHC3 = PtHC3 + tdv
    coincidenciaHC3 = coincidenciaHC3 + 1

#CO2
if (tempd > 0):
    tdv = 5
    print("Coincidencia CO2 temperatura Campo D, valor: ", tdv)
    PtCO3 = PtCO3 + tdv
    coincidenciaCO3 = coincidenciaCO3 + 1

#Micelar
if (tempd == 26 and tempd < 121):
    tdv = 30
    print("Coincidencia Micelar, polímero, ASP Campo D temperatura, valor: ", tdv)
    PtMPASP3 = PtMPASP3 + tdv
    coincidenciaMPASP3 = coincidenciaMPASP3 + 1 

#Campo E
#Hidrocarburo
if(tempe > 0):
    tev = 5
    print("Coincidencia Hidrocarburo temperatura Campo E, valor: ", tev)
    PtHC4 = PtHC4 + tev
    coincidenciaHC4 = coincidenciaHC4 + 1 

#CO2
if (tempe > 0):
    tev = 5
    print("Coincidencia CO2 temperatura Campo E, valor: ", tev)
    PtCO4 = PtCO4 + tev
    coincidenciaCO4 = coincidenciaCO4 + 1

#Micelar
if (tempe == 26 and tempe < 121):
    tev = 30
    print("Coincidencia Micelar, polímero, ASP Campo E temperatura, valor: ", tev)
    PtMPASP4 = PtMPASP4 + tev
    coincidenciaMPASP4 = coincidenciaMPASP4 + 1


#Valores finales Hidocarburo
print("Ponderación final Hidrocarburo Campo A: ", PtHC)
print("Numero de coincidencias para Hidrocarburo Campo A: ", coincidenciaHC)

print("Ponderación final Hidrocarburo Campo B: ", PtHC1)
print("Numero de coincidencias para Hidrocarburo Campo B: ", coincidenciaHC1)
 
print("Ponderación final Hidrocarburo Campo C: ", PtHC2)
print("Numero de coincidencias para Hidrocarburo Campo C: ", coincidenciaHC2)

print("Ponderación final Hidrocarburo Campo D: ", PtHC3)
print("Numero de coincidencias para Hidrocarburo Campo D: ", coincidenciaHC3)

print("Ponderación final Hidrocarburo Campo E: ", PtHC4)
print("Numero de coincidencias para Hidrocarburo Campo E: ", coincidenciaHC4)

#Valores finales CO2
print("Ponderación final CO2 Campo A: ", PtCO)
print("Numero de coincidencias para CO2 Campo A: ", coincidenciaCO)

print("Ponderación final CO2 Campo B: ", PtCO1)
print("Numero de coincidencias para CO2 Campo B: ", coincidenciaCO1)
 
print("Ponderación final CO2 Campo C: ", PtCO2)
print("Numero de coincidencias para CO2 Campo C: ", coincidenciaCO2)

print("Ponderación final CO2 Campo D: ", PtCO3)
print("Numero de coincidencias para CO2 Campo D: ", coincidenciaCO3)

print("Ponderación final CO2 Campo E: ", PtCO4)
print("Numero de coincidencias para CO2 Campo E: ", coincidenciaCO4)

#Valores finales Micelar, polímero, ASP
print("Ponderación final Micelar, polímero, ASP Campo A: ", PtMPASP)
print("Numero de coincidencias para Micelar, polímero, ASP Campo A: ", coincidenciaMPASP)

print("Ponderación final Micelar, polímero, ASP Campo B: ", PtMPASP1)
print("Numero de coincidencias para Micelar, polímero, ASP Campo B: ", coincidenciaMPASP1)
 
print("Ponderación final Micelar, polímero, ASP Campo C: ", PtMPASP2)
print("Numero de coincidencias para Micelar, polímero, ASP Campo C: ", coincidenciaMPASP2)

print("Ponderación final Micelar, polímero, ASP Campo D: ", PtMPASP3)
print("Numero de coincidencias para Micelar, polímero, ASP Campo D: ", coincidenciaMPASP3)

print("Ponderación final Micelar, polímero, ASP Campo E: ", PtMPASP4)
print("Numero de coincidencias para Micelar, polímero, ASP Campo E: ", coincidenciaMPASP4)

xa = ["Inyección de CO2" , "Inyección de gas hidrocarburo" , "Inyección de Micelar, polímeros, ASP"]
ya = [PtCO, PtHC, PtMPASP]

xb = ["Inyección de CO2" , "Inyección de gas hidrocarburo" , "Inyección de Micelar, polímeros, ASP"]
yb = [PtCO1, PtHC1, PtMPASP1]

xc = ["Inyección de CO2" , "Inyección de gas hidrocarburo" , "Inyección de Micelar, polímeros, ASP"]
yc = [PtCO2, PtHC2, PtMPASP2]

xd = ["Inyección de CO2" , "Inyección de gas hidrocarburo" , "Inyección de Micelar, polímeros, ASP"]
yd = [PtCO3, PtHC3, PtMPASP3]

xe = ["Inyección de CO2" , "Inyección de gas hidrocarburo" , "Inyección de Micelar, polímeros, ASP"]
ye = [PtCO4, PtHC4, PtMPASP4]





fig  = plt.figure()
ax = plt.axes()
ax.bar(xa[0], ya[0], color = 'g')
ax.bar(xa[1], ya[1], color = 'r')
ax.bar(xa[2], ya[2], color = 'b')
ax.set_title('Campo A')

fig1 = plt.figure()
ax1 = plt.axes()
ax1.bar(xb[0], yb[0], color = 'c')
ax1.bar(xb[1], yb[1], color = 'm')
ax1.bar(xb[2], yb[2], color = 'k')
ax1.set_title('Campo B')

fig2 = plt.figure()
ax2 = plt.axes()
ax2.bar(xc[0], yc[0], color = 'm')
ax2.bar(xc[1], yc[1], color = 'y')
ax2.bar(xc[2], yc[2], color = 'k')
ax2.set_title('Campo C')

fig3 = plt.figure()
ax3 = plt.axes()
ax3.bar(xd[0], yd[0], color = 'c')
ax3.bar(xd[1], yd[1], color = 'm')
ax3.bar(xd[2], yd[2], color = 'k')
ax3.set_title('Campo D')

fig4 = plt.figure()
ax4 = plt.axes()
ax4.bar(xe[0], ye[0], color = 'y')
ax4.bar(xe[1], ye[1], color = 'k')
ax4.bar(xe[2], ye[2], color = 'g')
ax4.set_title('Campo E')



plt.show()


