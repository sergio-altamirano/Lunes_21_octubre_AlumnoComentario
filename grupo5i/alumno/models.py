from django.db import models

# Create your models here.

class Alumno(models.Model):
    Apaterno=models.CharField(max_length=50,verbose_name="Apellido paterno")
    Amaterno=models.CharField(max_length=50,verbose_name="Apellido materno")
    nombre=models.CharField(max_length=100,verbose_name="Nombre")
    fecha_nacimiento=models.DateField(verbose_name="fecha de nacimiento", null=False,blank=False)
    fecha_ingreso=models.DateField(verbose_name="fecha de ingreso", null=False,blank=False)

    class Meta:
        db_table="alumnos"
        verbose_name="Alumno"
        verbose_name_plural="alumnos"

    def __str__(self) -> str:
        return self.nombre


class Frase(models.Model):
    comentario=models.TextField(verbose_name="comentario",max_length=400)
    Alumnos_fk=models.ForeignKey(Alumno, on_delete=models.CASCADE)

    class Meta :
        verbose_name="Frase"
        verbose_name_plural="Frases"