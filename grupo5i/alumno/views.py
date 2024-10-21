from django.shortcuts import render, get_object_or_404
from .models import Alumno

# Create your views here.
def index_vista(resquest):
    misAlumnos=Alumno.objects.all().order_by("id")
    return render (resquest, "index.html",{"misAlumnos": misAlumnos})

def Alumno_vista(resquest, id):
    alumno=get_object_or_404(Alumno, id=id)
    return render(resquest,'Alumno.html',{'objeto':alumno})
