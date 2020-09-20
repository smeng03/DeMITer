from django.shortcuts import render

# Create your views here.
from catalog.models import student, solvedProblem, unsolvedProblem
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .match import match

from .forms import ProblemsForm

matches = []

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_students = student.objects.all().count()
#    num_solved_problem = solvedProblem.objects.all()[0].getStudent()[0].name

    if request.method == 'POST':
        form = ProblemsForm(request.POST)
        if(form.is_valid()): #stores this in database
            name = form.cleaned_data['name']
            kerb = form.cleaned_data['kerb']
            grad_year = form.cleaned_data['grad_year']
            new_student = student(name, kerb, grad_year)
            new_student.save()
            
            s_class_name = form.cleaned_data['s_class_name']
            s_assign_name = form.cleaned_data['s_assign_name']
            s_question_number = form.cleaned_data['s_question_number']
            
            k=-1
            for i in solvedProblem.objects.all():
                if(i.class_name==s_class_name and i.assign_name==s_assign_name and i.question_number==s_question_number):
                    k = i
            if k!=-1:
                new_solved = solvedProblem(class_name=s_class_name, assign_name=s_assign_name, question_number=s_question_number)
                new_solved.save()
                new_solved.student_list.add(new_student)
            else:
                solvedProblem.objects.all()[k].student_list.add(new_student)

            u_class_name = form.cleaned_data['u_class_name']
            u_assign_name = form.cleaned_data['u_assign_name']
            u_question_number = form.cleaned_data['u_question_number']
            
            k=-1
            for i in unsolvedProblem.objects.all():
                if(i.class_name==u_class_name and i.assign_name==u_assign_name and i.question_number==u_question_number):
                    k = i
            if k!=-1:
                new_unsolved = unsolvedProblem(class_name=u_class_name, assign_name=u_assign_name, question_number=u_question_number)
                new_unsolved.save()
                new_unsolved.student_list.add(new_student)
            else:
                unsolvedProblem.objects.all()[k].student_list.add(new_student)
            
            all_kerbs = []
            all_solved = []
            all_unsolved = []
            k = -1
            a=0
            for i in student.objects.all():
                all_kerbs.append(i.kerb)
                temp_sol_list = []
                temp_unsol_list = []
                for j in i.solvedproblem_set.all():
                    temp_sol_list.append(j.id)
                all_solved.append(temp_sol_list)
                for l in i.unsolvedproblem_set.all():
                    temp_unsol_list.append(l.id)
                all_unsolved.append(temp_unsol_list)
                if i.kerb==new_student.kerb:
                    k = a
                a+=1
            print(all_kerbs)
            print(all_solved)
            print(all_unsolved)
            if (k!=-1):
                matches1 = match(all_kerbs, all_solved, all_unsolved)
                for i in matches1[k]:
                    for j in student.objects.all():
                        if i == j.kerb:
                            matches.append([j.name, i])
                print(matches1)
                print(matches)
                matchlist = ' '
                for i in matches:
                    matchlist += "\n" + i[0] + " (kerb: " + i[1] + ")"
                context = {'matches':matchlist, 'num_students':num_students,}
                print(matchlist)
                return render(request, 'matchresult.html', context=context)# sends it back to home page unless we have a page which displays matches
           
    else:
        form = ProblemsForm()

    context = {
        'form':form,
        'num_students': num_students,
    #    'num_solved_problem':  num_solved_problem,
        'matches': matches,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)