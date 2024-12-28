import math

#1 Faça um Programa que mostre a mensagem "Alo mundo" na tela.
def helloWorld():
    print("Hello World")

helloWorld()

#2 Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].
def onInputNumber():
    print("Put your number here:")
    number = input()
    print('Your favorite number is ' + number)

onInputNumber()

#3 Faça um Programa que peça dois números e imprima a soma.

def onPlusTwoNumbers():
    number1 = input("Put your first number:")
    number2 = input("Put your second number:")
    result = int(number1) + int(number2)
    print(number1+ ' + '+number2+' = ',result) 

onPlusTwoNumbers()

#4 Faça um Programa que peça as 4 notas bimestrais e mostre a média.
def onAverageToFourGrades():
    print('Offer the 4 bimonthly notes:')
    note1 = input("Note #1:")
    note2 = input("Note #2:")
    note3 = input("Note #3:")
    note4 = input("Note #4:")
    result = int(note1)+int(note2)+int(note3)+int(note4)
    print("The sum is: ",result)

onAverageToFourGrades()

#5 Faça um Programa que converta metros para centímetros.
def onConvertMeterToCentimerter():
    meterValue = input('Input value in meter: ')
    centimeterValue = int(meterValue)*100
    print(meterValue+' m in centimerters is ',centimeterValue)


onConvertMeterToCentimerter()


#6 Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
def calculateAreaOfACircle():
    radius = input('Put the radius of a circle here: ')
    pi = math.pi
    area = pow(int(radius),2)*pi
    print("The area of a circle is: ", area)

calculateAreaOfACircle()

#7 Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
def onCalculateAreaToSquare():
    print("This program calculate the area of a square")
    side = input("Offer the side of the square: ")
    area = pow(int(side),2)
    print("The area of the square is ",area)
    print("Twice the area of the square is ",(area*2))

onCalculateAreaToSquare()


#8 Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
def calculateSalayByHour():
    workedHours = input("how many hours did you work this month? ")
    valueByHour = input("How much do you earn per hour? ")
    monthlySalary = int(workedHours)*int(valueByHour)
    print("Your salary is: ",monthlySalary)

calculateSalayByHour()


#9 Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
#C = 5 * ((F-32) / 9).

def convertFahrenheitToCelsius():
    fahrenheit = input("Put temperature in fahrenheit: ")
    celsius = 5* ((int(fahrenheit)-32)/9)
    print ("The temperature in celsius is: ", celsius)

convertFahrenheitToCelsius()

#10 Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
def convertCelsiusToFahrenheit():
    celsius = input("Put temperature in celsius: ")
    fahrenheit = (int(celsius)/5)*9 +32
    print ("The temperature in fahrenheit is: ", fahrenheit)

convertCelsiusToFahrenheit()


#11 Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#o produto do dobro do primeiro com metade do segundo .
#a soma do triplo do primeiro com o terceiro.
#o terceiro elevado ao cubo.

def calculateValues():
    integer1 = input("Put a fisrt int number: ")
    integer2 = input("Put a second int number: ")
    real1 = input("Put a first real number: ")
    result1 = (2*int(integer1))*(int(integer2)/2)
    result2 = (3*int(integer1))+float(real1)
    result3 = pow(float(real1),3)
    print("(2*int(integer1))*(int(integer2)/2) = ", result1)
    print("(3*int(integer1))+float(real1) = ", result2)
    print("pow(float(real1),3)",result3)

calculateValues()


#12 Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58
def calculateIdealWeighForMan():
    height = input("Put your height: ")
    idealWeight = (72.7*float(height)) - 58
    print("Your ideal weight is : ", idealWeight)

calculateIdealWeighForMan()


#13 Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#Para homens: (72.7*h) - 58
#Para mulheres: (62.1*h) - 44.7

def calculateIdealWeighForWoman():
    height = input("Put your height: ")
    idealWeight = (61.1*float(height)) - 44.7
    print("Your ideal weight is : ", idealWeight)

def calculateIdealWeigh():
    option = input("Put\n[1] for man\n[2] for woman:\n")    
    if (int(option) == 1):
        idealWeight = calculateIdealWeighForMan() 
    else :
        idealWeight = calculateIdealWeighForWoman()

calculateIdealWeigh()



#João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. 
#Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo
# excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. 
#Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. 
#Imprima os dados do programa com as mensagens adequadas.
def calculateFineAndExcessToWork():
    idealWeight = 50
    weightFish = input("Fish's weight: ")
    if (int(weightFish) > 50):
        excess = int(weightFish) - 50
    else : 
        excess = 0
    fine = 4*excess
    print("Excess: (weight): ",excess)
    print("Fine: R$: ",fine)

calculateFineAndExcessToWork()
   

#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
#Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 
#8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
#salário bruto.
#quanto pagou ao INSS.
#quanto pagou ao sindicato.
#o salário líquido.
#calcule os descontos e o salário líquido, conforme a tabela abaixo:
#+ Salário Bruto : R$
#- IR (11%) : R$
#- INSS (8%) : R$
#- Sindicato ( 5%) : R$
#= Salário Liquido : R$
#Obs.: Salário Bruto - Descontos = Salário Líquido.

def calculateRealSalayByHour():
    workedHours = input("how many hours did you work this month? ")
    valueByHour = input("How much do you earn per hour? ")
    monthlySalary = int(workedHours)*int(valueByHour)
    ir = (11/100) * monthlySalary
    inss = (8/100) * monthlySalary
    union = (5/100) * monthlySalary
    realMonthlySalary = monthlySalary - ir - inss - union
    print("Your Salary is: ",monthlySalary)
    print("Your IR is: ",ir)
    print("Your INSS is: ",inss)
    print("Your Union is: ",union)
    print("Your Real Salary is: ",realMonthlySalary)

calculateRealSalayByHour()



