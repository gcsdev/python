import math
import re

#1 Faça um Programa que peça dois números e imprima o maior deles.

def findLargestNumber(number1, number2):
    if (number1 > number2): 
        print("More number is: ",number1)
    else:
        print("More number is: ",number2)

def mainFindLargestNumber():
    number1 = int(input("Put number 1: "))
    number2 = int(input("Put number 2: "))
    findLargestNumber(number1, number2)

#mainFindLargestNumber()

#2 Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
def isPositiveNumber():
    number1 = int(input("Put your number: "))
    if (number1>0):
        print("number > 0")
    else:
        print("number < 0")

#isPositiveNumber()

#3 Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

def isMalePerson():
    letter = input("Press:\n[F]:Feminino\n[M]:Masculino\n--->")
    if(letter == "F"):
        print("F - Feminino")
    else:
        if(letter == "M"):
            print("M - Masculino")
        else:
            print("Sexo Inválido")


#isMalePerson()

#4 Faça um Programa que verifique se uma letra digitada é vogal ou consoante.            
def isVowelsLetter():
    vowels = ["a","A","e","E","i","I","o","O","u","U"]
    letter = input("Put some letter: ")
    if letter in vowels:
        print("This letter is vowel")
    else:
        print("This letter is consonant")

#isVowelsLetter()

#5 Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
#A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
#A mensagem "Reprovado", se a média for menor do que sete;
#A mensagem "Aprovado com Distinção", se a média for igual a dez.
        
def checkStatusFromAverageGrade():
    grade1 = float(input("Put your first grade: "))
    grade2 = float(input("Put your second grade: "))
    average = (grade1+grade2)/2
    if (average >= 7):
        if (average == 10):
            print("Aprovado com Distinção")
        else:
            print("Aprovado")    
    else:
        print("Reprovado")

#checkStatusFromAverageGrade()

#6 Faça um Programa que leia três números e mostre o maior deles.
def findLargestNumber():
    number1 = int(input("Put your first number: "))
    number2 = int(input("Put your second number: "))
    number3 = int(input("Put your third number: "))
    numbers = [number1,number2,number3]
    numbers.sort()
    print("Your largest number is: ", numbers[2])

#findLargestNumber()

#7 Faça um Programa que leia três números e mostre o maior e o menor deles.
def findLargestAndSmallestNumber():
    number1 = int(input("Put your first number: "))
    number2 = int(input("Put your second number: "))
    number3 = int(input("Put your third number: "))
    numbers = [number1,number2,number3]
    numbers.sort()
    print("Your largest number is: ", numbers[2])
    print("Your smallest number is: ", numbers[0])

#findLargestAndSmallestNumber()

#8 Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.
def findCheapestproduct():
    value1 = float(input("Put your first product's value - (R$): "))
    value2 = float(input("Put your second product's value - (R$): "))
    value3 = float(input("Put your third product's value - (R$): "))
    if ((value1 < value2) and (value1 < value3)):
       print("You must purchase the first product")
    elif ((value2 < value1) and (value2 < value3)):
        print("You must purchase the second product")
    else :
        print("You must purchase the third product")

#findCheapestproduct()

#9 Faça um Programa que leia três números e mostre-os em ordem decrescente.
def onSortThreeNumbers():
    number1 = int(input("Put your first number: "))
    number2 = int(input("Put your second number: "))
    number3 = int(input("Put your third number: "))
    numbers = [number1,number2,number3]
    numbers.sort()
    numbersSort = str(numbers[0])+str(numbers[1])+str(numbers[2])
    print(numbersSort)

#onSortThreeNumbers()

#10 Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. 
#Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
def setGreetings():
    letter = input("Press:\n[M]-matutino\n[V]-Vespertino\n[N]-Noturno\n:->")
    if (letter == "M"):
        print("M-matutino")
    elif (letter == "V"):
        print("V-Vespertino")
    else: 
        print("N-Noturno")

#setGreetings()

#11 As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
#Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
#salários até R$ 280,00 (incluindo) : aumento de 20%
#salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
#salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
#salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
#o salário antes do reajuste;
#o percentual de aumento aplicado;
#o valor do aumento;
#o novo salário, após o aumento.

def onSalaryAdjustment():
    salary = float(input("Put your salary: "))
    increase = 0
    if (salary < 280):
        increasePercent = 20/100
    elif (salary < 700):
        increasePercent = 15/100
    elif (salary < 1500):
        increasePercent = 10/100
    else:
        increasePercent = 5/100
    increasevalue = salary*increasePercent
    salaryFinal = salary+increasevalue
    print("Salary: ",salary)
    print("Increase (%): ",increasePercent)
    print("Increase (R$): ",increasevalue)
    print("Final Salary (R$): ",salaryFinal)

#onSalaryAdjustment()

#12 Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo)
#e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita).
#O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
#Desconto do IR:
#Salário Bruto até 900 (inclusive) - isento
#Salário Bruto até 1500 (inclusive) - desconto de 5%
#Salário Bruto até 2500 (inclusive) - desconto de 10%
#Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220
def calculateRealSalayByHour():
    workedHours = input("how many hours did you work this month? ")
    valueByHour = input("How much do you earn per hour? ")
    monthlySalary = float(workedHours)*float(valueByHour)
    if (monthlySalary <= 900):
        irPercent = 0
    elif (monthlySalary <= 1500):
        irPercent = 5
    elif (monthlySalary <= 2500):
        irPercent = 10
    else:
        irPercent = 20

    inss = (10/100) * monthlySalary
    labelInss = "(-) INSS ( 10% )"+"        : R$"+str(inss) 
    fgts = (11/100) * monthlySalary
    labelFgts = "(-) FGTS ( 11% )"+"        : R$"+str(fgts) 
    irValue = (irPercent/100)*monthlySalary
    labelIRPercent = "(-) IR ("+str(irPercent)+" % )"+"        : R$"+str(irValue) 
    totalDiscount = inss+irValue
    labelDiscount = "Total de descontos"+"        : R$"+str(totalDiscount)
    realMonthlySalary = monthlySalary - totalDiscount
    labelRealSalary = "Salário Líquido"+"        : R$"+str(realMonthlySalary)
    labelSalary = "Salário bruto: ("+str(valueByHour)+" * "+str(workedHours)+" )"+"        : R$"+str(monthlySalary)
    print(labelSalary)
    print(labelIRPercent)
    print(labelInss)
    print(labelFgts)
    print(labelDiscount)
    print(labelRealSalary)

#calculateRealSalayByHour()

#13 Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.
def showWeekDay():
    day = int(input("Put a number between 1 and 7: "))
    if ( day == 1 ):
        print("1 - Domingo")
    elif ( day == 2 ):   
        print("2 - Segunda")
    elif ( day == 3 ):   
        print("3 - Terça")    
    elif ( day == 4 ):   
        print("4 - Quarta") 
    elif ( day == 5 ):   
        print("5 - Quinta") 
    elif ( day == 6 ):   
        print("6 - Sexta") 
    else :   
        print("7 - Sábado")   

#showWeekDay()   

#14 Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo
#Média de Aproveitamento  Conceito
#  Entre 9.0 e 10.0        A
#  Entre 7.5 e 9.0         B
#  Entre 6.0 e 7.5         C
#  Entre 4.0 e 6.0         D
#  Entre 4.0 e zero        E
#O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.

def showStatusGrade(grade, status):
    print("Your grade is "+grade+" and your status is "+status)

def calculateYourGrade():
    grade1 = float(input("Put your first grade: "))
    grade2 = float(input("Put your second grade: "))
    averageGrade = ((grade1+grade2)/2)
    if (averageGrade <= 4):
        showStatusGrade("E","REPROVADO")
    elif (averageGrade <= 6):
        showStatusGrade("D","REPROVADO")
    elif (averageGrade <= 7.5):
        showStatusGrade("C","APROVADO")
    elif (averageGrade <= 9):
        showStatusGrade("B","APROVADO")
    else:
        showStatusGrade("A","APROVADO")

#calculateYourGrade()

#15 Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
#Dicas:
#Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
#Triângulo Equilátero: três lados iguais;
#Triângulo Isósceles: quaisquer dois lados iguais;
#Triângulo Escaleno: três lados diferentes;

def checkTriagle():
    value1 = float(input("Put your first triangle's side: "))
    value2 = float(input("Put your second triangle's side: "))
    value3 = float(input("Put your third triangle's side:: "))
    if ( (value1 == value2) and (value1 == value3) ):
        print("Triângulo Equilátero: três lados iguais")
    elif ((value1 == value2) or (value1 == value3) or (value2 == value3)):
        print("Triângulo Isósceles: quaisquer dois lados iguais")
    else:
        print("Triângulo Escaleno: três lados diferentes")

#checkTriagle()

#16 Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
#Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
#Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
#Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
#Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;

def calculateSquareRoot():
    valueA = float(input("Coloque o valor de A  (ax2 + bx + c): "))
    if (valueA == 0):
        print("A equação não é do segundo grau e o programa será encerrado")
    else:
        valueB = float(input("Put b value (ax2 + bx + c): "))
        valueC = float(input("Put c value (ax2 + bx + c): "))
        delta = pow(valueB,2)-4*valueA*valueC
        if ( delta <0 ):
            print("A equação não possui raizes reais e o programa será encerrado")
        elif (delta == 0):
            valueX = (-valueB + math.sqrt(delta))/(2*valueA)
            print("A equação possui apenas uma raiz real que é: ",valueX)
        else:
            valueX_ = (-valueB + math.sqrt(delta))/(2*valueA)
            valueX__= (-valueB - math.sqrt(delta))/(2*valueA)
            print("A equação possui duas raiz reais; que são: "+str(valueX_)+" e "+str(valueX__))


#calculateSquareRoot()

#17 Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.
def calculaSeAnoEBissexto():
    year = int(input("Coloque o ano aqui: "))
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print("O ano é um ano bissexto (tem 366 dias).")
    else:
        print("O ano não é um ano bissexto (tem 365 dias).")    
       

#calculaSeAnoEBissexto()

#18 Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.
def checkIfdateIsValid():
    pattern = "dd/mm/aaaa" 
    date = str(input("Put your date here:"))   
    dateSplit = date.split("/")  
    if(len(dateSplit) == 3):
        if(int(dateSplit[0]) > 1 and int(dateSplit[0])<31 ):
            if(int(dateSplit[1]) > 1 and int(dateSplit[1])<=12 ):
                if(int(dateSplit[2]) > 1 and int(dateSplit[1])<=9999 ):
                    print("This date is valid")
                else:
                    print("This date is not valid")
            else:
                print("This date is not valid")
        else:
            print("This date is not valid")


#checkIfdateIsValid()

#19 Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo
def checkNumber():
    number = str(input("Put your number between 1 and 999: "))
    size = (len(number))
    if(size == 3 ):
        print(number[0]+" centenas, "+number[1]+" dezenas e "+number[2]+" unidades")
    elif (size == 2):
         print(number[0]+" dezenas e "+number[1]+" unidades")
    else: 
        print(number[0]+" unidades")

#checkNumber()

#20 Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e presentar:
#A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
#A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
#A mensagem "Aprovado com Distinção", se a média for igual a 10.
def checkStatusByAverageGrade():
    number1 = int(input("Put your first grade: "))
    number2 = int(input("Put your second grade: "))
    number3 = int(input("Put your third grade: "))
    averageGrade = (number1+number2+number3)/3
    if (averageGrade >=7 and averageGrade !=10):
        print("Aprovado, média: "+str(averageGrade))
    elif (averageGrade ==10):
        print("Aprovado com distinção, média: "+str(averageGrade))
    else:
        print("Reprovado, média: "+str(averageGrade))

#checkStatusByAverageGrade()

#21 Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas. 
#As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.
#Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
#Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.

def executeATM():
    valuetotal = float(input("Valor do saque: "))
    amountValue1 = int(input("Notas de R$ 1,00: "))
    amountValue5 = int(input("Notas de R$ 5,00: "))
    amountValue10 = int(input("Notas de R$ 10,00: "))
    amountValue50 = int(input("Notas de R$ 50,00: "))
    amountValue100 = int(input("Notas de R$ 100,00: "))
    sumValues = (amountValue1*1+amountValue5*5+amountValue10*10+amountValue50*50+amountValue100*100)
    if(sumValues == valuetotal):
        print(str(amountValue1)+" notas de "+"1 ,00 - "+str(amountValue5)+" notas de "+"5 ,00 - "+str(amountValue10)+" notas de "+"10 ,00 - "+str(amountValue50)+" notas de "+"50 ,00 - "+str(amountValue100)+" notas de "+"100 ,00")
    else:
        print("Quantidade de notas não referem ao valor total")

#executeATM()

#22 Faça um Programa que peça um número inteiro e determine se ele é par ou impar. Dica: utilize o operador módulo (resto da divisão).
def checkInNumberIsPar():
    number = int(input("Put your number: "))
    if (number % 2 == 0):
        print("Par")
    else:
        print("Impar")

#checkInNumberIsPar()

#23 Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de arredondamento.
def checkInNumberIsDecimal():
    number = float(input("Put your number: "))
    if (number.is_integer()):
        print("Integer")
    else:
        print("Decimal")

#checkInNumberIsDecimal()

def checkNumberIsPositive():
     number = float(input("Put your number: "))
     if (number > 0):
         print("Number is positive")
     else:
         print("Number is negative")


#24 Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
#par ou ímpar;
#positivo ou negativo;
#inteiro ou decimal.
def checkNumber():
    option = int(input("Press:\n[1]Check if number é par or ímpar\n[2]Check if number is positive or negative\n[3]Check if number is integer or decimal\n:"))
    if (option == 1):
        checkInNumberIsPar()
    elif (option == 2):
        checkNumberIsPositive()
    else:
        checkInNumberIsDecimal()

#checkNumber()

#25Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?" 
#O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
#Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
def checkYourParticipationInHomicide():
    print("--- -- -Responda as perguntas- -- ---")
    print("[1] - SIM\n[0] - NÃO")
    question1 = int(input("Telefonou para a vítima?: "))
    question2 = int(input("Esteve no local do crime?: "))
    question3 = int(input("Mora perto da vítima?: "))
    question4 = int(input("Devia para a vítima?: "))
    question5 = int(input("Já trabalhou com a vítima?: "))
    result = question1+question2+question3+question4+question5
    if(result == 2):
        print("Suspeita")
    elif ( result == 3 or result == 4 ):
        print("Cúmplice")
    elif (result == 5 ):
        print("Assassino")
    else:
        print("Inocente")

#checkYourParticipationInHomicide()
        
#26 Um posto está vendendo combustíveis com a seguinte tabela de descontos:
#Álcool:
#até 20 litros, desconto de 3% por litro
#acima de 20 litros, desconto de 5% por litro
#Gasolina:
#até 20 litros, desconto de 4% por litro
#acima de 20 litros, desconto de 6% por litro
#Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina),
# calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.
def checkPriceFuel():
    print("--- -- - PREÇO DE COMBUSTÍVEL - -- ---")
    print("********* Litro da gasolina: R$ 2,50 *********\n********* Litro do álcool: R$ 1,90 *********\n")
    print(" - Álcool:\n -- até 20 litros, desconto de 3% por litro\n -- acima de 20 litros, desconto de 5% por litro\n - Gasolina:\n -- até 20 litros, desconto de 4% por litro\n -- acima de 20 litros, desconto de 6% por litro")
    fuelType = str(input("Selecione o tipo de combustível\n[A] - Alcool\n[G] - Gasolina\n:"))
    amountFuel = float(input("Quantidade em litros: "))
    priceAlcohol = 1.9
    priceGasoline = 2.5
    if (amountFuel <= 20):
        if (fuelType == "A"):
            discount = (3/100)*(amountFuel*priceAlcohol)
            finalPrice = (amountFuel*priceAlcohol)-discount
        else:
            discount = (4/100)*(amountFuel*priceGasoline)   
            finalPrice = (amountFuel*priceGasoline)-discount
    else:
        if (fuelType == "A"):
            discount = (5/100)*(amountFuel*priceAlcohol)
            finalPrice = (amountFuel*priceAlcohol)-discount
        else:
            discount = (6/100)*(amountFuel*priceGasoline)
            finalPrice = (amountFuel*priceGasoline)-discount        
    print("Valor a ser pago: R$"+str(finalPrice))  

#checkPriceFuel()

#27 Uma fruteira está vendendo frutas com a seguinte tabela de preços:
#                      Até 5 Kg           Acima de 5 Kg
#Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
#Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
#Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total. 
#Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.

def calculateFruitBowlPrice():
    amountStrawberry = float(input("Quantidade de morango: "))
    amountApple = float(input("Quantidade de maçã: "))
    amountFruits = (amountStrawberry+amountApple)

    if (amountStrawberry <= 5):
        priceStrawberry = 2.5*amountStrawberry
    else:
         priceStrawberry = 2.2*amountStrawberry
    if (amountApple <= 5):
        priceApple = 1.8*amountApple
    else:
        priceApple = 1.5*amountApple
    if( amountFruits>=8 or (priceApple+priceStrawberry) >25 ):
        discount = (10/100)
        finalPrice = (priceApple+priceStrawberry) - (discount*(priceStrawberry+priceApple))
    else:
        finalPrice = (priceApple+priceStrawberry) 
    print("Valor a ser pago: R$"+str(finalPrice))
#calculateFruitBowlPrice()

#O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
#                      Até 5 Kg           Acima de 5 Kg
#File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
#Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
#Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
#Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há limites para a quantidade de carne por cliente.
#Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra. 
#Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.

def getMeatFromInt(type):
    if (type == 1): 
        return "File duplo"
    elif (type == 2): 
        return "Alcatra"
    else:
        return "Picanha"

def getPaymentFromInt(type):
    if (type == 1): 
        return "Cartão Tabajara"
    elif (type == 2): 
        return "Dinheiro"
    else:
        return "Cartão Crédito/Débito"


def calculatePriceToMeat():
    meat = int(input("Escolha sua carne: \n[1] - File duplo\n[2] - Alcatra\n[3] - Picanha\n:"))
    amount = float(input("Quantidade de carne \n:")) 
    payment = int(input("Forma de pagamento\n[1] - Cartão Tabajara\n[2] - Dinheiro\n[3] - Pix\n[4] - Cartão Crédito/Débito\n:"))
    if (amount <= 5):
        if (meat == 1):
            price = amount*4.9
        elif (meat == 2):
            price = amount*5.9
        else:
            price = amount*6.9
    else:
        if (meat == 1):
            price = amount*5.8
        elif (meat == 2):
            price = amount*6.8
        else:
            price = amount*7.8
    if (payment == 1):
        finalPrice = (price+ price*5/100)   
    else:
        finalPrice = price
    print("Comprovante fiscal")
    print("Tipo de carne: "+str(getMeatFromInt(meat)))
    print("Quantidade: "+str(amount)+" Kg")
    print("Tipo de Pagamento: "+str(getPaymentFromInt(payment)))
    print("Total da compra: R$ "+str(finalPrice))

#calculatePriceToMeat()
         




            

















