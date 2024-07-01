from django.shortcuts import render,redirect
from baseapp.models import *
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

# # Create your views here.
@login_required(login_url="/")
def add_teacher_by_Head_of_dep(request,username):    
    data = None
    Department = Departments.objects.all()
    Shifts = Shift.objects.all()

    admins = CustomUser.objects.get(username = username)
    hod = Head_Of_Dep.objects.get(admin=admins)
    Dep_id = hod.Dep_id
    Sub = Subjects.objects.filter(Dep_ID = Dep_id )

    action = request.GET.get("action")
    if request.method == "POST":
        data = request.POST
    else:
        pass
    


    cp={
        "Department":Department,
        "Shifts":Shifts,
        "action":action,
        "data":data,
        "Sub":Sub,
        "Dep_id":Dep_id,
    }    
    return render (request,"dephead/add_teacher_by_principal.html",context=cp)


@login_required(login_url="/")
def save_teacher_information(request):
    if request.method == "POST":
        data = request.POST
        Image = request.FILES.get("Image")
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        username = data.get("username")
        email = data.get("email")
        Pass1 = data.get("Pass1")
        Pass2 = data.get("Pass2")
        Department = data.get("Department")
        Dep_id = Departments.objects.get(id = Department)
        Shifts = data.get("Shift")
        S_ID = Shift.objects.get(id = Shifts)
        Gender = data.get("Gender")
        JoinDate = data.get("JoinDate")
        date_of_birth = data.get("date_of_birth")
        mobile = data.get("mobile")
        qualifications = data.get("qualifications")
        exprience = data.get("exprience")
        Subjectss = data.getlist("Subjects")
        address = data.get("address")
        state = data.get("state")
        district = data.get("district")
        country = data.get("country")

        add_by = data.get("add_by")
        if CustomUser.objects.filter(username=username).exists():
            messages.info(request,"Teacher ID already Given Already Given!")
            return redirect(f"/add_teacher_by_Head_of_dep/{add_by}/")
        elif Pass1 != Pass2:
            messages.info(request,"Password is not Matched!")
            return redirect(f"/add_teacher_by_Head_of_dep/{add_by}/")
        else:
            Usr = CustomUser.objects.create(
                first_name = first_name,
                last_name = last_name,
                username = username,
                mobile_number = mobile,
                profile_pic = Image,
                email = email,
            )
            Usr.set_password(Pass1)

            TCR = Teacher.objects.create(
                admin = Usr,
                Dep_id = Dep_id,
                Shift_id = S_ID,
                Gender = Gender,    
                Join_date = JoinDate,  
                Date_of_Birth = date_of_birth,
                Mobile = mobile,    
                Qualification = qualifications,
                Exprience = exprience,
                Address = address,
                State = state,
                District = district,
                Country = country,
                principal_aproval = "0",
            )
            for x in Subjectss:
                Sub = Subjects.objects.get(id = x)
                TCR.Sub_id.add(Sub)
            Usr.save()
            TCR.save()
            messages.info(request,"Teacher Added Successfully !")
            return redirect(f"/add_teacher_by_Head_of_dep/{add_by}/")
    return redirect("/user_home_page/")



@login_required(login_url="/")
def Teacher_list(request,id):
    USR = CustomUser.objects.get(id = id)
    if USR.user_type == "1":
        TSRS = Teacher.objects.all()
        TSRS=TSRS.filter(principal_aproval = "1")
        TC = TSRS.count()
    elif USR.user_type == "2":
        USR = CustomUser.objects.get(id = id)
        HOD = Head_Of_Dep.objects.get(admin = USR)
        Dep = HOD.Dep_id
        TSRS = Teacher.objects.filter(Dep_id = Dep)
        TSRS=TSRS.filter(principal_aproval = "1")
        TC = TSRS.count()
    else:
        pass


    cp = {
        "TSRS":TSRS,
        "TC":TC,
    }
    
    return render(request,"dephead/Teacher_list.html",context=cp)


@login_required(login_url="/")
def edite_teacher_information(request,id):
    Shifts = Shift.objects.all()
    USR = CustomUser.objects.get(id = id)
    TSAR = Teacher.objects.get(admin = USR)
    Dep_id = TSAR.Dep_id
    if request.method == "POST":
        data = request.POST
        Image = request.FILES.get("Image")
        if Image:
            USR.profile_pic = Image
        else:
            pass

        first_name = data.get("first_name")
        USR.first_name = first_name

        last_name = data.get("last_name")
        USR.last_name = last_name
        
        username = data.get("username")
        USR.username = username

        email = data.get("email")
        USR.email = email

        mobile = data.get("mobile")
        USR.mobile_number = mobile


        TSAR.admin = USR

        TSAR.Mobile = mobile


        Shifts = data.get("Shift")
        if Shifts == "0":
            pass
        else:
            S_ID = Shift.objects.get(id = Shifts)
            TSAR.Shift_id = S_ID

        Gender = data.get("Gender")
        if Gender =="0":
            pass
        else:
            TSAR.Gender = Gender

        JoinDate = data.get("JoinDate")
        if JoinDate:
            TSAR.Join_date = JoinDate
        else:
            pass
        date_of_birth = data.get("date_of_birth")
        if date_of_birth:
            TSAR.Date_of_Birth = date_of_birth
        else:
            pass
        
        
        qualifications = data.get("qualifications")
        TSAR.Qualification = qualifications

        exprience = data.get("exprience")
        TSAR.Exprience = exprience

        address = data.get("address")
        TSAR.Address = address

        state = data.get("state")
        TSAR.State = state

        district = data.get("district")
        TSAR.District = district

        country = data.get("country")
        TSAR.Country = country

        add_by = data.get("add_by")
        USR.save()
        TSAR.save()
        messages.info(request,"Teacher Updated Successfully")
    cp = {
        "TSAR":TSAR,
        "Shifts":Shifts,
        "Dep_id":Dep_id
    }
    return render(request,"dephead/edite_teacher_information.html",context=cp)


@login_required(login_url="/")
def delete_teacher_information(request,id,user_id):
    
    USR = CustomUser.objects.get(id = id)
    TSAR = Teacher.objects.get(admin = USR)
    TSAR.delete()
    USR.delete()
   
    return redirect(f"/Teacher_list/{user_id}/")






# Students Part

@login_required(login_url="/")
def view_none_aproval_Student(request,id):
    user = CustomUser.objects.get(id = id)
    HOD  = Head_Of_Dep.objects.get(admin = user)
    Dep_id = HOD.Dep_id

    Students = Student.objects.filter(aproval_status = "0", Dep_id = Dep_id)
    None_aprovaled = Students.count()
    
    paginator = Paginator(Students,10)
    pagenumber = request.GET.get("page")
    Finaldata = paginator.get_page(pagenumber)
    last_page = Finaldata.paginator.num_pages

    cp = {
        "Students":Finaldata,
        "last_page":last_page,
        "totalpage_list":[n+1 for n in range(last_page)],
        "None_aprovaled":None_aprovaled,

    }
    return render (request,"dephead/view_none_aproval_Student.html",context=cp)

@login_required(login_url="/")
def aprove_a_studnet(request,id,id2):
    user = CustomUser.objects.get(id = id)
    Students = Student.objects.get(admin = user)
    user.user_type = "4"
    Students.aproval_status = "1"
    user.save()
    Students.save()

    return redirect(f"/view_none_aproval_Student/{id2}/")

def get_student_list (request,id):
    user = CustomUser.objects.get(id = id)
    Students = None
    TS = None
    if user.user_type == "1":
        Students = Student.objects.filter(aproval_status = "1", student_disable_or_not = "0")
        TS = Students.count()
        
    elif user.user_type == "2":
        Dep_head = Head_Of_Dep.objects.get(admin = user)
        dep_id = Dep_head.Dep_id
        Students = Student.objects.filter(Dep_id = dep_id, aproval_status = "1", student_disable_or_not = "0")
        TS = Students.count()
    elif user.user_type == "3":
        Teachers = Teacher.objects.get(admin = user)
        D_id = Teachers.Dep_id
        Students = Student.objects.filter(Dep_id = D_id, aproval_status = "1",student_disable_or_not = "0")
        TS = Students.count()








    paginator = Paginator(Students,5)
    pagenumber = request.GET.get("page")
    Finaldata = paginator.get_page(pagenumber)
    last_page = Finaldata.paginator.num_pages


    cp = {
        "Students":Finaldata,
        "TS":TS,
        "last_page":last_page,
        "totalpage_list":[n+1 for n in range(last_page)],
    }   


    return render(request,"dephead/students_list.html",context=cp)


@login_required(login_url="/")
def Update_a_student_data (request,id):
    admin = CustomUser.objects.get(id = id)
    data = Student.objects.get(admin = admin)
    if request.method == "POST":
        data2 = request.POST

        e1 = data2.get("username")
        e2 = data2.get("email")
        if e1 == e2:
            pass
        else:
            messages.info(request,"Emails are not Matched!")
            return redirect(f"/Update_a_student_data/{id}/")
        Images = request.FILES.get("images")
        if Images:
            admin.profile_pic = Images

        admin.first_name = data2.get("first_name")
        admin.last_name = data2.get("last_name")
        admin.username  = data2.get("username")
        admin.email = data2.get("email")
        admin.mobile_number = data2.get("Mobile_phone")

        data.admin = admin

        
        
        data.Gender = data2.get("Gender")

        dates = data2.get("date_of_birth")

        if dates:
            data.date_of_birth = data2.get("date_of_birth")
        else:
            pass
        data.religion = data2.get("Religion")


        #parents Informations
        data.father_name = data2.get("father_name")
        data.father_ocupation = data2.get("father_ocupation")
        data.father_mobile = data2.get("father_mobile")
        data.father_email = data2.get("father_email")

        data.mother_name = data2.get("mother_name")
        data.mother_ocupation = data2.get("mother_ocupation")
        data.mother_mobile = data2.get("mother_mobile")
        data.mother_email = data2.get("mother_email")

        data.present_address = data2.get("present_address")
        data.permenent_address = data2.get("permenent_address")
        admin.save()
        data.save()
        messages.info(request,"User Updated Successfully!")




        return redirect(f"/Update_a_student_data/{id}/")

    cp = {
        "data":data
    }
    return render(request,"dephead/Update_a_student_data.html",context=cp)
    


@login_required(login_url="/")
def Delete_a_student_data (request,id,userid):
    admin = CustomUser.objects.get(id = id)
    data = Student.objects.get(admin = admin)
    data.delete()
    admin.delete()

    return redirect(f"/get_student_list/{userid}/")

@login_required(login_url="/")
def enable_or_desible_a_student(request,id,type,userid):
    mainadmin = CustomUser.objects.get(id = userid)
    admin = CustomUser.objects.get(id = id)
    data = Student.objects.get(admin = admin)
    if mainadmin.user_type == "1":
        if type == "enable":
            admin.user_type = "4"
            data.admin = admin
            admin.save()
            data.save()

        elif type == "disable":
            admin.user_type = "0"
            data.admin = admin
            admin.save()
            data.save()
        else:
            pass
    
    return redirect(f"/get_student_list/{userid}/")

@login_required(login_url="/")
def view_neer_app_course(request):

    return render(request,"neermanager/view_neer_app_course.html")







    


