from django.shortcuts import render,redirect
from django.http import HttpResponse
from baseapp.models import *
from django.contrib import messages
from datetime import datetime
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="/")
def take_addtedance(request,id):
    admins = CustomUser.objects.get(id = id)
    Dep_id = None
    Sub_ids = None
    Semesters = Semester.objects.all()
    Groups = Group.objects.all()
    Shift_id =Shift.objects.all()
    Stud_TPI = None
    data = None



    Semesters_ids = None
    group_id = None
    shift_id = None
    sub_id = None
    

    # Get Department and subjects
    if admins.user_type == "3":
        Teachers = Teacher.objects.get(admin = admins)
        Dep_id = Teachers.Dep_id
        Sub_ids = Subjects.objects.filter(Dep_ID = Dep_id)
    elif admins.user_type == "2":
        Dep_head = Head_Of_Dep.objects.get(admin = admins)
        Dep_id = Dep_head.Dep_id
        Sub_ids = Subjects.objects.filter(Dep_ID = Dep_id)
    else:
        messages.info(request,"Not able to take attendance")
    # Get Department and Subjects
    
    action = None
    if request.method == "POST":
        data = request.POST
        action = request.GET.get("action")
      
        Semesters_id = data.get("Semester")
        Semesters_ids = Semester.objects.get(id = Semesters_id)

        Groups_id = data.get("Group")
        group_id = Group.objects.get(id = Groups_id)

        Subject_id = data.get("Subject")
        sub_id = Subjects.objects.get(id = Subject_id)

        Shifts = data.get("Shift")
        shift_id = Shift.objects.get(id = Shifts)

        subject_instances = subject_group_for_student.objects.filter(Dep_ID = Dep_id, Sem_id = Semesters_ids)[0]
        sub_group = subject_instances.Subjects_groups.all()
        if sub_id in sub_group:
            Stud_TPI = Student.objects.filter(Dep_id = Dep_id, shift_id = shift_id, Sem_id = Semesters_ids, group_id = group_id)
        else:
            messages.info(request,f"{sub_id} is not a Subject of {Semesters_ids} Semester Student !")
            return redirect (f"/take_addtedance/{id}/")
        

     
        
        



        
        

    cp = {
        "Dep_id":Dep_id,
        "Semesters":Semesters,
        "Groups":Groups,
        "Sub_ids":Sub_ids,
        "action":action,
        "Shift_id":Shift_id,
        "Stud_TPI":Stud_TPI,
        "data":data,
        "Semesters_ids":Semesters_ids,
        "group_id":group_id,
        "shift_id":shift_id,
        "sub_id":sub_id,
        "admins":admins,

    }
    return render(request,"techer/take_addtedance.html",context=cp)


@login_required(login_url="/")
def save_attendence_information (request):
    admin_id = None
    if request.method == "POST":
        data = request.POST
        admin_id = data.get("Creator")
        admins = CustomUser.objects.get(id = admin_id)

        date = data.get("date")
        Dep_id = None

        if admins.user_type == "3":
            Teachers = Teacher.objects.get(admin = admins)
            Dep_id = Teachers.Dep_id

        elif admins.user_type == "2":
            Dep_head = Head_Of_Dep.objects.get(admin = admins)
            Dep_id = Dep_head.Dep_id



        Semesters = Semester.objects.get(id = data.get("Semester"))
        Groups = Group.objects.get(id = data.get("Group"))
        Shifts = Shift.objects.get(id = data.get("Shift"))
        Subject = Subjects.objects.get(id = data.get("Subject"))
        Students = data.getlist("Students")
        

   

        if AttendanceObject.objects.filter(date = date, department = Dep_id , sem_id = Semesters , group = Groups, subjects = Subject, Shift_id = Shifts ).exists():
            messages.info(request,"Attendence Already Taken !")
            return redirect(f"/take_addtedance/{admin_id}/")
        else:
            ATT = AttendanceObject.objects.create(
                taken_by = admins,
                date = date,
                department = Dep_id,
                sem_id = Semesters,
                group = Groups,   
                subjects = Subject,
                Shift_id = Shifts,
                
            )
            ATT.students.set(Students)
        
            ATT.save()
            messages.info(request,"Attandance Created Successfully !")
            return redirect(f"/take_addtedance/{admin_id}/")
        

    return redirect(f"/take_addtedance/{admin_id}/")


@login_required(login_url="/")
def view_attendence(request,id):
    admins = CustomUser.objects.get(id = id)
    
    Semesters = Semester.objects.all()
    Groups = Group.objects.all()
    Shift_id =Shift.objects.all()
    Subject = Subjects.objects.all()
    Dep = Departments.objects.all()


    action = None
    Semesters_ids = None
    group_id = None
    shift_id = None
    sub_id = None
    date = None
    Dep_ids = None

    Present_Student = None



    
    if request.method == "POST":

        data = request.POST
        action = request.GET.get("action")

        Dep_ids = Departments.objects.get(id = data.get("Department"))
        Semesters_ids = Semester.objects.get(id = data.get("Semester") )
        group_id = Group.objects.get(id = data.get("Group"))
        shift_id = Shift.objects.get(id = data.get("Shift"))
        sub_id = Subjects.objects.get(id = data.get("Subject"))
        date = data.get("date")

        if AttendanceObject.objects.filter(date = date , department = Dep_ids , sem_id = Semesters_ids , group = group_id , subjects = sub_id, Shift_id = shift_id ).exists():
            Present_Sheet = AttendanceObject.objects.filter(date = date , department = Dep_ids , sem_id = Semesters_ids , group = group_id , subjects = sub_id, Shift_id = shift_id )[0]

            Present_Student = Present_Sheet.students.all()
         
        
        else:
            messages.info(request, "Attendence Not Created")


        

    cp = {
        "Dep":Dep,
        "Semesters":Semesters,
        "Groups":Groups,
        "Shift_id":Shift_id,
        "Subject":Subject,
        "action":action,
        "admins":admins,
        "Semesters_ids":Semesters_ids,
        "group_id":group_id,
        "shift_id":shift_id,
        "sub_id":sub_id,
        "date":date,
        "Dep_ids":Dep_ids,
        "Present_Student":Present_Student,
    }
    return render(request, "techer/view_attendence.html", context=cp)



@login_required(login_url="/")
def add_mark_for_sudent(request,id):
    user = CustomUser.objects.get(id = id)

    Dep_id = None
    action = None
    data = None
    Semesters_ids = None
    group_id = None
    shift_id = None
    sub_id = None
    Studentsss = None


    if user.user_type == "3":
        Hod = Teacher.objects.get(admin = user)
        Dep_id = Hod.Dep_id
             
    else:
        messages.info(request, "You Are Not Able to Add mark")
    #Add mark Add mark Add mark Add mark
        



    Semesters = Semester.objects.all()
    Groups = Group.objects.all()
    Shift_id = Shift.objects.all()
    SubjectSSS = Subjects.objects.all()
    

    if request.method == "POST":
        data = request.POST
        Semesters_ids = Semester.objects.get(id = data.get("Semester"))
        group_id = Group.objects.get(id = data.get("Group"))
        shift_id = Shift.objects.get(id = data.get("Shift"))
        sub_id = Subjects.objects.get(id = data.get("Subject"))

        Studentsss = Student.objects.filter( Dep_id = Dep_id, Sem_id = Semesters_ids, shift_id = shift_id, group_id=group_id, aproval_status = "1")

        # 'Semester': ['1'], 'Group': ['1'], 'Shift': ['2'], 'Subject': ['18']}>

        action = request.GET.get("action")


    

        


    cp = {
        "Semesters":Semesters,
        "Groups":Groups,
        "Shift_id":Shift_id,
        "SubjectSSS":SubjectSSS,
        "action":action,
        "data":data,
        "Semesters_ids":Semesters_ids,
        "group_id":group_id,
        "shift_id":shift_id,
        "sub_id":sub_id,
        "user":user,
        "Studentsss":Studentsss,
    }
    return render(request,"techer/add_mark_for_sudent.html",context=cp)


@login_required(login_url="/")
def save_marks_info(request,id):
    Adder = CustomUser.objects.get(id = id)
    TCR = None
    if Adder.user_type == "3":
        TCR = Teacher.objects.get(admin  = Adder)
    else:
        messages.info(request,"You Are Not Able to Add mark")
        return render(request,"been/alart1.html")
    
    TCT_Subjects = TCR.Sub_id.all()

   

    if request.method == "POST":
        data = request.POST

        Sem_id = data.get("Semester")
        Sem = Semester.objects.get(id = Sem_id)        

        Sub_id = data.get("Subject")
        Sub  =Subjects.objects.get(id = Sub_id)        

        Stu_id = data.get("Student")
        Stude = Student.objects.get(id = Stu_id)
        Student_DEP = Stude.Dep_id
        StudSem_ID = Stude.Sem_id
        Subjects_Group = subject_group_for_student.objects.filter(Dep_ID = Student_DEP , Sem_id = StudSem_ID)[0]
        SG = Subjects_Group.Subjects_groups.all()
        
        TC_Mark = data.get("TC_Mark")
        PC_Mark = data.get("PC_Mark")

        if Sub not in TCT_Subjects:
            messages.info(request,"You Are Not Able to Add mark !")
            return render(request,"been/alart1.html")
            
        elif Student_mark.objects.filter(Student_ID = Stude,Subject_id = Sub ,Semesters_id = Sem ).exists():
            messages.info(request,"Already Aded Student Marks !")
            return render(request,"been/alart1.html")
        
        elif Sub in SG :
            S_Result = Student_mark.objects.create(
                Student_ID = Stude,
                Subject_id = Sub,
                Semesters_id = Sem,
                TC_Mark = TC_Mark,
                PC_Mark = PC_Mark,
                
            )
           
            S_Result.save()            
            messages.info(request,"Mark Aded SuccessFully !")
            return render(request,"been/alart1.html")

        else:
            messages.info(request,"This Subject Is not For the Student That you Select")
            return render(request,"been/alart1.html")


        
    

    return render(request,"been/alart1.html")



