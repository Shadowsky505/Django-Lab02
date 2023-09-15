from django.shortcuts import render

def index(request):
    context = {
        'titulo':'Formulario'
    }
    return render(request, 'encuesta/formulario.html', context)

def enviar(request):
    context = {
        'titulo':'Respuesta',
        'nombre':request.POST['nombre'],
        'clave':request.POST['clave'],
        'educacion':request.POST['educacion'],
        'nacionalidad':request.POST['nacionalidad'],
        'idiomas':request.POST.getlist('idiomas'),
        'correo':request.POST['email'],
        'website':request.POST['sitioweb'],
    }
    return render(request, 'encuesta/respuesta.html', context)