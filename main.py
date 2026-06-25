from class_tutorial import Dog

d = Dog('Fido')
e = Dog('Buddy')

print(d.name)
print(e.name)
d.add_trick('roll_over')
e.add_trick('play dead')
print(d.tricks)
print(e.tricks)