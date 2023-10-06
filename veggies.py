veggie_1 = 'Kohlrabi'
veggie_2 = 'Asparagus'
taco = [veggie_1, veggie_2]
print(taco)
taco.append('Eggplant')
print(taco)
extras = ['onions', 'candy corn']
taco.extend(extras)
print(taco)
taco.remove('candy corn')
print(taco)
print(taco[0:2])