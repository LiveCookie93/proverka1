text = input("Введите текст на английском языке: ")
print(len(text))

print(text.lower())

glas = set("aeiou")
count = 0
for i in text:
    if i in glas:
        count +=1
print("Колличество гласных в предложении: ", count)

text = text.replace("ugly", "beauty")
print(text)

print(text.startswith("The"))
print(text.endswith("end"))