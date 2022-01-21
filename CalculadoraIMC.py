Altura = float(input("Insira sua altura em cm:"))
Peso = float(input("Insira seu peso em kg:"))

IMC = Peso / Altura**2

print(f"Seu IMC é {IMC:.2f}")

if IMC <= 18.4:
 print('Está abaixo do peso, BORA ENGORDAR PORRA')
elif IMC <= 24.9:
 print('Está no seu peso normal, MANTÉM CARALHO')
elif IMC <= 29.9:
 print('TA UM POUCO GORDO EM FILHO DA PUTA')
elif IMC <= 34.9:
 print('TA PORRA É UM ELEFANTE')
elif IMC <= 39.9:
 print('COMEÇA A FAZER DIETA E ACADEMIA GORDO SAFADO')
elif IMC >= 40.0:
 print('FAZ UMA BARIATRICA') 
