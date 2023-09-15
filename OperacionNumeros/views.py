from django.shortcuts import render

def index(request):
    context = {
    }
    return render(request, 'Operaciones/index.html',context)

def resultado(request):
    if request.method == 'POST':

        numero1 = float(request.POST.get('numero1',0))
        numero2 = float(request.POST.get('numero2',0))
        operacion = request.POST.get('operacion','')

        resultado = None

        if operacion == 'sumar':
            resultado = numero1 + numero2
        elif operacion == 'restar':
            resultado = numero1 - numero2
        elif operacion == 'multiplicar':
            resultado = numero1 * numero2
        elif operacion == 'dividir':
            if numero2 != 0:
                resultado = numero1 / numero2
            else:
                resultado = 'Error: División por cero'
        else:
            resultado = 'Error: Operación no válida'

        context = {
            'resultado': resultado,
        }
        
        return render(request, 'operaciones/index.html', context)
    return render(request, 'operaciones/index.html')
