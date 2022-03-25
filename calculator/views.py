from django.shortcuts import render
from django.utils.datastructures import MultiValueDictKeyError


def recipes(request):
    try:

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

        servings = int(request.GET['servings'])
        recipe = request.GET.get('recipe')
        context = {
            'test': DATA[recipe],
        }
        context['test'].update((i, j * servings) for i, j in context['test'].items())
        return render(request, 'index.html', context)
    except KeyError:

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

        recipe = request.GET.get('recipe')
        context = {
            'test': DATA[recipe],
            'recipe': DATA[recipe].keys(),
            'ingredients': DATA[recipe].values(),
            #'length': len(list(DATA[recipe].keys()))
        }
        return render(request, 'index.html', context)
