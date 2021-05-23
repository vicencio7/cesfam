from django.db import models


# Create your models here.
class Paciente(models.Model):
    rut = models.CharField(max_length=12, null=False, blank=False, primary_key=True)
    nombre = models.CharField(max_length=50, null=False, blank=False)
    apellido = models.CharField(max_length=50, null=False, blank=False)
    prevision_social = models.CharField(max_length=50, null=False, blank=False)
    direccion = models.CharField(max_length=100, null=False, blank=False)
    edad = models.IntegerField(null=False, blank=False)
    numero_telefono = models.CharField(max_length=50, null=False, blank=False)
    sexos = [("1", "Hombre"),("2", "Mujer")]
    sexo_paciente = models.CharField(max_length=50, null=False, blank=False, choices=sexos)

class Contacto(models.Model):
    rut_paciente = models.ForeignKey(Paciente,null=False, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50, null=False, blank=False)
    apellido = models.CharField(max_length=50, null=False, blank=False)
    numero_telefono_contacto = models.CharField(max_length=50, null=False, blank=False)
    parentezco = models.CharField(max_length=50, null=False, blank=False)

class Programa(models.Model):
    nombre_programa = models.ForeignKey(Paciente,null=False, on_delete=models.CASCADE)
    nombreprograma = [("1", "Orientacion"), ("2", "Salud Mental"), ("3", "Red Odontologica"), ("4", "Red Oncologica"), ("5", "Quimicos Farmaceuticos"), ("6", "Red Imagenologia"), ("7", "Red ITS"),                       ("8", "Red Medicina Nuclear"), ("9", "Red Telemedicina"), ("10", "Red Salud Sexual")]
    programa = models.CharField(max_length=50, null=False, blank=False, choices=nombreprograma)
    especialidad = [("1", "Médico General"), ("2", "Enfermera"), ("3", "Nutricionista"), ("4", "Fonoaudiologo"),("5", "Psicologo"), ("6", "Kinesiologo"), ("7", "Trabajor Social"), ("8", "Teraupetica Ocupacional"), ("9", "Tecnico Paramedico")]
    especialidadprofesional = models.CharField(max_length=50, null=False, blank=False, choices=especialidad)

class Cita(models.Model):
    cita_paciente = models.ForeignKey(Paciente,null=False, on_delete=models.CASCADE)
    fecha_cita = models.DateTimeField()

class Reporte(models.Model):
    usuario_responsable = models.ForeignKey(Paciente,null=False, on_delete=models.CASCADE)
    asistencia = models.IntegerField(null= False, blank=False)
    NSP = models.IntegerField(null= False, blank=False)






