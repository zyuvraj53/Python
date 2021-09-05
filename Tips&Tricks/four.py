names = ['Peter Parker', 'Clark Kent', 'Wade Wilson', 'Bruce Wayne']
heroes = ['Spider-man', 'Superman', 'Deadpool', 'Batman']
universes = ['Marvel', 'DC', 'Marvel', 'DC']

for name, hero, universe in zip(names, heroes, universes):
  print(f'{name} is actually {hero} from {universe}')
  
print('--- --- --- --- --- --- --- --- --- ---')
  
for value in  zip(names, heroes, universes):
  print(f'{value[0]} is actually {value[1]} from {value[2]}')
