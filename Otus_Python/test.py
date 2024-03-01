# print("Результат:", 27 ** 5) #** возведение в степень\ //-rounding when dividing
# print('hello', 7, 14, '.', sep='|', end='') #sep- install delimiter/ end='' no new line
# print('dad \' \n get', '\n find') #\n- new line \t- tabulation
#print("Результат:", min(1,4,6,-7,5), max(1,4,6,-7,5), abs(-4), pow(8,2), round(5/3))
#input("Enter your age: ") #receiving data from ther user
number = 5 #int
float = 4.8765 #float
boolean = True #bool
world = 'result: ' #string

#print(world + str(number + float))
#num1 = int(input('Enter the first number'))

#num2 = int(input('Enter second number')) #data from outside
#print('result:', num1 * num2)
#print('Result', num1 + num2)
#print('Result', num1 - num2)
#print('Result', num1 / num2)
#print('Result', num1 ** num2)

#user_number = int(input('Enter number:'))
#if user_number < 5: #condition
    #print('we are in place')
#elif user_number > 5: #additional condition
        #print('number is bigger that 5')
#else:  #everything above didn't work
    #print('you entered  5')

    #Ternary operator
#data = input()
#number = 5 if data =='Five' else 0
#print(number)

       #Cycles
#for i in range (1, 6, 2):
   # print(i)
#count = 0
#world = 'i work here'
#for a in world:
    #if a == 'w':
       # count +=1
#print('Count:', count)

#isHashCar = True
#while isHashCar:
    #if input('enter data ') == 'Stop':
        #isHashCar = False
#for s in range(11):
    #if s >= 5:
       # break # stop sycle
    #if s % 2 == 0:
        #continue # skip value
    #print(s)
nums = [1, 3, 5, 7, 8, 9, 12, 24, -5, True, 'hello', 7.65, [1, 4]]
nums[0] =111
#print(nums[-1][1])

numbers = [5, 2, 8]
numbers.append(100)
numbers.insert(3, False)
g = [9, 13, 47]
numbers.extend(g)#insert pack
numbers.sort()
#numbers.reverse()
numbers.pop() #delete last element
numbers.remove(2) # delete meaning
#print(numbers.count(8)) #count matches
#print(len(numbers)) #count meaning
#print(numbers)
#data = [1, 'name', 5, 8, 13, -4, 5.6]
#for d in data:
     #print(d)
#n = int(input('Enter length: '))
#suprem = []
#i = 0
#while i < n:
    # string = 'Enter element №' + str(i + 1) + ':'
     #suprem.append(input(string))
    # i += 1
#print(suprem)

     #Функции для строк
#word = "footbal, basketbal, tenis, skate"
#print(word.split('_')) #islower; isupper; lower; capitalize; find; split
#hobby = word.split(', ')
#for i in range(len(hobby)):
    #hobby[i] = hobby[i].capitalize()
#result = ', '.join(hobby) #return everything to string
#print(result)

People = (1, 3, 5, 6, 8, True, 'Hello') #tuple
#People[0] = 5 no
flat = [1,7,5]
#new_flat = tuple(flat)
#q = tuple('Hello world')
#print(q)
#print(new_flat)

#(playlist_1 = {'Три белых коня', 'Happy new year', 'Снежинка', 'Новогодняя', 'Mom'}
#playlist_2 = {'Last christmas', 'Снежинка', 'Happy new year', 'Mom'}
#new_sing =['she', 'love', 'cloudy clouds']
##playlist_3 = playlist_1.difference(playlist_2) # Output only different values
#playlist_4 = playlist_1.intersection(playlist_2) # Output of identical values
# playlist_5 = playlist_1.union(playlist_2) # merge without repetition

#print(playlist_4)

#Словари
country = {'code': 'RU', 'name': 'Russia', 'population': 144, 'capital': 'Moscow'}
address = dict(city= 'Moscow', strit= 'Dosflota proezd', home= 7, apartment= 107)
print(address["city"])



