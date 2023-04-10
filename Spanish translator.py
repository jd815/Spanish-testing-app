import random
wordspa = ["comida", "cafe", "leche", "jugo de fruta", "naranja", "manzana", "toronja", "tomate", "agua", "te", "limon", "licuado", "llegar", "ver", "desayunar", "caminar", "tarde", "pronto/temprano", "mes", "semana", "pasado", "ano", "el ano pasado", "camisa", "camiseta", "pantalones", "zapatos", "chaqueta", "abrigo", "cinturon", "ocio", "enero", "febrero", "marzo", "abril"]
worden = ["food", "coffee", "milk", "fruit juice", "orange", "apple", "grapefruit", "tomato", "water", "tea", "lemon", "smoothie", "to arrive", "to watch", "to have breakfest", "to walk", "late", "early", "month", "week", "past", "year", "last year", "shirt", "t-shirt", "pants", "shoes", "jacket", "coat", "belt", "hobbies", "january", "february" , "march", "april"]
wordnos = []
wordnoe = []
print(len (wordspa))
x=0
while x<10:
    ranNum=random.randint(0,33)
    print (wordspa[ranNum])
    answer = input("What is this word in english:")
    if answer == (worden[ranNum]):
        print("Correct answer")
    elif answer != (worden[ranNum]):
        print("Wrong answer. The correct answer was:", worden[ranNum])
        wordnos.append(wordspa[ranNum])
        wordnoe.append(worden[ranNum])   
    x=x+1

print("now in spanish!")
i=0
while i<10:
    ranNum=random.randint(0,33)
    print (worden[ranNum])
    answer1 = input("What is this word in spanish:")
    if answer1 == (wordspa[ranNum]):
        print("Correct answer")
    elif answer1 != (wordspa[ranNum]):
        print("Wrong answer. The correct answer was:", wordspa [ranNum])
        wordnos.append(wordspa[ranNum])
        wordnoe.append(worden[ranNum])   
    i=i+1
    
y=0
while y<len (wordnos):
    print (wordnos[y], ":", wordnoe[y])
    y=y+1

