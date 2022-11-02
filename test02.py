from datetime import date
p1=['iaurt', date(2022,11,2), date(2022,11,9), 26]
p2=['smantana', date(2022,11,1), date(2022,11,7), 32]
p3=['salam', date(2022,9,17), date(2022,10,11), 105]
paine=['paine', date(2022,11,2), date(2022,11,3), 8]
inghetata=['inghetata', date(2022,7,13), date(2022,12,23), 17]
ciocolata=['ciocolata', date(2022,6,18), date(2023,4,10), 41]
hrisca=['hrisca', date(2021,3,11), date(2022,7,11), 33]
azi=date(2022,11,2)
def termenval(t): 
    return (t[2]-t[1])
print("Termenul de valabilitate este ", termenval(iaurt).days, "zile")
print("Termenul de valabilitate este ", termenval(smantana).days, "zile")
print("Termenul de valabilitate este ", termenval(salam).days, "zile")
print("Termenul de valabilitate este ", termenval(paine).days, "zile")
print("Termenul de valabilitate este ", termenval(inghetata).days, "zile")
print("Termenul de valabilitate este ", termenval(ciocolata).days, "zile")
print("Termenul de valabilitate este ", termenval(hrisca).days, "zile")

pex=[]
cper=[]
an=[]
luna=[]
dper=[]
if azi>iaurt[2]:
    pex.append(iaurt[0])
if azi>smantana[2]:
    pex.append(smantana[0])
if azi>salam[2]:
    pex.append(salam[0])
if azi>paine[2]:
    pex.append(paine[0])
if azi>ciocolata[2]:
    pex.append(ciocolata[0])
if azi>hrisca[2]:
    pex.append(hrisca[0])
print("Lisa prodselor expiate:",pex,"cu pretul 0 lei")

if (iaurt[2]-azi)<(0,25*termenval(iaurt).days):
    cper.append(iaurt[0])
if (smantana[2]-azi)<(0,25*termenval(smantana).days):
    cper.append(smantana[0])
if (salam[2]-azi)<(0,25*termenval(salam).days):
    cper.append(salam[0])
if (paine[2]-azi)<(0,25*termenval(orez).days):
    cper.append(orez[0])
if (salam[2]-azi)<(0,5*termenval(salam).days):
    dper.append(salam[0])
if (iaurt[2]-azi)<(0,25*termenval(iaurt).days):
    cper.append(iaurt[0])
if (orez[2]-azi)<(0,25*termenval(orez).days):
    cper.append(orez[0])
print('cu 50%=',cper)

