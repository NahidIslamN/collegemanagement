from django.db import models
from baseapp.models import *
from django.utils import timezone


# Create your models here.

class neer_page_caroules(models.Model):
    Slide_Title = models.CharField(max_length = 25)
    Slide_discription = models.TextField()
    slide_image = models.ImageField(upload_to="neer_slider")

class administrations(models.Model):
    BasicInfo = models.ForeignKey(CustomUser,on_delete=models.SET_NULL,null = True, blank = True)
    Discription = models.TextField()

class viceprincipal(models.Model):
    BasicInfo = models.ForeignKey(CustomUser,on_delete=models.SET_NULL,null = True, blank = True)
    Discription = models.TextField()



class neerapp_coursess(models.Model):
    Dep_Image = models.ImageField(upload_to="course_image")
    dep_name = models.ForeignKey(Departments, on_delete=models.SET_NULL,null = True, blank = True)
    dep_description = models.TextField()
    disable_status = models.CharField(max_length = 1,default = "0")

class Thakurgaon_Polytechnic_Institute(models.Model):
    Collage_Name = models.CharField(max_length = 50)
    Collage_Image = models.ImageField(upload_to="collage_images")
    Collge_Discrition = models.TextField()
    def __str__(self):
        return self.Collage_Name
    

class Mission_of_TPI(models.Model):
    Mission_text = models.TextField()

class Vission_of_TPI(models.Model):
    Vission_text = models.TextField()

class Image_gallary(models.Model):
    Image_title = models.CharField(max_length = 50)
    img_type = models.CharField(max_length = 1)
    Image = models.ImageField(upload_to="images_gallary")
    aprove_status = models.CharField(max_length = 1,default = "0")


class Block_Post_of_tip(models.Model):
    Post_image = models.ImageField(upload_to="block_post_images")
    Post_title = models.CharField(max_length = 50)
    Post_Creator = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    Created_at = models.DateTimeField(default=timezone.now)
    Update_at = models.DateTimeField(auto_now = True)
    Total_comment = models.IntegerField(default=0)
    Post_Discription = models.TextField()
    aprove_status = models.CharField(max_length = 1,default = "0")

class Comments_on_block_post(models.Model):
    post_id = models.ForeignKey(Block_Post_of_tip,on_delete = models.CASCADE)
    admin = models.ForeignKey(CustomUser, on_delete = models.CASCADE)
    comments_text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

class reply_of_comments (models.Model):
    com_id = models.ForeignKey(Comments_on_block_post,on_delete = models.CASCADE)
    admin = models.ForeignKey(CustomUser, on_delete = models.CASCADE)
    comments_text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)


class Notice_of_TPI (models.Model):
    admin = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    Notice_file = models.FileField(upload_to="notices")
    Create_at = models.DateTimeField(default = timezone.now)
    Expird_date = models.DateField()
    aproval_status = models.CharField(max_length = 1, default = "1")




class Public_masseges(models.Model):
    Massages_sender_name = models.CharField(max_length = 50)
    sender_email = models.EmailField()
    messagess_subject = models.CharField(max_length = 150)
    messages_text = models.TextField()
    sent_at = models.DateTimeField(default = timezone.now)
    Create_at = models.DateTimeField(default = timezone.now)



class Contuct_info(models.Model):
    Address = models.TextField()
    tip_email_1 = models.EmailField()
    tip_email_2 = models.EmailField()
    tip_phone_1 = models.CharField(max_length = 20)
    tip_phone_2 = models.CharField(max_length = 20)
    Create_at = models.DateTimeField(default = timezone.now)



class footer_link(models.Model):
    link_name = models.CharField(max_length=15)
    link_url = models.TextField()
    def __str__(self):
        return self.link_name








    


    