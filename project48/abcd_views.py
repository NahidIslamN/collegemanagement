from django.shortcuts import render, redirect
from baseapp.models import *
from django.contrib import messages

# Create your views here.


def view_my_result(request):
    Sem_ids = Semester.objects.all()[0:8]
    if request.method == "POST":
        data = request.POST
        Student_IDs = data.get("Student_ID")

        Semesters = data.get("Department")
        sem_id =Semester.objects.get(id = Semesters)

        try:
            Student_is_present = Student.objects.get(id = Student_IDs)
        except:
            Student_is_present = None
            messages.info(request,"Student is Not found !")
            return redirect("/view_my_result/")


        if Student_is_present is not None:
            mark_is_present = None
            try:
                mark_is_present = Student_mark.objects.filter(Student_ID=Student_is_present, Semesters_id=sem_id)[0]
            except IndexError:
                # Handle the case where the queryset is empty
                messages.info(request,"Result not added yet!")
                return redirect("/view_my_result/")
                

            
            # mark_is_present = Student_mark.objects.filter(Student_ID = Student_is_present ,Semesters_id = sem_id)[0]
            if mark_is_present is not None:
                if mark_is_present.publised_status == "1":
                    return redirect(f"/result_sheet/{Student_IDs}/{Semesters}/")
                else:
                    messages.info(request,"Mark is not Published yet !")
            else:
                messages.info(request,"Result not added yet !")
                return redirect("/view_my_result/")

      


    cp = {
        "Sem_ids":Sem_ids
    }
    return render(request,"student/view_my_result.html",context=cp)
