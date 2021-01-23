# n = input("Enter a number: ")
# number = int(n)

# if number > 10 :
#     print("This is the number ", number)

#     print("This is inside the if block")

# print("exited")

# def print_HelloWorld():
#     print("Hola mundo!")

# def greet(lang):
#     if lang == 'es':
#         print('Hola!')
#     elif lang == 'fr':
#         print('Bonjour!')
#     else:
#         print('Hello!')

# print_HelloWorld()
# greet('es')

# def give_me_my_money(value):
#     return value

# val = give_me_my_money(5)
# print(val)

# val2 = give_me_my_money('hola')
# print(val2)

# arreglo = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(arreglo[2:5])

# try:
#     file = open('texxt.txt')
#     for line in file:
#         print(line.strip())
# except:
#     print("didn't work")


# text = file.read()
# print(text[:5])


# counts = dict()
# names = [ 'csev', 'cwen', 'csev', 'zqian', 'cwen']
# for name in names:
#     # if name not in counts:
#     #     counts[name] = 1
#     # else:
#     #     counts[name]+=1
#     counts[name] = counts.get(name, 0) + 1
# print(counts)

counts = dict()
print('Enter a line of text:')
line = input('')

words = line.split()

print('Words:', words)

print('Counting...')
for word in words:
    counts[word] = counts.get(word, 0) + 1
# print('Counts', sorted(counts.items()))


print( sorted( [ (v,k) for (k, v) in counts.items()], reverse=True))