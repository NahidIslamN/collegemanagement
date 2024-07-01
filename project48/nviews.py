# from django.shortcuts import render,redirect
# from neerapp.models import*
# from django.contrib.auth.decorators import login_required
# from django.contrib import messages

from django.shortcuts import render,redirect
from neerapp.models import*
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .decorators import *



# write your view here...


# purlic Fucntion # purlic Fucntion # purlic Fucntion # purlic Fucntion # purlic Fucntion # purlic Fucntion # purlic Fucntion # purlic Fucntion



def neerpage_of_tpi(request):
    index_slider = neer_page_caroules.objects.all()
    principal = administrations.objects.get(id ="1")

    dis = principal.Discription[0:728]
    DipHead = Head_Of_Dep.objects.all()

    Current_news = Block_Post_of_tip.objects.all().order_by("-Created_at")[0:2]


    total_member = CustomUser.objects.all().count()
    total_student = Student.objects.all().count()
    total_sub = Subjects.objects.all().count()
   
    cp = {
        "index_slider":index_slider,
        "principal":principal,
        "dis":dis,
        "DipHead":DipHead,
        "Current_news":Current_news,
        "total_member":total_member,
        "total_student":total_student,
        "total_sub":total_sub,
    }
    return render(request,"neer/neer_home.html", context=cp)



def learn_more_principal(request):
    principal = administrations.objects.get(id ="1")
    dis = principal.Discription[0:728]     
   
    cp = {
        "principal":principal,
        "dis":dis,
    }

    return render(request,"neer/learn_more.html",context=cp)


def all_courses(request):

    courses = neerapp_coursess.objects.all()

    cp = {
        "courses":courses,
    }
    return render(request,"neer/courses.html",context=cp)



def learn_mor_about_course(request,id):

    CRS = neerapp_coursess.objects.get(id = id)

    cp={
        "CRS":CRS,
    }
    return render(request,"neer/learn_mor_about_course.html",context=cp)





def about_page(request):
    Vice_principal = viceprincipal.objects.get(id = "1")
    TPI = Thakurgaon_Polytechnic_Institute.objects.get(id = "1")
    Missions = Mission_of_TPI.objects.all()
    Vissions = Vission_of_TPI.objects.all()
    IMG_Student = Image_gallary.objects.filter(img_type="0")[0]
    IMG_Collage = Image_gallary.objects.filter(img_type="1")[0]

    cp={
        "Vice_principal" : Vice_principal,
        "TPI":TPI,
        "Missions":Missions,
        "Vissions":Vissions,
        "IMG_Student":IMG_Student,
        "IMG_Collage":IMG_Collage,
    }
    return render(request,"neer/about_page.html",context=cp)




def learn_more_about_vice(request):
    Vice_principal = viceprincipal.objects.get(id = "1")

    cp={
        "Vice_principal":Vice_principal,
    }
    return render(request,"neer/learn_more_about_vice.html",context=cp)

def learn_more_about_tpi(request):
    TPI = Thakurgaon_Polytechnic_Institute.objects.get(id = "1")
    
    cp = {
        "TPI":TPI,
    }
    return render(request,"neer/learn_more_about_tpi.html",context=cp)


def Images_gelary(request,type):
    if type == "0":
        Gallary_Images = Image_gallary.objects.filter(img_type="0" , aprove_status="1")
    elif type == "1":
        Gallary_Images = Image_gallary.objects.filter(img_type="1", aprove_status="1")
    else:
        pass
    cp={
      "Gallary_Images":Gallary_Images,  
    }

    return render(request,"neer/photo_gelary.html",context=cp)





@login_required(login_url="/user_login/")
def block_post(request):
    Principal = administrations.objects.get(id="1")
    vice_Princi = viceprincipal.objects.get(id = "1")
    BPS = Block_Post_of_tip.objects.filter(aprove_status = "1").order_by("-Created_at")
    CMTS = Comments_on_block_post.objects.all()
    REPS = reply_of_comments.objects.all()
    RCMTS = Block_Post_of_tip.objects.all().order_by("-Created_at")[0:5]

    ResentComme = Comments_on_block_post.objects.all().order_by("-created_at")[0:10]


    if request.method == "POST":
        data=request.POST
        Search = data.get("Search")
        BPS = BPS.filter(Post_Discription__icontains = Search)
        
    
    cp={
        "Principal":Principal,
        "vice_Princi":vice_Princi,
        "BPS":BPS,
        "CMTS":CMTS,
        "REPS":REPS,
        "ResentComme":ResentComme,
        "RCMTS":RCMTS,
 
    }
    return render(request,"neer/blog_post.html",context=cp)

@login_required(login_url="/user_login/")
def sent_comments(request):
    if request.method == "POST":
        data = request.POST
        user_id = data.get("CommentSender")
        Sent_by = CustomUser.objects.get(id = user_id)
        post_id  = data.get("POSTID")

        PID = Block_Post_of_tip.objects.get(id = post_id)
        PID.Total_comment = PID.Total_comment + 1
        PID.save()
        CommenstText = data.get("CommenstText")
        CCom = Comments_on_block_post.objects.create(
            post_id = PID,
            admin = Sent_by,
            comments_text = CommenstText,
        )
        CCom.save()
    return redirect(f"/learn_more_about_block/{post_id}/")

@login_required(login_url="/user_login/")
def sent_reply(request):
    if request.method == "POST":
        data = request.POST
        Rep_sender = data.get("CommentSender")
        CMTID = data.get("CMTID")

        CommenstText = data.get("CommenstText")

        RS = CustomUser.objects.get(id = Rep_sender)

        cmments_id = Comments_on_block_post.objects.get(id = CMTID)

        post_id = cmments_id.post_id.id
        PostC = Block_Post_of_tip.objects.get(id = post_id )
        PostC.Total_comment = PostC.Total_comment + 1
        PostC.save()

        Reply = reply_of_comments.objects.create(
            com_id = cmments_id,
            admin = RS,
            comments_text = CommenstText,
            )
        Reply.save()
     
    return redirect(f"/learn_more_about_block/{post_id}/")




def notice_of_tpi(request):


    notices = Notice_of_TPI.objects.filter(aproval_status = "1").order_by("-Create_at")

    cp={
        "notices":notices,
    }

    return render(request,"neer/notices.html",context=cp)



def learn_more_about_block(request,id):
    bp = Block_Post_of_tip.objects.get(id=id)
    CMTS = Comments_on_block_post.objects.all()
    REPS = reply_of_comments.objects.all()
    RCMTS = Block_Post_of_tip.objects.all().order_by("-Created_at")[0:5]

    ResentComme = Comments_on_block_post.objects.all().order_by("-created_at")[0:10]

        
    
    cp={
        "bp":bp,
        "CMTS":CMTS,
        "REPS":REPS,
        "ResentComme":ResentComme,
        "RCMTS":RCMTS,
 
    }
    


    return render(request,"neer/learn_more_block_post.html",context=cp)



def Contuct_with_us(request):
    Cinfo = Contuct_info.objects.get(id = "1")

    if request.method == "POST":
        data = request.POST
        name = data.get("name")
        email =data.get("email")
        subject = data.get("subject")
        message = data.get("message")

        Massage = Public_masseges.objects.create(
            Massages_sender_name = name,
            sender_email = email,
            messagess_subject = subject,
            messages_text = message,
        )
        Massage.save()

        messages.info(request,"Your message has been sent. Thank you!")
        

     
    cp = {
        "Cinfo":Cinfo,
    }
    return render(request,"neer/contucts.html",context=cp)






# Manager Functions Manager Functions Manager Functions Manager Functions Manager FunctionsManager FunctionsManager Functions Manager Functions Manager Functions


@login_required(login_url="/")
@specific_user_required(user_id=16)
def add_carosel_for_neer(request):
    if request.method == "POST":
        data = request.POST
        images = request.FILES.get("iamges")
        carousel = neer_page_caroules.objects.create(
            Slide_Title = data.get("Slide_Title"),
            Slide_discription = data.get("Slide_discription"),
            slide_image = images,

        )
        carousel.save()
        messages.info(request,"Carosel Created Successfully !")
        return redirect("/add_carosel_for_neer/")
    return render(request,"neermanager/add_carosel.html")

@login_required(login_url="/")
@specific_user_required(user_id=16)
def carousel_list(request):

    Carosels = neer_page_caroules.objects.all()




    cp = {
        "Carosels":Carosels
    }


    return render (request,"neermanager/carousel_list.html",context=cp)


@login_required(login_url="/")
@specific_user_required(user_id=16)
def edite_carosel_slide(request,id):
    Curosel = neer_page_caroules.objects.get(id = id)

    if request.method == "POST":
        data = request.POST
        images = request.FILES.get("iamges")
        Curosel.Slide_Title = data.get("Slide_Title")
        Curosel.Slide_discription = data.get("Slide_discription")
        if images:
            Curosel.slide_image = images
           
        Curosel.save()
        messages.info(request,"Updated Successfully !")


    cp = {
        "Curosel":Curosel   
    }
    return render(request,"neermanager/edite_carosel_slide.html",context=cp)

@login_required(login_url="/")
@specific_user_required(user_id=16)
def delete_carosel_slide(request,id):
    Curosel = neer_page_caroules.objects.get(id = id)
    Curosel.delete()


    return redirect("/carousel_list/")

@login_required(login_url="/")
@specific_user_required(user_id=16)
def neer_add_courses(request):
    Dep = Departments.objects.all()
    if request.method == "POST":
        data = request.POST
        images = request.FILES.get("Dep_Image")
        Dep_id = Departments.objects.get(id = data.get("dep_name"))
        if neerapp_coursess.objects.filter(dep_name=Dep_id).exists():
            messages.info(request,"This Department Already Exists!")
            return redirect("/neer_add_courses/")
        else:
            Crses = neerapp_coursess.objects.create(
                Dep_Image = images,
                dep_name = Dep_id,
                dep_description = data.get("dep_description"),
            )
            Crses.save()
            messages.info(request,"Department for Student successfully Created !")
            return redirect("/neer_add_courses/")
    cp = {
        "Dep":Dep
    }
    return render(request,"neermanager/neer_add_courses.html",context=cp)

@login_required(login_url="/")
@specific_user_required(user_id=16)
def neer_app_course_list(request):
    NCourses = neerapp_coursess.objects.all()


    cp={
        "NCourses":NCourses,
    }
    return render(request,"neermanager/neer_app_course_list.html",context=cp)


@login_required(login_url="/")
@specific_user_required(user_id=16)
def neer_course_edite(request,id):
    NCrs = neerapp_coursess.objects.get(id = id)
    if request.method == "POST":
        data = request.POST
        Images = request.FILES.get("Dep_Image")
        NCrs.dep_description = data.get("dep_description")
        if Images:
            NCrs.Dep_Image = Images
        NCrs.save()
        messages.info(request,"Courses Updated Successfully !")
        return redirect(f"/neer_course_edite/{id}/")

    cp={
        "NCrs":NCrs,
    }
    return render (request,"neermanager/neer_course_edite.html",context=cp)

@login_required(login_url="/")
@specific_user_required(user_id=16)
def update_collage_informations(request):
    TPI = Thakurgaon_Polytechnic_Institute.objects.get(id = "1")

    if request.method == "POST":
        data = request.POST
        Images = request.FILES.get("Collage_Image")
        TPI.Collge_Discrition = data.get("Collge_Discrition")
        if Images:
            TPI.Collage_Image = Images
        else:
            pass
        TPI.save()
        messages.info(request,"Update Collages Informations Successfully !")
        return redirect("/update_collage_informations/")

    cp = {
        "TPI":TPI,
    }
    return render(request,"neermanager/update_collage_informations.html",context=cp)




@login_required(login_url="/")
@specific_user_required(user_id=16)
def add_mission(request):
    if request.method == "POST":
        data = request.POST
        miss = Mission_of_TPI.objects.create(
            Mission_text = data.get("Mission_text")
        )
        miss.save()
        messages.info(request,"Mission Created Successfully !")
        return redirect("/add_mission/")


    return render(request,"neermanager/add_mission.html")


@login_required(login_url="/")
@specific_user_required(user_id=16)
def add_vission(request):
    if request.method == "POST":
        data = request.POST
        miss = Vission_of_TPI.objects.create(
            Vission_text = data.get("Mission_text")
        )
        miss.save()
        messages.info(request,"Vission Created Successfully !")
        return redirect("/add_vission/")


    return render(request,"neermanager/add_vission.html")

@login_required(login_url="/")
@specific_user_required(user_id=16)
def mission_list_or_vission_list(request,type):
    if type == "0":
        MissNs = Mission_of_TPI.objects.all()
        cp = {
            "MissNs":MissNs
        }
        return render(request,"neermanager/mission_list.html",context=cp)
    elif type == "1":
        Vissions = Vission_of_TPI.objects.all()
        cp={
            "Vissions":Vissions,
        }
        return render(request,"neermanager/vission_list.html",context=cp)
    else:
        pass



@login_required(login_url="/")
@specific_user_required(user_id=16)
def update_mission(request,id):
    Miss = Mission_of_TPI.objects.get(id = id)
    if request.method == "POST":
        data  = request.POST
        Miss.Mission_text = data.get("Mission_text")
        Miss.save()
        messages.info(request,"Update Successfully !")
        return redirect(f"/update_mission/{id}/")
    
    cp={
        "Miss":Miss,
    }
    return render(request,"neermanager/update_mission.html",context=cp)


@login_required(login_url="/")
@specific_user_required(user_id=16)
def update_vission(request,id):
    Miss = Vission_of_TPI.objects.get(id = id)
    if request.method == "POST":
        data  = request.POST
        Miss.Vission_text = data.get("Mission_text")
        Miss.save()
        messages.info(request,"Update Successfully !")
        return redirect(f"/update_vission/{id}/")
    
    cp={
        "Miss":Miss,
    }
    return render(request,"neermanager/update_vission.html",context=cp)



@login_required(login_url="/")
@specific_user_required(user_id=16)
def update_mission(request,id):
    Miss = Mission_of_TPI.objects.get(id = id)
    if request.method == "POST":
        data  = request.POST
        Miss.Mission_text = data.get("Mission_text")
        Miss.save()
        messages.info(request,"Update Successfully !")
        return redirect(f"/update_mission/{id}/")
    
    cp={
        "Miss":Miss,
    }
    return render(request,"neermanager/update_mission.html",context=cp)


@login_required(login_url="/")
@specific_user_required(user_id=16)
def update_vission(request,id):
    Miss = Vission_of_TPI.objects.get(id = id)
    if request.method == "POST":
        data  = request.POST
        Miss.Vission_text = data.get("Mission_text")
        Miss.save()
        messages.info(request,"Update Successfully !")
        return redirect(f"/update_vission/{id}/")
    
    cp={
        "Miss":Miss,
    }
    return render(request,"neermanager/update_vission.html",context=cp)

@login_required(login_url="/")
@specific_user_required(user_id=16)
def delete_mission(request,id):
    Miss = Mission_of_TPI.objects.get(id = id)
    Miss.delete()

    return redirect("/mission_list_or_vission_list/0/")


@login_required(login_url="/")
@specific_user_required(user_id=16)
def delete_vission(request,id):
    Miss = Vission_of_TPI.objects.get(id = id)
    Miss.delete()
    
    return redirect("/mission_list_or_vission_list/1/")


@login_required(login_url="/")
@specific_user_required(user_id=16)
def none_aproval_photos(request):
    Listess = Image_gallary.objects.filter(aprove_status = "0")

    cp = {
        "Listess":Listess,
    }
    return render(request,"neermanager/none_aproval_photos.html",context=cp)

@login_required(login_url="/")
@specific_user_required(user_id=16)
def aprove_a_photo (request,id):
    Photo = Image_gallary.objects.get(id = id)
    Photo.aprove_status = "1"
    Photo.save()
    return redirect("/none_aproval_photos/")


@login_required(login_url="/")
@specific_user_required(user_id=16)
def delete_a_photo (request,id):
    Photo = Image_gallary.objects.get(id = id)
    Photo.delete()
    return redirect("/none_aproval_photos/")


@login_required(login_url="/")
@specific_user_required(user_id=16)
def add_photo_into_gelarry(request):
    if request.method == "POST":
        data = request.POST
        Images = request.FILES.get("iamges")
        IMG = Image_gallary.objects.create(
            Image_title = data.get("Image_title"),
            img_type = data.get("img_type"),
            Image = Images,
        )
        IMG.save()
        messages.info(request,"Image Uploded Successfully wait for Aproveal")

    return render(request,"neermanager/add_photo_into_gelarry.html")

@login_required(login_url="/")
def create_a_post(request,id):
    admin = CustomUser.objects.get(id = id)
    if request.method == "POST":
        Image = request.FILES.get("iamges")
        data = request.POST
        BP = Block_Post_of_tip.objects.create(
            Post_image = Image,
            Post_title = data.get("Image_title"),
            Post_Creator = admin,          
            Post_Discription = data.get("Mission_text"),
            
        )
        BP.save()
        messages.info(request,"Post Created Successfully wait for aproval")
    return render(request,"neermanager/create_a_post.html")

@login_required(login_url="/")
@specific_user_required(user_id=16)
def none_aproval_post(request):
    Naproval = Block_Post_of_tip.objects.filter(aprove_status = "0")


    cp = {
        "Naproval":Naproval
    }
    return render(request,"neermanager/none_aproval_post.html",context=cp)


@login_required(login_url="/")
@specific_user_required(user_id=16)
def aprove_a_post (request,id):
    Post = Block_Post_of_tip.objects.get(id = id)
    Post.aprove_status = "1"
    Post.save()
    return redirect("/none_aproval_post/")

@login_required(login_url="/")
def delete_a_post (request,id):
    Post = Block_Post_of_tip.objects.get(id = id)
    Post.delete()
    return redirect("/none_aproval_post/")


@login_required(login_url="/")
def update_a_post (request,id):
    Post = Block_Post_of_tip.objects.get(id = id)
    if request.method == "POST":
        data = request.POST
        images = request.FILES.get("iamges")
        Post.Post_title = data.get("Post_title")
        Post.Post_Discription = data.get("Post_Discription")
        if images:
            Post.Post_image = images
        Post.save()
        messages.info(request,"Post Update Successfully !")



    cp = {
        "Post":Post
    }    
    return render(request, "neermanager/update_a_post.html", context=cp)




@login_required(login_url="/")
def my_posts(request,id):
    admin = CustomUser.objects.get(id = id)
    Naproval = Block_Post_of_tip.objects.filter(Post_Creator = admin)



    cp = {
        "Naproval":Naproval,
    }
    return render(request,"neermanager/my_posts.html" ,context=cp)

@login_required(login_url="/")
@specific_user_required(user_id=16)
def update_contuct_info(request):
    Cinfo = Contuct_info.objects.get(id = "1")
    if request.method == "POST":
        data = request.POST
        Cinfo.Address = data.get("Address")
        Cinfo.tip_email_1 = data.get("tip_email_1")
        Cinfo.tip_email_2 = data.get("tip_email_2")
        Cinfo.tip_phone_1 = data.get("tip_phone_1")
        Cinfo.tip_phone_2 = data.get("tip_phone_2")


        Cinfo.save()
        messages.info(request,"Updated Successfully")



    cp={
        "Cinfo":Cinfo,
    }
    return render(request,"neermanager/update_contuct_info.html", context=cp)


@login_required(login_url="/")
@specific_user_required(user_id=16)
def public_messages (request):
    Pmass = Public_masseges.objects.all().order_by("-Create_at")
    
    cp = {
        "Pmass":Pmass
    }
    return render(request,"neermanager/public_messages.html",context=cp)



@login_required(login_url="/")
def create_a_notices_for_user_and_other(request,id):
    notice_ceator = CustomUser.objects.get(id = id)
    if notice_ceator.user_type == "2" or notice_ceator.user_type == "1" or notice_ceator.user_type == "5":
        if request.method == "POST":
            data = request.POST
            Notice_file = request.FILES.get("Notice_file")
            final_notice_ceator = CustomUser.objects.get(id = data.get("NoticeCreatorId"))
            Expair_date = data.get("Expair")
            

            Notice_obj = Notice_of_TPI.objects.create(
                admin = final_notice_ceator,
                Notice_file = Notice_file,
                Expird_date = Expair_date,
            )
        
            Notice_obj.save()
            messages.info(request,"Notice Created Successfully !")
            return redirect(f"/create_a_notices_for_user_and_other/{id}/")

    else:
        messages.info(request,"You are not Able to Create Notice !")
        return redirect(f"/create_a_notices_for_user_and_other/{id}/")
    

    return render(request,"neermanager/create_a_notices_for_user_and_other.html")



@login_required(login_url="/")
@specific_user_required(user_id=16)
def delete_a_notice(request,id):
    delet_notic_obje = Notice_of_TPI.objects.get(id = id)
    delet_notic_obje.delete()
    return redirect("/notice_of_tpi/")



