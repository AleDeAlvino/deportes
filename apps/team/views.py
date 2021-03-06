from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from .models import Team, Student
from .forms import StudentForm

# Create your views here.
def equipos(request):
    # .all = seleccionar todos los equipos
    equipos = Team.objects.all()
    print("===============")
    print(equipos)
    print("===============")
    return HttpResponse(equipos)

def estudiantes(request):
    #Todos los estudiantes
    estudiantes = Student.objects.all()
    print("===============")
    print(estudiantes)
    print("===============")
    return HttpResponse(estudiantes)

def estudiantes_plan(request, plan):
    #Todos los estudiantes por plan
    estudiantes = Student.objects.filter(plan = plan)
    print("===============")
    print(estudiantes)
    print("===============")
    return HttpResponse(estudiantes)

def estudiantes_equipo(request, id_equipo):
    #Todos los estudiantes por plan
    estudiantes = Student.objects.filter(team = id_equipo)
    print("===============")
    print(estudiantes)
    print("===============")
    return HttpResponse(estudiantes)

def team_details(request, Team_id):
    # Vista que registra un alumno en un taller
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('team_details', Team_id)
        team =Team.objects.get(pk=Team_id)
        students = Student.objects.filter(team = Team_id)
        return render(request, 'team_details.html',{'form':form, 'students':students, 'team':team})
    team =Team.objects.get(pk=Team_id)
    students = Student.objects.filter(team = Team_id)
    form = StudentForm(initial={'team':Team_id})
    return render(request, 'team_details.html', {'form':form, 'students':students, 'team':team})