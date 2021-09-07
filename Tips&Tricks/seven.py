class Person():
  pass

person = Person()

first_key = 'first'
first_val = 'Corey'

setattr(person, 'first', 'Corey')
first = getattr(person, first_key)

print(person.first)