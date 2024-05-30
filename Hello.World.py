name = input("Give me your name: ")
print("Hello ",name,"!", end= " ")
age = int(input("How old are you? "))
year = int(2023)
date = int(year - age)
print("So you were born in", date,"? ", end="")
answer = input('')
while True:
    
    if answer == 'yes':
        print("Very well")
        break
    
    elif answer == 'no':
        print("sorry")
        break
    
    else:
        print("You must say yes or no: ", end="")
        answer = input('')
        continue

#sumowanie liczb
    
print("How many hours do you spend on your hobby every day? ", end="")
hobby = float(input(''))
print("Okay, let met count it...")
weekHobby = hobby * 5
print("So you spend ", weekHobby," h per week. Would you like to know how much do you pay for it every single day?", end="")
answer = input('')

while True:
    
    if answer == 'yes':
        print("Okay then...")
        break
    
    elif answer == 'no':
        print("sorry")
        break
    
    else:
        print("You must say yes or no: ", end="")
        answer = input('')
        continue
    
suma = ile = 0
    
while True:
    l1 = float(input("Give me first amount: " ))
    max = l1 
    l2 = float(input("Give me second amount: "))
    if l2 > max:
        max = l2
    l3 = float(input("Give me third amount: "))
    if l3 > max:
        max = l3
    l4 = float(input("Give me fourth amount: "))
    if l4 > max:
        max = l4
    l5 = float(input("Give me fifth amount: "))
    if l5 > max:
        max = l5
    break
    

liczba = float(l1+l2+l3+l4+l5)
suma= liczba
ile += 5

if ile == 0:
    print("You didn't provide any data, I won't calculate your average, meatball! ") 
else:
    print("The highest amount you've spent is =", max)
    print("Total amount is ", suma)
    print("Avarage amount is =", suma/ile)


     

# można je tez zapisać po prostu jako l, dzięki czemu zmniejszymy ilość zmiennych

#liczenie pola
import math

while True:
    x = int(input("Enter the side of the square to count the area: "))
    
    if x <=0 :
        print("There are no such squares")
        print("Enter a number greater than 0")
        y = int(input("The side of the square to count the area: "))
        if y == x or y <= 0:
            print("I said greater than 0, you idiot! ")
            z = int(input("The side of the square to count the area: "))
            if z >0:
                print ("At last, pal!")
                break
            elif z <=0:
                print("Szkoda strzępić ryja")
                break
        
    else:
        x > 0
        break



# obliczenie pola

pole = x * x 

# wyprowadzenie wyniku
print("The area of ​​the square is", pole)





