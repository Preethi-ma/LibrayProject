from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, redirect


# Create your views here
from django.views.decorators.cache import cache_control, never_cache

from Libraryapp.models import Student, Course, Books, Issue_Book

# @cache_control(no_cache=True,revalidate=True, nostore=True)
# @never_cache
def student_reg_fun(request):
    course = Course.objects.all()
    return render(request, 'StudentReg.html',{'Course_Data': course})

# @cache_control(no_cache=True,revalidate=True, nostore=True)
# @never_cache
def admin_reg_fun(request):
    return render(request, 'AdminReg.html')

# @cache_control(no_cache=True,revalidate=True, nostore=True)
# @never_cache
def log_fun(request):
    return render(request, 'login.html', {'data': ''})


# @cache_control(no_cache=True,revalidate=True, nostore=True)
# @never_cache
def logdata_fun(request):

    User_Name = request.POST['txtname']
    User_Password = request.POST['txtpassword']
    User1 = authenticate(username=User_Name,
                         password=User_Password)  # it is used to compare user table is present or not
    if User1 is not None:
        if User1.is_superuser:
            login(request, User1)
            return redirect('home')
        else:
            return render(request, 'login.html', {'data': 'User is not super user'})  # redirect('log')
    elif Student.objects.filter(Q(Student_Name=User_Name) & Q(Student_Password=User_Password)).exists:
        request.session['n'] = User_Name
        return render(request,'studenthome.html',{'Student':User_Name})

    else:
        return render(request, 'login.html', {'data': 'enter proper userName and Password'})

# @cache_control(no_cache=True,revalidate=True, nostore=True)
# @never_cache
def regdata_fun(request):
    User_Name = request.POST['txtname']
    User_Email = request.POST['txtemail']
    User_Password = request.POST['txtpassword']

    if User.objects.filter(Q(username=User_Name) | Q(email=User_Email)).exists():
        return render(request, 'AdminReg.html', {'data': 'Username,email and password is already is exists'})
    else:
        u1 = User.objects.create_superuser(username=User_Name, email=User_Email, password=User_Password)
        u1.save()
        return redirect('log')


# @cache_control(no_cache=True,revalidate=True, nostore=True)
# @never_cache
def sregdata_fun(request):
    s1Name = request.POST['txtname']
    s1Phno = request.POST['txtphno']
    if Student.objects.filter(Q(Student_Name=s1Name) | Q(Student_Phno=s1Phno)).exists():
        return render(request, 'StudentReg.html', {'data': 'Studentname and Phno is already is exists'})
    else:
        s1 = Student()
        s1.Student_Name = request.POST['txtname']
        s1.Student_Password = request.POST['txtpassword']
        s1.Student_Phno = request.POST['txtphno']
        s1.Student_Semester = request.POST['txtsemester']
        s1.Student_Course_id = Course.objects.get(Course_Name=request.POST['ddlcourse'])
        s1.save()
        return redirect('log')

# @login_required
# @cache_control(no_cache=True,revalidate=True, nostore=True)
# @never_cache
def home_fun(request):
    return render(request, 'home.html')

# @login_required
# @cache_control(no_cache=True,revalidate=True, nostore=True)
# @never_cache
def addbook_fun(request):
    course = Course.objects.all()
    return render(request, 'addbook.html', {'Course_Data': course})
# @login_required
# @cache_control(no_cache=True,revalidate=True, nostore=True)
# @never_cache
def readdata_fun(request):
    b1 = Books()
    b1.Book_Name = request.POST['txtname']
    b1.Author_Name = request.POST['txtauthor']
    b1.Course_id = Course.objects.get(Course_Name=request.POST['ddlcourse'])
    b1.save()
    return redirect('add_book')
# @login_required
# @cache_control(no_cache=True,revalidate=True, nostore=True)
# @never_cache
def displaybook_fun(request):

    b1 = Books.objects.all()
    return render(request, 'displaybook.html',{'data': b1})

# @login_required
# @cache_control(no_cache=True,revalidate=True, nostore=True)
# @never_cache
def update_fun(request,id):
    b1 = Books.objects.get(id=id)
    course = Course.objects.all()

    if request.method == 'POST':
        b1.Book_Name = request.POST['txtname']
        b1.Author_Name = request.POST['txtauthor']
        b1.Course_id = Course.objects.get(Course_Name=request.POST['ddlcourse'])
        b1.save()
        return redirect('display_book')

    return render(request, 'update.html', {'data': b1,'Course_Data': course})

# @login_required
# @cache_control(no_cache=True,revalidate=True, nostore=True)
# @never_cache
def delete_fun(request,id):
    b1 = Books.objects.get(id=id)
    b1.delete()

    return redirect('display_book')

#
# @cache_control(no_cache=True,revalidate=True, nostore=True)
# @never_cache
def log_out_fun(request):
    logout(request)
    return redirect('log')

# @login_required
# @cache_control(no_cache=True,revalidate=True, nostore=True)
# @never_cache
def assignbook_fun(request):
    course = Course.objects.all()
    return render(request, 'assignbook.html', {'Course_Data': course})


# @login_required
# @cache_control(no_cache=True,revalidate=True, nostore=True)
# @never_cache
def areaddata_fun(request):
    s1 = Student.objects.filter(Q(Student_Semester=request.POST['txtsemester']) & Q(Student_Course_id=Course.objects.get(Course_Name=request.POST['ddlcourse'])))
    b1 = Books.objects.filter(Course_id=Course.objects.get(Course_Name=request.POST['ddlcourse']))
    return render(request, 'assignbook.html', {'dataa': s1, 'datab': b1})
# @login_required
# @cache_control(no_cache=True,revalidate=True, nostore=True)
# @never_cache
def sreaddata_fun(request):
    i = Issue_Book()
    i.Student_Name = Student.objects.get(Student_Name=request.POST['txtname'])
    i.Book_Name = Books.objects.get(Book_Name=request.POST['txtbook'])
    i.Start_Date = request.POST['txtstart']
    i.End_Date = request.POST['txtend']
    i.save()
    return redirect('assign_book')

# @login_required
# @cache_control(no_cache=True,revalidate=True, nostore=True)
# @never_cache
def issuebook_fun(request):
    i = Issue_Book.objects.all()
    return render(request, 'issuebook.html',{'data': i})

# @login_required
# @cache_control(no_cache=True,revalidate=True, nostore=True)
# @never_cache
def deleted_fun(request,id):
    i = Issue_Book.objects.get(id=id)
    i.delete()
    return redirect('issue_book')

# @login_required
# @cache_control(no_cache=True,revalidate=True, nostore=True)
# @never_cache
def updated_fun(request,id):
    i = Issue_Book.objects.get(id=id)
    s1 = Student.objects.get(id=i.Student_Name_id)
    b1 = Books.objects.filter(Course_id=s1.Student_Course_id)
    if request.method == 'POST':
        i.Student_Name = Student.objects.get(Student_Name=request.POST['txtname'])
        i.Book_Name = Books.objects.get(Book_Name=request.POST['txtbook'])
        i.Start_Date = request.POST['txtstart']
        i.End_Date = request.POST['txtend']
        i.save()
        return redirect('issue_book')
    return render(request, 'updated.html', {'data': i, 'datab': b1})

# @login_required
# @cache_control(no_cache=True,revalidate=True, nostore=True)
# @never_cache
def issuedbook_fun(request):
    i = Issue_Book.objects.filter(Student_Name=Student.objects.get(Student_Name=request.session['n']))
    return render(request,'issuedbook.html',{'data': i})

# @login_required
# @cache_control(no_cache=True,revalidate=True, nostore=True)
# @never_cache
def studenthome_fun(request):
    student = request.session['n']
    return render(request, 'studenthome.html', {'Student':student})


def profile_fun(request):
    s1 = Student.objects.get(Student_Name=request.session['n'])
    return render(request, 'profile.html', {'data': s1})


def update_profile_fun(request):
    s1 = Student.objects.get(Student_Name=request.session['n'])
    s1.Student_Name = request.POST['txtname']
    s1.Student_Password = request.POST['txtpassword']
    s1.Student_Phno = request.POST['txtphno']
    s1.Student_Semester = request.POST['txtsemester']
    s1.save()

    return redirect('profile')

def ureaddata_fun(request):
    s1 = Student.objects.get(Student_Name=request.session['n'])
    return render(request, 'updateprofile.html', {'data': s1})

