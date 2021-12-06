f=open('c:/Users/User/Desktop/input.txt', 'r')
elevi=list(f)
print(f'Nr  Numele  Prenumele  Nota1  Nota2  Nota3')
b=open('c:/Users/User/Desktop/rezerva.txt', 'w')
c=open('c:/Users/User/Desktop/output.txt', 'w')
media=0
for i in elevi:
    elev=i.split()
    print(f'{elev[0]}  {elev[1]}  {elev[2]}  {elev[3]}  {elev[4]}  {elev[5]}')
    b.write(f'{elev[0]}\t{elev[1]}\t{elev[2]}\t{elev[3]}\t{elev[4]}\t{elev[5]}\n')
    media=(float(elev[3])+float(elev[4])+float(elev[5]))/3
    c.write(f'{elev[0]}\t{elev[1]}\t{elev[2]}\t{media}\n')
c.close()
with open('c:/Users/User/Desktop/output.txt', 'r') as c:
    elevi2=list(c)
print(f'Nr\tNumele\t\tPrenumele\tMedia')
for i in elevi2:
    elev=i.split()
    print(f'{elev[0]}\t{elev[1]}\t{elev[2]}\t{elev[3]}')
b.close()
f.close()