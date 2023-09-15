from django.shortcuts import render
import math

def calcular_volumen_cilindro(altura, diametro):
    radio = diametro / 2
    volumen = math.pi * radio**2 * altura
    return volumen

def index(request):
    
    return render(request, 'volumenCilindro/index.html')
def resultado(request):
    
    if request.method == 'POST':
        altura = float(request.POST['altura'])
        diametro = float(request.POST['diametro'])
        volumen = round(calcular_volumen_cilindro(altura, diametro),2)
        return render(request, 'volumenCilindro/index.html', {'volumen': volumen})

    return render(request, 'volumenCilindro/index.html')