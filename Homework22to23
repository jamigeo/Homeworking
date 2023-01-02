import random
import math

# Task 1) 

# Realisiere ein Programm, das eine Zeichenkette von

# Minimum 4 und Maximum 10 Zeichen einliest.

# Wenn die Eingabe korrekt ist, soll auf dem Bildschirm "Okay" erscheinen.
# Ist die String-Länge zu klein oder zu groß, soll eine entsprechende Fehlermeldung ausgegeben werden.string = input("Bitte geben Sie eine Zeichenkette ein: ")

string = input("Please insert a String with length, between 4-10 signs: ")

def stringCheck(string):

    if len(string) >= 4 and len(string) <= 10:
        print(f"Okay, your input was: {string}")
    else:
        if len(string) < 4:
            print("The String is to short!")
        else:
            print("The String is to long!")

stringCheck(string)

# Task 2)

# Schreibe zunächst eine Funktion, 
# die als Rückgabewert eine einfache sortierte Liste 
# mit 6 zufälligen Zahlen von 1 bis 49 liefert (6 aus 49). 
# Dabei soll eine Zahl jeweils nur ein Mal in der Liste vorkommen!
# Schreibe anschließend ein Programm, welches die Funktion 3 Mal aufruft und den Rückgabewert jeweils wieder in einer Liste speichert. 
# Am Ende geben Sie diese zweidimensionale Liste mit den drei Ziehungen 6 aus 49 auf dem Bildschirm aus.


def six_random_numbers():
    numbers = []
    while len(numbers) < 6:
        number = random.randint(1, 49)
        if number not in numbers:
            numbers.append(number)
    numbers.sort()
    return numbers

drawings = []

for i in range(3):
    drawing = six_random_numbers()
    drawings.append(drawing)

print(drawings)

# Task 3)

# Gesucht ist eine Zahl
# die kleiner 500.000 ist,
# deren Quersumme 43 beträgt und
# ein Quadrant ist (Ergebnis einer Zahl, die mit sich selbst mal genommen wird).

for i in range(1, 500000):

  if math.isqrt(i)**2 == i:

    digits = [int(d) for d in str(i)]
    digit_sum = sum(digits)

    if digit_sum == 43:

      print(f"The searched number is {i}.") # Die Basiszahl ist 707
      break
