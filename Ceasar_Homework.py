# WEEKEND HOMEWORK (calendar week 46) 
# De- and encryption algorithm, based on Julius Ceasar's method...
#
# Task 1 (a) (Decrypt) Following message: Asterix: "KDOORFDHVDUZLUKDEHQGHLQYHUVFKOXHVVHOXQJVYHUIDKUHQJHNQDFNW"
#
# Keyvalue = 3, Based on latin alphabet = 26 Sign's -> keyvalue 1..25
#

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

key = 3

message = "KDOORFDHVDUZLUKDEHQGHLQYHUVFKOXHVVHOXQJVYHUIDKUHQJHNQDFNW"

crypt = []

len_a = len(alphabet)

class Julius:

    def crypt():

        for c in message:
            crypt.append(alphabet[(alphabet.find(c)-key)%len_a]) # switch from "-" to "+" to de- and encrypt messages... (Task 5 (a/b))
            print("Task 1 (a) decryption: ",'"',''.join(crypt), '"')
            

    crypt()

# Solution Task 1 (a) -> "Hallo Ceasar wir haben dein Verschlüsselungsverfahren geknackt"
#
#
# Task 1 (b) (Decrypt) Following message: "Surjudpplhuxqj lvw hlqidfk qxu phjd jxw."

import string

message = "surjudpplhuxqj lvw hlqidfk qxu phjd jxw"

key = 23

result = ""

a = string.ascii_lowercase
x = []

for i in message:
    for i2 in a:
        if i == i2:
            ind = int(a.index(i2))
            x.append(ind+key)

for s in x:
    if s > len(a)-1:
        result += a[s-len(a)]
    else:
        result += a[s]

print("Task 1 (b) decryption: ",'"',' '.join(result), '"')

# Solution Task 1 (b) -> "Programmierung ist einfach nur mega gut"

# Task 1 (bb) Encrypt a own message... The message is: "Man muss nicht immer sagen was man denkt, aber immer denken was man sagt."

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

key = int(input("Please enter a Key value (Integer), for the following message: "))

newMessage = ""

message = "MAN MUSS NICHT IMMER SAGEN WAS MAN DENKT, ABER IMMER DENKEN WAS MAN SAGT."


for char in message.upper() :
    if char in alphabet :
        position = alphabet.find(char)
        newPosition = (position+key)%26
        newChar = alphabet[newPosition]
        newMessage += newChar
    else:
        newMessage += char

print(f"The old message is: {message}")
print(f"The encrypted message is: {newMessage}")