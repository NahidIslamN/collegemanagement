from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from baseapp.models import *
from neerapp.models import *
import requests
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.hashers import check_password

from django.db.models import Q

# Create your views here.

@login_required(login_url="/")
def user_home_page(request):

    user_count = CustomUser.objects.all().count()

    student_count = Student.objects.filter(aproval_status="1").count()

    dep_count = Departments.objects.all().count()

    graduate_students = Student.objects.filter(student_disable_or_not = "1").count()

    techar_count = Teacher.objects.all().count()

    studetn_gender_female = Student.objects.filter(Gender = "Female", aproval_status="1").count()
    studetn_gender_male = Student.objects.filter(Gender = "Male" , aproval_status="1").count()
    # For Principal For Principal For Principal For Principal
    
    hod = Head_Of_Dep.objects.all().count()
    hod_persentice =round(((hod*100)/user_count),2) 
    Student_persentice =round(((student_count*100)/user_count),2) 
    Teacher_persentice =round(((techar_count*100)/user_count),2) 

    Sessions = Session.objects.all()

    female_student_count_data = []
    male_student_count_data = []

    for x in Sessions:
        session_student_male_count = Student.objects.filter(Session = x , Gender = "Male", aproval_status="1").count()
        male_student_count_data.append(session_student_male_count)

        session_student_female_count = Student.objects.filter(Session=x, Gender="Female",aproval_status="1").count()
        female_student_count_data.append(session_student_female_count)



    semester_sutdentcount = []
    Semesters = Semester.objects.all()[0:8]
    for i in Semesters:
        student_counder_sem = Student.objects.filter(Sem_id = i,aproval_status="1").count()
        semester_sutdentcount.append(student_counder_sem)


    # End end end end end enn home page user type 3 and 2 end of user homoepage
    
    total_post = Block_Post_of_tip.objects.all().count()

    mission = Mission_of_TPI.objects.all().count()
    vission = Vission_of_TPI.objects.all().count()
    total_mission = mission + vission

    pbulicmess = Public_masseges.objects.all().count()

    totalimage = Image_gallary.objects.all().count()

    Notices = Notice_of_TPI.objects.all().count()

    collageimg = Image_gallary.objects.filter(img_type = "1").count()
    Student_images = Image_gallary.objects.filter(img_type = "0").count()

   
        

    








    current_user = request.user
    unseenmessages = message_model_for_user.objects.filter(to_reciver = current_user, reciver_seen_status = "0" )
    unseenmessages_count = unseenmessages.count()

    cp = {
        "user_count":user_count,
        "student_count":student_count,
        "dep_count":dep_count,
        "graduate_students":graduate_students,
        "techar_count":techar_count,
        "studetn_gender_female":studetn_gender_female,
        "studetn_gender_male":studetn_gender_male,
        "hod_persentice":hod_persentice,
        "Student_persentice":Student_persentice,
        "Teacher_persentice":Teacher_persentice,
        "Sessions":Sessions,
       "female_student_count_data":female_student_count_data,
       "male_student_count_data": male_student_count_data,
       "semester_sutdentcount":semester_sutdentcount,
       "total_post":total_post,
       "total_mission":total_mission,
       "pbulicmess":pbulicmess,
       "totalimage":totalimage,
       "Notices":Notices,
       "collageimg":collageimg,
       "Student_images":Student_images,
       "unseenmessages_count":unseenmessages_count,
       "unseenmessages":unseenmessages,

    }
    return render(request,"home_pages.html",context=cp)

def user_login(request):  

    if request.method == "POST":
        data = request.POST
        username = data.get("Username")
        password = data.get("Passwords")
        if CustomUser.objects.filter(username=username).exists():            
            if authenticate(username = username,password = password):
                user = CustomUser.objects.get(username = username)
                login(request,user)
                return redirect ("/user_home_page/")
            else:
                messages.info(request,"Invailed Password")
                return redirect("/user_login/")
                
        else:
            messages.info(request,"Invaild Username")
            return redirect("/user_login/")               


    return render(request,"user_login.html")


def user_logut(request):
    logout(request)             


    return redirect("/")


@login_required(login_url="/")
def user_profile(request,username):
    
    user = CustomUser.objects.get(username = username)


    return render(request,"user_profile.html")

@login_required(login_url="/")
def user_profile_edite(request,username):
    user = CustomUser.objects.get(username = username)

    if request.method == "POST":
        data = request.POST
        data = request.POST
        Image = request.FILES.get("images")
        first_name = data.get("first_name")
        last_name = data.get("last_name")
       
        email = data.get("email")
        mobile = data.get("mobile")

        if Image:
            user.profile_pic = Image
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.mobile_number = mobile
        user.save()
        messages.info(request,"Profile Update Successfully")



    return render (request,"edite_user_profile.html")



def appy_to_become_a_sutdent(request,id):
    Dep = Departments.objects.get(id = id)
    SessDefault = Session.objects.all().order_by("-id")[0]
    Sessions = Session.objects.all().order_by("-id")
    Shifts = Shift.objects.all()
    data =  None

    action = request.GET.get("action")
    print(action)

    if request.method == "POST":
        data = request.POST
               

        Pass1 = data.get("Pass1")
        Pass2 = data.get("Pass2")
        username = data.get("username")
        email = data.get("email")
        Examination = data.get("Examination")

        if Pass1 != Pass2:
            messages.info(request,"Password Is Not Matched !")
        elif username != email:
            messages.info(request,"UserName is Not Matched !")
        elif CustomUser.objects.filter(username = username).exists():
            messages.info(request,"Your Email already taken !")
        elif Examination !="HSC" and Examination != "SSC" :
            messages.info(request,"Your Education Qualification is not Valid for this institute Ente SSC or HSC")
        

    cp = {
        "Dep":Dep,
        "SessDefault":SessDefault,
        "Sessions":Sessions,
        "Shifts":Shifts,
        "data":data,
        "action":action,
    }
    return render(request,"student_application_from.html",cp)



def save_student_info(request):
    if request.method == "POST":
        data = request.POST
        Image = request.FILES.get("images")

        Pass1 = data.get("Pass1")
        Pass2 = data.get("Pass2")
        username = data.get("username")
        email = data.get("email")
        Examination = data.get("Examination")
        dep_id = data.get("departments")
        Dep = Departments.objects.get(id = dep_id)

        Sessions = data.get("Session")
        sess_id = Session.objects.get(id=Sessions)

        Shifts = data.get("Shift")
        shift_id = Shift.objects.get(id = Shifts)       
        

    
# Error Handeling Part ... Error Handaling Part
        
        if Pass1 != Pass2:
            messages.info(request,"Password Is Not Matched !")
            return redirect(f"/appy_to_become_a_sutdent/{dep_id}/")

        elif username != email:

            messages.info(request,"UserName is Not Matched !")
            return redirect(f"/appy_to_become_a_sutdent/{dep_id}/")

        elif CustomUser.objects.filter(username = username).exists():
            messages.info(request,"User Name Already Exist !")
            return redirect(f"/appy_to_become_a_sutdent/{dep_id}/")
        
        elif Examination !="HSC" and Examination != "SSC" :
            messages.info(request,"Your Education Qualification is not Valid for this institute Ente SSC or HSC")
            return redirect(f"/appy_to_become_a_sutdent/{dep_id}/")
        
        # End Error Handeling Part



        # Create Database Part

        if Examination == "SSC":            
            group_a = Group.objects.get(id = "1")
            group_b = Group.objects.get(id = "2")
            if Student.objects.filter(group_id = group_a).count() < 50 :
                Group_ID = group_a

            else:
                Group_ID = group_b

            Sem_id = Semester.objects.get(id = "1")
            try:
                subject_Group = subject_group_for_student.objects.filter(Sem_id=Sem_id, Dep_ID=dep_id)[0]
            except IndexError:
                messages.info(request, "No subject group found for this semester and department.")
                return redirect(f"/appy_to_become_a_sutdent/{dep_id}/")
            except ObjectDoesNotExist:
                messages.info(request, "Subject group does not exist.")
                return redirect(f"/appy_to_become_a_sutdent/{dep_id}/")
            



        elif Examination == "HSC":
            group_a = Group.objects.get(id = "1")
            group_b = Group.objects.get(id = "2")
            if Student.objects.filter(group_id = group_a).count() < 50 :               
                Group_ID = group_a
                print("Group A")
            else:
                Group_ID = group_b
                print("Group B")

            Sem_id = Semester.objects.get(id = "3")
            try:
                subject_Group = subject_group_for_student.objects.filter(Sem_id=Sem_id, Dep_ID=dep_id)[0]
            except IndexError:
                messages.info(request, "No subject group found for this semester and department.")
                return redirect(f"/appy_to_become_a_sutdent/{dep_id}/")
            except ObjectDoesNotExist:
                messages.info(request, "Subject group does not exist.")
                return redirect(f"/appy_to_become_a_sutdent/{dep_id}/")
            

        user = CustomUser.objects.create(
            first_name = data.get("first_name"),
            last_name = data.get("last_name"),
            username = username,
            email = email,
            mobile_number = data.get("Mobile_phone"),
            user_type = "0",
            profile_pic = Image,
        )
        user.set_password(Pass1)



        stud = Student.objects.create(
            admin = user,
            Gender = data.get("Gender"),
            date_of_birth = data.get("date_of_birth"),
            religion = data.get("Religion"),

            Session = sess_id,
            Dep_id = Dep,
            shift_id = shift_id,
            Sem_id = Sem_id,
            group_id = Group_ID,
            Subjects_id = subject_Group,

            #parents Informations
            father_name = data.get("father_name"),
            father_ocupation = data.get("father_ocupation"),
            father_mobile = data.get("father_mobile"),
            father_email = data.get("father_email"),

            mother_name = data.get("mother_name"),
            mother_ocupation = data.get("mother_ocupation"),
            mother_mobile = data.get("mother_mobile"),
            mother_email = data.get("mother_email"),

            present_address = data.get("present_address"),
            permenent_address = data.get("permenent_address"),


            Examination = data.get("Examination"),
            examr_roll = data.get("examr_roll"),  
            exam_year = data.get("exam_year"),
            Examresult = data.get("Examresult"),
        )
        user.save()
        stud.save()

        messages.info(request,"Your Application Successfully Submited !")

    return redirect(f"/appy_to_become_a_sutdent/{dep_id}/")







# Apply for leave Apply for leave Apply for leave Apply for leave Apply for leave Apply for leave Apply for leave 

def apply_for_leave(request,id):
    admin = CustomUser.objects.get(id = id)
    if request.method == "POST":
        data = request.POST
        Message = data.get("Message")
        leavestart = data.get("leavestart")
        leaveend = data.get("leaveend")
        Leave_obj = Apply_for_leave.objects.create(
            admin = admin,
            Leave_start = leavestart,
            Leave_end = leaveend,
            message  = Message,
        )
        Leave_obj.save()
        messages.info(request, "Application Submited Successfully !")

    

    cp = {
        "admin":admin
    }
    return render (request,"alluser/apply_for_leave.html", context=cp)



def View_apply_for_leave_applications(request):
    Application = Apply_for_leave.objects.filter(status = "0").order_by("-createdat")    

    cp = {
        "Application":Application
    }
    return render (request,"alluser/View_apply_for_leave_applications.html", context=cp)


def aprove_a_applications(request,id,user_id):
    admin = CustomUser.objects.get(id = user_id)
    Application = Apply_for_leave.objects.get(id = id)
    Application.status = "1"
    Application.aproved_by = admin
    Application.save()

    return redirect("/View_apply_for_leave_applications")


def denied_a_applications(request,id,user_id):
    admin = CustomUser.objects.get(id = user_id)
    Application = Apply_for_leave.objects.get(id = id)
    Application.status = "3"
    Application.aproved_by = admin
    Application.save()

    return redirect("/View_apply_for_leave_applications")




def view_aproved_application(request):
    Application = Apply_for_leave.objects.filter(status = "1").order_by("-createdat")    

    cp = {
        "Application":Application
    }
    return render (request,"alluser/View_apply_for_leave_applications.html", context=cp)

def My_leaving_applications(request, id):
    admin = CustomUser.objects.get(id = id)
    Application = Apply_for_leave.objects.filter(admin = admin).order_by("-createdat")


    cp = {
        "Application":Application,
    }
    return render (request, "alluser/My_leaving_applications.html",context=cp)


# Change User Password Chage User Password Changet User PassOrld

def change_password(request):
    User = None
   
    if request.method == "POST":
        data = request.POST
        print(data)
        User = CustomUser.objects.get(id = data.get("User"))
        


        Old_pass = data.get("Old_pass")
        New_pass = data.get("New_pass")
        New_pass2 = data.get("New_pass2")

        is_password_correct = check_password(Old_pass, User.password)
        if is_password_correct == True :
            if New_pass == New_pass2:
                User.set_password(New_pass2)
                User.save()            
                messages.info(request,"Successfully Change Your Password !")
                return render(request,"been/alart1.html")
            else:
                messages.info(request,"Password Is Not Mached !")
                return render(request,"been/alart1.html")
        else:
            messages.info(request,"Enter the Right Password as a Oldpassword !")
            return render(request,"been/alart1.html")

    return render(request,"been/alart1.html")





# alart to for alrting
def view_alr2 (request):
    
    return render(request,"been/alart2.html")





def sent_massege_to_user(request, user_id):
    
    try:
        admins = CustomUser.objects.get(id=user_id)
        message_set = message_model_for_user.objects.filter(to_reciver=admins ).order_by("-create_at")
        unique_senders = set(message.from_sender for message in message_set)

        unique_queryset = [
            message_model_for_user.objects.filter(to_reciver=admins, from_sender=sender).order_by("-create_at").first()
            for sender in unique_senders
        ]
        
        cp = {
            "unique_queryset": unique_queryset
        }
        return render(request, "alluser/messenger.html", context=cp)
    
    except CustomUser.DoesNotExist:

        return render(request, "alluser/messenger.html")
    


def message_sent_and_get(request,user_id,sender_id):
    messages = None
     
    # admins = CustomUser.objects.get(id=user_id)
    # message_set = message_model_for_user.objects.filter(to_reciver=admins ).order_by("-create_at")
    # unique_senders = set(message.from_sender for message in message_set)

    # unique_queryset = [
    #     message_model_for_user.objects.filter(to_reciver=admins, from_sender=sender).order_by("-create_at").first()
    #     for sender in unique_senders
    # ]
        
    # cp = {
        
    #     "unique_queryset": unique_queryset
    # }
    sender = CustomUser.objects.get(id = sender_id)
    
    messages = message_model_for_user.objects.filter(
        Q(from_sender_id=sender_id, to_reciver_id=user_id) |
        Q(from_sender_id=user_id, to_reciver_id=sender_id)
    ).order_by('create_at')



    if request.method == "POST":
        data = request.POST

        Sender_id = data.get("Sender_id")
        sent_by = CustomUser.objects.get(id = Sender_id)

        received_by = data.get("received_by")
        recive_by = CustomUser.objects.get(id = received_by )

        message = data.get("message")

        message_obj = message_model_for_user.objects.create(
            from_sender = sent_by,
            to_reciver = recive_by,
            message_text = message,
     
        )

        message_obj.save()
        return redirect(f"/message_sent_and_get/{Sender_id}/{received_by}/")




   




    
    cp={
        "messages":messages,
        "sender":sender,
    }

    return render(request,"alluser/message_sent_and_get.html",context=cp)




def clear_all_notification(request):
    current_user = request.user
    unseenmessages = message_model_for_user.objects.filter(to_reciver = current_user, reciver_seen_status = "0" )
    for y in unseenmessages:
        y.reciver_seen_status = "1"
        y.save()

    return redirect("/user_home_page/")

