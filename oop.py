from typing import Counter


class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
      print("Hello my name is "+ self.name + " and I am " + str(self.age))

p1 = Person("Aluel", 36)
p1.myfunc()

# sentence=input('Enter your sentence: ')
# print('Your sentence is: ' + sentence )
# word1=input('Enter the word to replace: ')
# word2=input('Enter the word to replace it with: ')
# print(sentence.replace(word1,word2))
fruits= ['oranges', 'bananas', 'mangoes', 'pineapples', 'Maperas']
print (type(fruits))
fruits[0]='bala'
fruits[4]='Mzabibu'
print(fruits)
print(len(fruits))
list1=['South Sudan', 'Kenya', 'Sudan', 'Uganda', 'Rwanda']
list2=['pen', 'pencil', 'book', 'rubber', 'ruler']
# list1.extend(list2)
# print(list1)
list2.append('laptop')
print(len(list2))
list2.insert(1, 'file')
print(list2)
list1.remove('Uganda')
print(list1)
list2.clear()
print(list2)
print(list1.index('South Sudan'))
print(list1.count('Kenya'))
list1.reverse()
print(list1)
list3=list1.copy()
print(list3)
list3.pop()
print(list3)
del list3[0]
print(list3)
