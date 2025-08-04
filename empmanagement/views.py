# Create your views here.

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import ADD_EMPFORM
from .models import ADD_EMP
from django.db.models import Q

from django.shortcuts import get_object_or_404


@login_required(login_url="admin_login")  # Redirect if not logged in
def dashboard(request):
    return render(request, 'emp_dashboard.html')

def admin_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")  # Make sure "pass" matches your input name in HTML

        user = authenticate(request, username=username, password=password)

        if user is not None:
            if user.is_staff:  # Allow only admin users to log in
                login(request, user)
                return redirect('dashboard')  # Change this to your admin dashboard page
            else:
                messages.error(request, "You are not authorized to access this page.")
        else:
            messages.error(request, "Invalid username or password")

    return render(request, "admin_login.html")

def admin_logout(request):
    logout(request)
    return redirect("admin_login")

@login_required(login_url="admin_login")  # Redirect if not logged in
def add_emp(request):
    if request.method=='POST':
        form=ADD_EMPFORM(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_emp')
    else:
        form=ADD_EMPFORM()
    return render(request,'add_emp.html',{'form':form})
    

def view_emp(request):
    query = request.GET.get('q')  # 'q' is the name of the input field in the search form
    if query:
        employees = ADD_EMP.objects.filter(Q(name__icontains=query) | Q(empid__icontains=query))
        # You can also search by empid, email, etc.
        # Example: ADD_EMP.objects.filter(Q(name__icontains=query) | Q(empid__icontains=query))
    else:
        employees = ADD_EMP.objects.all()
    return render(request, 'view_emp.html', {'employees': employees})


@login_required(login_url="admin_login")  # Redirect if not logged in
def delete_emp1(request,id):
    emp = ADD_EMP.objects.get(id=id)
    emp.delete()
    return redirect('view_emp')  # Redirect back to the list




def update_emp(request, id):
    mem = get_object_or_404(ADD_EMP, id=id)
    return render(request, 'update_emp.html', {'mem': mem})

def update_records(request, id):
    if request.method == "POST":
        mem = get_object_or_404(ADD_EMP, id=id)
        mem.name = request.POST.get('name')
        mem.contact = request.POST.get('contact')
        mem.email = request.POST.get('email')
        mem.age = request.POST.get('age')
        mem.gender = request.POST.get('gender')
        mem.empid = request.POST.get('empid')
        mem.dept = request.POST.get('dept')
        mem.save()
        return redirect("view_emp")
    return redirect(f"/update_emp/{id}")

    




