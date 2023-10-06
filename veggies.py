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
taco_dict = {
    'Kohlrabi': 1, 
    'Asparagus': 2, 
    'Eggplant': 3, 
    'onions': 4}
print(taco_dict)
salsa_heat_lvl = {
    'mild': "pico de gallo",
    'medium': "salsa verde", 
    'spicy': "salsa roja"}
print(salsa_heat_lvl)