from django.shortcuts import render
from django.http import HttpResponse
from .forms import PhraseForm
import math

def bubblesort(list, label_list):
    for iter_num in range(len(list)-1,0,-1):
        for idx in range(iter_num):
            if list[idx]<list[idx+1]:
                temp = list[idx]
                list[idx] = list[idx+1]
                list[idx+1] = temp
                temp = label_list[idx]
                label_list[idx] = label_list[idx+1]
                label_list[idx+1] = temp

def string_to_list(data):
    a_list = data.split()
    map_object = map(int, a_list)            
    list_of_integers = list(map_object)
    return list_of_integers

def coseno(vec1, vec2):
    if len(vec1) != len(vec2):
        return -1

    numerator = 0
    modvec1 = 0
    modvec2 = 0
    for i in range(len(vec1)):
        numerator += vec1[i] * vec2[i]
        modvec1 += pow(vec1[i], 2)
        modvec2 += pow(vec2[i], 2)

    result = numerator / math.sqrt(modvec1 * modvec2)
    print(result)
    return result

def calculate_vectors(request):

    if request.method == 'POST':
        form = PhraseForm(request.POST)
        if form.is_valid():
            
            vec1 = string_to_list(form.cleaned_data['vec1'])            
            vec2 = string_to_list(form.cleaned_data['vec2'])
            vec3 = string_to_list(form.cleaned_data['vec3'])
            vec4 = string_to_list(form.cleaned_data['vec4'])
            vec5 = string_to_list(form.cleaned_data['vec5'])

            label_list = []
            result_list = []
            label_list.append('vec2')
            result_list.append(coseno(vec1, vec2))
            label_list.append('vec3')
            result_list.append(coseno(vec1, vec3))
            label_list.append('vec4')
            result_list.append(coseno(vec1, vec4))
            label_list.append('vec5')
            result_list.append(coseno(vec1, vec5))

            bubblesort(result_list, label_list)
            print(result_list)
            print(label_list)
            
            form.cleaned_data['result'] = ""
            for i in range(4):
                form.cleaned_data['result'] += "%s -> %s\n"%(label_list[i], result_list[i])
            new_form = PhraseForm(form.cleaned_data)

            return render(request, 'calculate_vectors.html', {'form': new_form})

    form = PhraseForm()
    return render(request, 'calculate_vectors.html', {'form': form})
