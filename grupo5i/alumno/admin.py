from django.contrib import admin
from .models import Alumno, Frase
# Register your models here.

class comentarioIntLine(admin.TabularInline):
    model=Frase
    extra=1

class AlumnoAdmin(admin.ModelAdmin):
    fields=["Apaterno", "Amaterno", "nombre", "fecha_nacimiento", "fecha_ingreso"]
    list_display=["Apaterno", "Amaterno", "nombre"]
    inlines=[comentarioIntLine]



admin.site.register(Alumno, AlumnoAdmin)

@admin.register(Frase)
class FraseAdmin(admin.ModelAdmin):
    fields=["comentario", "Alumno_fk"]
    list_display=["comentario"]