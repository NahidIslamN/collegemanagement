from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
import random
import string

# Create your models here.

class CustomUser(AbstractUser):
    USER = (
        (1,"Principal"),
        (2,"HOD"),
        (3,"Instractor"),
        (4,"STUDENT"),
        (5,"Neeer_Manager")
    )
    mobile_number = models.CharField(max_length=20)
    user_type = models.CharField(choices = USER,max_length=50)
    profile_pic = models.ImageField(upload_to="profile_picture")
    def __str__(self):
        return self.first_name



class Departments (models.Model):
    Dep_ID = models.CharField(max_length = 8) #TPID0001
    Dep_Name = models.CharField(max_length=50)
    def __str__(self):
        return self.Dep_Name



class Shift (models.Model):
    Shift_ID = models.CharField(max_length = 25)
    def __str__(self):
        return self.Shift_ID

    

class Session(models.Model):
    Session_Start = models.CharField(max_length = 25)
    Session_End = models.CharField(max_length = 25)
    def __str__(self):
        return self.Session_Start + " To " + self.Session_End



class Semester(models.Model):
    Semester = (
        ("1","First Semester"),
        ("2","Second Semester"),
        ("3","Third Semester"),
        ("4","Fourth Semester"),
        ("5","Fifth Semester"),
        ("6","Sixth Semester"),
        ("7","Seventh Semester"),
        ("8","Eighth Semester"),
        ("9","Nine Semester"),
    )
    Semester_ID = models.CharField(choices = Semester, max_length = 50)
    def __str__ (self):
        return self.Semester_ID


class Group(models.Model):
    Group_ID = models.CharField(max_length = 50)
    def __str__ (self):
        return self.Group_ID

    

class Subjects(models.Model):
    Sub_ID = models.CharField(max_length=8) #TPIS0001
    Subjects_Name = models.CharField(max_length = 50)
    Dep_ID =  models.ForeignKey(Departments, on_delete=models.SET_NULL,null = True, blank = True)
    Creadite = models.IntegerField(default= 2 ,null = True, blank = True)
    TC = models.IntegerField(default= 2, null = True, blank = True )
    PC = models.IntegerField(default= 0 ,null = True, blank = True)
    def __str__(self):
        return self.Subjects_Name

class Head_Of_Dep (models.Model):
    admin = models.OneToOneField(CustomUser, on_delete = models.SET_NULL, null=True,blank=True )
    Dep_id = models.ForeignKey(Departments, on_delete = models.SET_NULL, null=True,blank=True )
    Mobile = models.CharField(max_length=30)
    Gender = models.CharField(max_length=30)
    Date_of_Birth = models.DateField()
    Join_date = models.DateField()
    def __str__(self):
        return self.Dep_id.Dep_Name


class Teacher(models.Model):
    admin = models.OneToOneField(CustomUser, on_delete = models.SET_NULL, null=True,blank=True) #usertype must be filled
    Dep_id = models.ForeignKey(Departments, on_delete = models.SET_NULL, null=True,blank=True)
    Shift_id = models.ForeignKey(Shift,on_delete = models.SET_NULL, null = True, blank = True)
    Sub_id = models.ManyToManyField("Subjects",related_name="subject_of_teachers")
    Gender = models.CharField(max_length=30)    
    Join_date = models.DateField()   
    Date_of_Birth = models.DateField()
    Mobile = models.CharField(max_length=30)     
    Qualification =models.CharField(max_length = 50)
    Exprience = models.TextField()
    Address = models.TextField(max_length = 50)
    State = models.CharField(max_length = 50)
    District = models.CharField(max_length = 50)
    Country = models.CharField(max_length = 50)
    principal_aproval = models.CharField(max_length=1, default ="0")
    def __str__(self):
        return self.admin.first_name + " " + self.admin.last_name



class subject_group_for_student(models.Model):
    Dep_ID =  models.ForeignKey(Departments, on_delete=models.SET_NULL,null = True, blank = True)
    Sem_id = models.ForeignKey(Semester,on_delete=models.SET_NULL,null = True, blank = True)
    Subjects_groups = models.ManyToManyField(Subjects, related_name="Siubjects")
    def __str__(self):
        return f"{self.Dep_ID.Dep_Name} {self.Sem_id.id}"



class Student(models.Model):

    admin = models.OneToOneField(CustomUser, on_delete = models.SET_NULL, null=True,blank=True)
    Gender = models.CharField(max_length=30)
    date_of_birth = models.DateField()
    religion = models.CharField(max_length=30)



    Session = models.ForeignKey(Session,on_delete = models.SET_NULL, null = True, blank = True)
    Dep_id = models.ForeignKey(Departments,on_delete = models.SET_NULL, null = True, blank = True)
    shift_id = models.ForeignKey(Shift,on_delete = models.SET_NULL, null = True, blank = True)
    Sem_id = models.ForeignKey(Semester,on_delete = models.SET_NULL, null = True, blank = True)
    group_id = models.ForeignKey(Group,on_delete = models.SET_NULL, null = True, blank = True)
    Subjects_id = models.ForeignKey(subject_group_for_student,on_delete = models.CASCADE)

    #parents Informations
    father_name = models.CharField(max_length = 50)
    father_ocupation = models.CharField(max_length = 50)
    father_mobile = models.CharField(max_length = 15)
    father_email = models.EmailField(null = True , blank = True)

    mother_name = models.CharField(max_length = 50)
    mother_ocupation = models.CharField(max_length = 50)
    mother_mobile = models.CharField(max_length = 15)
    mother_email = models.EmailField(null = True , blank = True)

    present_address = models.TextField()
    permenent_address = models.TextField()


    Examination = models.CharField(max_length = 100)
    examr_roll = models.CharField(max_length=25)    
    exam_year = models.CharField(max_length = 4)
    Examresult = models.CharField(max_length = 5)

    aproval_status = models.CharField(max_length = 1,default="0")

    student_disable_or_not = models.CharField(default = "0", max_length = 1)

    def __str__(self):
        return self.admin.username + " " + self.admin.last_name
    




class AttendanceObject(models.Model):
    taken_by = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateField()
    department = models.ForeignKey(Departments, on_delete=models.SET_NULL, null=True, blank=True, related_name='department_attendance')
    sem_id = models.ForeignKey(Semester, on_delete=models.SET_NULL, null=True, blank=True)
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, blank=True, related_name='group_attendance')   
    subjects = models.ForeignKey(Subjects, on_delete=models.SET_NULL, null=True, blank=True)
    students = models.ManyToManyField(Student)
    Shift_id = models.ForeignKey(Shift, on_delete=models.SET_NULL, null=True, blank=True, related_name='shift_attendance')
    



class Apply_for_leave (models.Model):
    admin = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    Leave_start = models.DateField()
    Leave_end = models.DateField()
    message  = models.TextField()
    status = models.CharField(max_length = 1,default = "0")
    createdat = models.DateTimeField(default = timezone.now)
    updatedat = models.DateTimeField(auto_now = True)
    aproved_by = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True , related_name='aproved_byApply_for_leave' )
    def __str__(self):
        return self.admin.first_name
    


class Student_mark(models.Model):
    Student_ID = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True, blank=True, related_name='Student_mark')

    Subject_id = models.ForeignKey(Subjects, on_delete=models.SET_NULL, null=True, blank=True, related_name='Student_mark')

    Semesters_id = models.ForeignKey(Semester, on_delete=models.SET_NULL, null=True, blank=True, related_name='Student_mark')

    publised_status = models.CharField(default = "0", max_length = 1, null=True, blank=True)

    Credit = models.FloatField(default = 2, null=True, blank=True)

    TC_Mark = models.FloatField(default = 0.01, null=True, blank=True)
    PC_Mark = models.FloatField(default = 0.01, null=True, blank=True)

    Total_TCPC_Mark = models.FloatField(null=True, blank=True)
    Total_Mark_of_Subject = models.FloatField(null=True, blank=True)

    Persentice = models.FloatField(null=True, blank=True)

    Subjec_GPA = models.FloatField(null=True, blank=True)
    Subject_Grade = models.CharField(max_length = 5 , null=True, blank=True)
    Pass_or_Fail = models.CharField(max_length = 1 , default = "1" ,null=True, blank=True)



    Sem_Mark_helper = models.FloatField(null=True, blank=True)
    def __str__(self):
        return f"{self.Student_ID.id} {self.Student_ID.admin.username} {self.Subject_id.Subjects_Name}"



    def mark_manager (self):
        self.Credit = self.Subject_id.Creadite
        # self.Semesters_id = self.Student_ID.Sem_id
        self.Total_TCPC_Mark = float(self.TC_Mark) + float(self.PC_Mark)
        self.Total_Mark_of_Subject = float(self.Credit) * 50
        self.Persentice = (float(self.Total_TCPC_Mark) * 100) / (float(self.Total_Mark_of_Subject))
        if self.Persentice >= 80:
            self.Subjec_GPA = 4.00
            self.Subject_Grade = "A+"
        elif self.Persentice >= 75:
            self.Subjec_GPA = 3.75
            self.Subject_Grade = "A"
        elif self.Persentice >= 70:
            self.Subjec_GPA = 3.50
            self.Subject_Grade = "A-"
        elif self.Persentice >= 65:
            self.Subjec_GPA = 3.25
            self.Subject_Grade = "B+"
        elif self.Persentice >= 60:
            self.Subjec_GPA = 3.00
            self.Subject_Grade = "B"
        elif self.Persentice >= 55:
            self.Subjec_GPA = 2.75
            self.Subject_Grade = "B-"
        elif self.Persentice >= 50:
            self.Subjec_GPA = 2.50
            self.Subject_Grade = "C+"
        elif self.Persentice >= 45:
            self.Subjec_GPA = 2.25
            self.Subject_Grade = "C"
        elif self.Persentice >= 40:
            self.Subjec_GPA = 2.00
            self.Subject_Grade = "D"
        else:
            self.Subjec_GPA = 0.00
            self.Subject_Grade = "F"
            self.Pass_or_Fail = "0"
            
        self.Sem_Mark_helper = float(self.Subjec_GPA) * float(self.Credit
)

    def save(self, *args, **kwargs):
        self.mark_manager()
        super().save(*args, **kwargs)




class message_model_for_user(models.Model):
    from_sender = models.ForeignKey(CustomUser, on_delete = models.CASCADE, related_name ="message_model" )
    to_reciver = models.ForeignKey(CustomUser, on_delete = models.CASCADE, related_name ="message_model2")
    message_text = models.TextField()
    create_at = models.DateTimeField(default = timezone.now)
    update_at = models.DateTimeField(default = timezone.now,)
    sender_seen_status = models.CharField(max_length = 1, default = "1")
    reciver_seen_status = models.CharField(max_length = 1, default = "0")
    def __str__(self):
        return self.from_sender.first_name
    




class Main_Bank(models.Model):
    admin = models.OneToOneField(CustomUser, on_delete = models.CASCADE)
    bank_name = models.CharField(max_length=100)
    Security_key = models.CharField(max_length = 250)
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=0) 
    location = models.CharField(max_length=100)
    established_date = models.DateField(default=timezone.now)
    def __str__(self):
        return self.bank_name    

class SavingsAccount(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    account_number = models.CharField(max_length=10, unique=True)
    Security_key = models.CharField(max_length = 250)
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=0)    
    bank = models.ForeignKey(Main_Bank, on_delete=models.CASCADE)
    def acc_no_generator(self):
        return 'TPIBNK'.join(random.choices(string.digits, k=16))

    def save(self, *args, **kwargs):
        if not self.account_number:
            self.account_number = self.acc_no_generator()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Savings Account for {self.user.username} at {self.bank.bank_name}"

    

    






    

        
 



    