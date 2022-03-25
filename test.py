DATA = {
    'omelet': {
        'eggs': 2,
        'milk, l': 0.1,
        'salt, t.s': 0.5,
    },
    'paste': {
        'pasta, g': 0.3,
        'cheese, g': 0.05,
    },
    'burger': {
        'bread, slices': 1,
        'sausage, slices': 1,
        'cheese, slices': 1,
        'tomato, slices': 1,
    },

}
context = {}
recipe = DATA['omelet']
for x in recipe:
    context = {
        'recipe': x
    }
print(context)