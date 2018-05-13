#james galante
#10.20.15

pets = ['cat','dog','rabbit','hamster']

#list methods
#append
print(pets)
pets.append('rat')
print(pets)


print(pets)
pets.append('dog')
print(pets)

#index()
dog_1 = pets.index('dog')
print(dog_1, pets[dog_1])

#index second dog 
dog_2 = dog_1 + 1 + pets[dog_1 + 1:].index('dog')
print(dog_2, pets[dog_2])


#insert()
print(pets)
pets.insert(2, 'snake')
print(pets)

#sort()
pets.sort()
print(pets)

#revesre()
pets.reverse()
print(pets)

#Tuples
my_tuple = (1,2,3,4)
print(my_tuple)
my_tuple = ('python',)
print(my_tuple)


fixed_pets = tuple(pets)
print(fixed_pets)














