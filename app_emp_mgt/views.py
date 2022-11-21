from django.shortcuts import render, redirect

from app_emp_mgt.models import Employee


def index(request):
    return render(request, "index.html")


def master_employee(request):
    employees = Employee.objects.all()
    return render(request, 'employee/master.html', context={'msg': '', 'employees': employees})


def edit_employee(request, pk):
    if request.method == "POST":
        try:
            employee = Employee.objects.get(pk=pk)
            employee.name = request.POST.get("name", employee.name)
            employee.gender = request.POST.get("gender", employee.gender)
            employee.cont_no = request.POST.get("cont_no", employee.cont_no)
            employee.email = request.POST.get("email", employee.email)
            employee.save()
            return redirect('master')
        except Exception as e:
            return render(request, 'employee/edit.html', context={'msg': str(e), 'employee': None})
    else:
        try:
            employee = Employee.objects.get(pk=pk)
            return render(request, 'employee/edit.html', context={'msg': '', 'employee': employee})
        except(Employee.DoesNotExist, Exception) as e:
            return render(request, 'employee/edit.html', context={'msg': str(e), 'employee': None})


def delete_employee(request, pk):
    if request.method == "POST":
        try:
            employee = Employee.objects.get(pk=pk)
            employee.delete()
            return redirect('master')
        except(Employee.DoesNotExist, Exception) as e:
            return render(request, 'employee/delete.html', context={'msg': str(e), 'employee': None})
    else:
        try:
            employee = Employee.objects.get(pk=pk)
            return render(request, 'employee/delete.html', context={'msg': '', 'employee': employee})
        except(Employee.DoesNotExist, Exception) as e:
            return render(request, 'employee/delete.html', context={'msg': str(e), 'employee': None})


def create_employee(request):
    if request.method == "POST":
        name = request.POST.get("name")
        gender = request.POST.get("gender")
        cont_no = request.POST.get("cont_no")
        email = request.POST.get("email")
        try:
            employee = Employee.objects.create(name=name, gender=gender, cont_no=cont_no, email=email)
            return redirect('master')
        except Exception as e:
            return render(request, 'employee/create.html', context={'msg': str(e), 'employee': None})
    else:
        return render(request, 'employee/create.html', context={})
