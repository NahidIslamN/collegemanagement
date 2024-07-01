from django.shortcuts import render,redirect
from baseapp.models import*
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .decorators import specific_user_required


# Principal'pals Worlks.


@login_required(login_url="/")
@specific_user_required(user_id=2)
def add_department_head(request,username):
    user = CustomUser.objects.get(username = username)
    Dep = Departments.objects.all()
    if user.user_type == "1":
        if request.method == "POST":
            data = request.POST
            images = request.FILES.get("iamges")
            first_name = data.get("first_name")
            last_name = data.get("last_name")
            user_name = data.get("username")
            email = data.get("email")
            Pass1 = data.get("Pass1")
            Pass2 = data.get("Pass2")
            Department = data.get("Department")
            Dep_id = Departments.objects.get(id = Department )
            Gender = data.get("Gender")
            JoinDate = data.get("JoinDate")
            date_of_birth = data.get("date_of_birth")
            mobile = data.get("mobile")
            if Pass1 == Pass2:
                if CustomUser.objects.filter(username = user_name).exists():
                    messages.info(request,"username already exists !")
                    return redirect("/add_department_by_principal/")
                else:
                    users= CustomUser.objects.create(
                        first_name = first_name,
                        last_name = last_name,
                        username = user_name,
                        email = email,
                        user_type = "2",
                        is_staff = "1",
                        mobile_number = mobile,
                        profile_pic = images,                        
                    )
                    users.set_password(Pass1)
                    Hod = Head_Of_Dep.objects.create(
                        admin = users,
                        Dep_id = Dep_id,
                        Mobile = mobile,
                        Gender = Gender,
                        Date_of_Birth = date_of_birth,
                        Join_date = JoinDate
                    )
                    users.save()
                    Hod.save()
                    messages.info(request,f"Head of Department of {Dep_id} Created successfully")
                    return redirect(f"/add_department_head/{username}/")

            else:
                messages.info(request,"Passwords ar not Mecheing")
                return redirect("/add_department_by_principal/")
    else:
        messages.info(request,"You are not Principal !")
        return redirect("/user_logout/")


    cp = {
        "Dep":Dep,
    }
    return render(request,"principal/add_head_of_dep.html",context=cp)


def list_of_dephead(request):
    Dep_heads = Head_Of_Dep.objects.all()
    Departcount = Head_Of_Dep.objects.all().count()
    page_creator = Paginator(Dep_heads,6)
    pagenumber = request.GET.get("page")
    Finaldata = page_creator.get_page(pagenumber)
    last_page = Finaldata.paginator.num_pages


    cp = {
        "Dep_head_data":Finaldata,
        "Departcount":Departcount,
        "last_page":last_page,
        "totalpage_list":[n+1 for n in range(last_page)],
    }    
    return render(request,"principal/list_of_dephead.html",context=cp)



@login_required(login_url="/")
@specific_user_required(user_id=2)

def update_head_of_department(request,id):
    users = CustomUser.objects.get(id = id)
    Head_of_Deps = Head_Of_Dep.objects.get(admin = users)
    Dep = Departments.objects.all()

    if request.method == "POST":
        data = request.POST
        images = request.FILES.get("iamges")
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        email = data.get("email")
        Department = data.get("Department")
        Dep_id = None
        if Department:
            Dep_id = Departments.objects.get(id = Department )
        Gender = data.get("Gender")
        JoinDate = data.get("JoinDate")
        date_of_birth = data.get("date_of_birth")
        mobile = data.get("mobile")
        users.first_name = first_name
        if images:
            users.profile_pic = images
        users.last_name = last_name
        users.email = email
        users.mobile_number = mobile
        Head_of_Deps.admin=users
        if Dep_id:
            Head_of_Deps.Dep_id = Dep_id
        if Gender:
            Head_of_Deps.Gender = Gender
        
        if JoinDate:
            Head_of_Deps.Join_date = JoinDate
        if date_of_birth:
            Head_of_Deps.Date_of_Birth = date_of_birth
        messages.info(request,"update Department Head Successfully !")
        return redirect(f"/update_head_of_department/{id}/")


        
        
    
    cp = {
        "Head_of_Deps":Head_of_Deps,
        "Dep":Dep
    }
    return render(request,"principal/update_head_of_department.html",cp)




@login_required(login_url="/")
@specific_user_required(user_id=2)
def delete_head_of_department(request,id):
    users = CustomUser.objects.get(id = id)
    Head_of_Deps = Head_Of_Dep.objects.get(admin = users)
    Head_of_Deps.delete()
    users.delete()

    return redirect("/list_of_dephead/")

@login_required(login_url="/")
def add_subject(request,id):
    Dep = Departments.objects.all()
    Dep2 = None

    admin = CustomUser.objects.get(id = id)
    if admin.user_type == "2":
        Dep2 = Head_Of_Dep.objects.filter(admin = admin)[0]
    if request.method == "POST":
        data = request.POST     
        Sub_ID = data.get("Sub_ID")
        Subjects_Name = data.get("Subjects_Name")
        Department = data.get("Department")
        Depart = Departments.objects.get(id = Department)
        TC = data.get("TC")
        PC = data.get("PC")
        Credit = data.get("Credit")

        if len(Sub_ID) > 8:
            messages.info(request,"Subject Code is too Long !")
            return redirect(f"/add_subject/{id}/")
        elif Subjects.objects.filter(Sub_ID = Sub_ID).exists() or Subjects.objects.filter(Subjects_Name = Subjects_Name).exists() :
            messages.info(request,"Subject already Exist !")
            return redirect(f"/add_subject/{id}/")
        else:
           sub= Subjects.objects.create(
                Sub_ID = Sub_ID,
                Subjects_Name = Subjects_Name,
                Dep_ID = Depart,
                TC = TC,
                PC = PC,
                Creadite = Credit,

            )
           sub.save()
           messages.info(request,"Subject Create Successfully !")
           return redirect(f"/add_subject/{id}/")



            
    cp={
        "Dep":Dep,
        "Dep2":Dep2,
    }
    return render(request,"principal/add_subject.html",context=cp)




@login_required(login_url="/")
def subject_list(request,id):
    
    admin = CustomUser.objects.get(id = id)

    if admin.user_type == "1":
        subjects = Subjects.objects.all()
    elif admin.user_type == "2":
        Dep = Head_Of_Dep.objects.get(admin = admin)
        Deps = Dep.Dep_id
        subjects = Subjects.objects.filter(Dep_ID = Deps )

    if request.method == "POST":
        search_data = request.POST
        subjects = Subjects.objects.filter(Subjects_Name__icontains = search_data.get("search"))

    Subjectss = Subjects.objects.all().count()

    paginator = Paginator(subjects,10)
    pagenumber = request.GET.get("page")
    Finaldata = paginator.get_page(pagenumber)
    last_page = Finaldata.paginator.num_pages


    cp = {
        "subjects":Finaldata,
        "Subjectss":Subjectss,
        "last_page":last_page,
        "totalpage_list":[n+1 for n in range(last_page)]
    }

    return render(request,"principal/subjects.html",context=cp)


@login_required(login_url="/")
@specific_user_required(user_id=2)
def edite_subject(request,id):
    Sub = Subjects.objects.get(id = id)
    Dep = Departments.objects.all()

    if request.method == "POST":
        data = request.POST
        print(data)
        Departmentss = data.get("Department")       
        Sub.Sub_ID = data.get("Sub_ID")  
        Sub.Subjects_Name = data.get("Subjects_Name")
        Sub.save()
        Departmentss = data.get("Department")
        if Departmentss == "0":
            pass
        else:
            Department = Departments.objects.get(id = Departmentss)
            Sub.Dep_ID = Department
            Sub.save()
        
        TC_mark = data.get("TC")
        Sub.TC = TC_mark

        PC_mark = data.get("PC")
        Sub.PC = PC_mark

        CRD_mark = data.get("Credit")
        Sub.Creadite = CRD_mark
        Sub.save()

        messages.info(request,"Subject Update Successfully !")
        return redirect(f"/edite_subject/{id}/")

    cp={
        "Sub":Sub,
        "Dep":Dep,
    }
    return render(request,"principal/edite_subject.html",context=cp)



@login_required(login_url="/")
@specific_user_required(user_id=2)
def delete_subjects(request,id):

    Subjectss = Subjects.objects.get(id = id)
    Subjectss.delete()

    return redirect("/subject_list/")


@login_required(login_url="/")
def add_teacher_by_principal(request,username):    
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
@specific_user_required(user_id=2)
def add_department_by_principal(request):
    if request.method == 'POST':
        data = request.POST
        DepartmentID = data.get("DepartmentID")
        DepartmentName = data.get("DepartmentName")
        if len(DepartmentID) > 8:
            messages.info(request,"Pleace use the right text for department ID !")
            return redirect("/add_department_by_principal/")
        else:
            if Departments.objects.filter(Dep_ID = DepartmentID).exists() or Departments.objects.filter(Dep_Name = DepartmentName).exists() :
                messages.info(request,"Department already exists!")
                return redirect("/add_department_by_principal/")
            else:
                dep = Departments.objects.create(
                    Dep_ID = DepartmentID,
                    Dep_Name = DepartmentName
                )
                dep.save()
                messages.info(request,"Department Create Successfully!")
                return redirect("/add_department_by_principal/")           

    return render(request,"principal/add_department.html")




def department_list(request):
    Dep_data = Departments.objects.all()
    Departcount = Departments.objects.all().count()
    paginator = Paginator(Dep_data,6)
    pagenumber = request.GET.get("page")
    Finaldata = paginator.get_page(pagenumber)
    last_page = Finaldata.paginator.num_pages


    cp = {
        "Dep_data":Finaldata,
        "Departcount":Departcount,
        "last_page":last_page,
        "totalpage_list":[n+1 for n in range(last_page)]

    }
    return render(request,"principal/department_list.html",context=cp)


@login_required(login_url="/")
@specific_user_required(user_id=2)
def edite_department(request,id):
    dep = Departments.objects.get(id = id)
    if request.method == 'POST':
        data = request.POST
        DepartmentID = data.get("DepartmentID")
        DepartmentName = data.get("DepartmentName")
        if len(DepartmentID) > 8:
            messages.info(request,"Pleace use the right text for department ID !")
            return redirect(f"/edite_department/{id}/")
        else:
            dep.Dep_ID = DepartmentID
            dep.Dep_Name = DepartmentName
            dep.save()
            messages.info(request,"Successfully Updated department !")
            return redirect(f"/edite_department/{id}/") 
    cp = {
        "dep":dep
    }
    return render(request,"principal/edite_department.html",context=cp)

@login_required(login_url="/")
@specific_user_required(user_id=2)
def delete_department(request,id):
    dep = Departments.objects.get(id = id)
    dep.delete()
    return redirect("/department_list/")


@login_required(login_url="/")
@specific_user_required(user_id=2)
def show_dep_head(request,id):
    dep = Departments.objects.get(id = id)
    Headof_dep = None
    if Head_Of_Dep.objects.filter(Dep_id = dep).exists():
        Headof_dep = Head_Of_Dep.objects.filter(Dep_id = dep)[0]
    else:
        pass

    
    cp={
        "Headof_dep":Headof_dep,
    }
    return render (request,"principal/show_dephead.html",context=cp)

@login_required(login_url="/")
@specific_user_required(user_id=2)
def not_aproval_teacher_list(request):
    TSRS = Teacher.objects.filter(principal_aproval = "0")
    TC = TSRS.count()
    cp={
       "TSRS":TSRS,
       "TC":TC,
    }
    return render(request,"principal/not_aproval_teacher_list.html",context=cp)



@login_required(login_url="/")
@specific_user_required(user_id=2)
def aprove_a_techer(request,id):
    USR = CustomUser.objects.get(id = id)
   
    TSAR = Teacher.objects.get(admin_id = id)     
    USR.user_type = "3"
    USR.is_staff = "1"
    TSAR.admin = USR
    TSAR.principal_aproval = "1"
    USR.save()
    
    TSAR.save()

    return redirect("/not_aproval_teacher_list/")




def result_sheet(request,student_id,semester_id):
    Stude = Student.objects.get(id =student_id )
    Sem_id = Semester.objects.get(id = semester_id )
    Dep_id = Stude.Dep_id
    Subcount = subject_group_for_student.objects.filter(Dep_ID = Dep_id, Sem_id = Sem_id )[0].Subjects_groups.all().count()
    Results = Student_mark.objects.filter(Student_ID = Stude, Semesters_id = Sem_id)
    Res_count = Results.count()


    GPA = None

    Fcount = 0
    Credite_count = 0
    gpa_healper_count = 0

    for x in Results:
        Credite_count = Credite_count + float(x.Credit)
        gpa_healper_count = gpa_healper_count + float(x.Sem_Mark_helper)
        if x.Pass_or_Fail == "0":
            Fcount = Fcount + 1
        else:
            pass
    if gpa_healper_count == 0 :
        messages.info(request,"Result Not Added Yet")
        return render(request,"been/alart1.html")

    else:
        GPA = round((gpa_healper_count / Credite_count),2)


        

    



    cp = {
        "Stude":Stude,
        "Sem_id":Sem_id,
        "Subcount":Subcount,
        "Res_count":Res_count,
        "Results" : Results,
        "GPA":GPA,
        "Fcount":Fcount,

    }
    return render (request,"principal/result_sheet.html",context = cp)


@login_required(login_url="/")
@specific_user_required(user_id=2)
def published_student(request,id):
    admin = CustomUser.objects.get(id = id)

    Sem_IDs = None
    sem_marks = None
    Sem_id = None
    Fcount = 0
    student = None
    adminid = None
    student_curr_sem_id = None
    Dep_id = None

  
    if admin.user_type == "1":
        #Filtert Withvalid user now it is a bug
        Studentsss = Student.objects.filter(student_disable_or_not = "0")

        for Stu in Studentsss:
            student = Stu
            adminid = student.admin.id 
        
            
            Sem_id = student.Sem_id
            Dep_id = student.Dep_id
            Sem_IDs = student.Sem_id.id 
            
            student_curr_sem_id = Sem_IDs+1 
            sem_marks = Student_mark.objects.filter(Student_ID = Stu, Semesters_id = Sem_id )

            Sugfor_sutd  = subject_group_for_student.objects.filter(Sem_id = Sem_id, Dep_ID = Dep_id )[0].Subjects_groups.all().count()

           

            sem_marks_count = sem_marks.count()
            


            if sem_marks_count == Sugfor_sutd :
                
                for x in sem_marks:
                    if x.Pass_or_Fail == "1":
                        x.publised_status = "1"
                        x.save()
                        pass
                    else:
                        Fcount = Fcount + 1
                        x.publised_status = "1"
                        x.save()

                if Fcount>3:
                    pass
                    for y in sem_marks:
                        y.publised_status = "1"
                        y.save()
                else:
                    SemS = Semester.objects.get(id = student_curr_sem_id)
                    student.Sem_id = SemS
                    student.save()
                    if student.Sem_id.id == 9:
                        User = CustomUser.objects.get(id = adminid)
                        User.user_type = "0"
                        student.student_disable_or_not = "1"
                        student.admin = User
                        User.save()
                        student.save()        
                
            else:
                print("mark Not added yet")     

                    
                 
                        
                        


        messages.info(request,"Published Successfully !")
        return render(request,"been/alart1.html")  
   

    else:
        messages.info(request,"Only Principal Can Published result")
        return render(request,"been/alart1.html")
    


@login_required(login_url="/")
@specific_user_required(user_id=2)
def create_a_session(request):
    if request.method == "POST":
        data = request.POST

        Session_Satar = data.get("Session_Satar")
        Session_End = data.get("Session_End")
        Sess_obj = Session.objects.create(
           Session_Start = Session_Satar,
           Session_End = Session_End,

        )
        Sess_obj.save()
        messages.info(request,"Session Created Successfully !")
        return redirect("/create_a_session/")

     

    return render(request,"principal/create_a_session.html")