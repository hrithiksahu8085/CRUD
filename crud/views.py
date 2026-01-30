from django.shortcuts import render, redirect 
from blog.models import UserDetails



def home(req):
    if req.method == 'POST':

    
        FullName = req.POST.get('fullName')
        Email = req.POST.get('email')
        Mobile = req.POST.get('mobile')
        Age = req.POST.get('age')
        Course = req.POST.get('course')
        Image = req.FILES.get('image')
        

        conn = UserDetails.objects.create(name=FullName,email=Email,mobile=Mobile,age=Age,course=Course,images=Image)
        conn.save()  
        
    else:
        print('sorry')    



    return render(req, 'home.html')


def table(req):
    userData = UserDetails.objects.all()
    print(userData)
    data = {
        'userDetail' : userData
    } 
    return render(req, 'table.html', data)


def deleteUser(req, id):
    user = UserDetails.objects.get(id=id)
    user.delete()
    return render(req,'table.html')


def updateUser(req, id):
    user = UserDetails.objects.get(id=id)
    if req.method == 'POST':
        user.name = req.POST.get('fullName')
        user.email = req.POST.get('email')
        user.mobile = req.POST.get('mobile')
        user.age = req.POST.get('age')
        user.course = req.POST.get('course')

        
        user.save()

        return redirect(table)
    data = {
        'user' : user
    }
    return render(req, 'update.html', data)