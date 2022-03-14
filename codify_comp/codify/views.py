
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Company, Employee
from django.http import HttpResponse

def Employee_view(request):
    employees = Employee.objects.all()
    return render(request, 'render.html', {'employees': employees})

def detail_view(request, id):
    employee_detail = Employee.objects.get(id=id)
    return render(request, 'detail.html', {'employee_detail': employee_detail})

def delete_view(request, id):
    delete_employee = Employee.objects.get(id=id)
    delete_employee.delete()
    return HttpResponse("сотрутник удалён")

def create_view(request):
    
    if request.method == "GET":
        companies = Company.objects.all()
        return render(request, 'create.html', {'companies': companies})

    if request.method == "POST":
        first_name = request.POST.get('first_name')
        surname = request.POST.get('surname')
        last_name = request.POST.get('last_name')
        date_of_birth = request.POST.get('date_of_birth')
        working_date = request.POST.get('working_date')
        job = request.POST.get('job')
        company_id = request.POST.get('company')
        
        company = Company.objects.get(id=company_id)
        new_employees = Employee(
            first_name=first_name,
            surname=surname,
            last_name=last_name,
            date_of_birth=date_of_birth,
            working_date=working_date,
            job=job,
            company=company
            )  
        new_employees.save()

        return redirect(reverse('all_employees'))

    
def update_view(request, id):
    employee = Employee.objects.get(id=id)
    if request.method == "GET":
        companies = Company.objects.all()
        context = {
            'companies': companies,
            'employee': employee,
        }
        return render(request, 'update.html', context)

    if request.method == "POST":
        first_name = request.POST.get('first_name')
        surname = request.POST.get('surname')
        last_name = request.POST.get('last_name')
        date_of_birth = request.POST.get('date_of_birth')
        working_date = request.POST.get('working_date')
        job = request.POST.get('job')
        company_id = request.POST.get('company')
        
        company = Company.objects.get(id=company_id)

        employee.first_name = first_name
        employee.surname = surname
        employee.last_name = last_name
        employee.date_of_birth = date_of_birth
        employee.working_date = working_date
        employee.job = job
        employee.company_id = company_id

        employee.save()

        return redirect(reverse('all_employees'))