"""
URL configuration for project48 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import a__views,ab_views,abc_views,abcd_views,views,nviews




urlpatterns = [
    path('admin/', admin.site.urls),
    path("user_home_page/",views.user_home_page,name="user_home_page"),

    path("",nviews.neerpage_of_tpi,name="neerpage_of_tpi"),
    path("learn_more_principal/",nviews.learn_more_principal,name="learn_more_principal"),    
    path("all_courses/",nviews.all_courses, name="all_courses"),
    path("learn_mor_about_course/<id>/",nviews.learn_mor_about_course,name="learn_mor_about_course"),
    path("about_page/",nviews.about_page,name="about_page"),
    path("learn_more_about_vice/",nviews.learn_more_about_vice,name="learn_more_about_vice"),
    path("learn_more_about_tpi/",nviews.learn_more_about_tpi,name="learn_more_about_tpi"),
    path("Images_gelary/<type>/",nviews.Images_gelary,name="Images_gelary"),
    path("block_post/",nviews.block_post,name="block_post"),
    path("sent_commentss/",nviews.sent_comments,name = "sent_commentss"),
    path("sent_replyss/",nviews.sent_reply,name="sent_replyss"),
    path("notice_of_tpi/",nviews.notice_of_tpi,name = "notice_of_tpi"),
    path("learn_more_about_block/<id>/",nviews.learn_more_about_block,name="learn_more_about_block"),
    path("Contuct_with_us/",nviews.Contuct_with_us,name="Contuct_with_us"),
    

    # Neer Manager
    path("add_carosel_for_neer/",nviews.add_carosel_for_neer,name = "add_carosel_for_neer"),
    path("carousel_list/",nviews.carousel_list,name="carousel_list"),
    path("edite_carosel_slide/<id>/",nviews.edite_carosel_slide,name="edite_carosel_slide"),
    path("delete_carosel_slide/<id>/",nviews.delete_carosel_slide,name="delete_carosel_slide"),
    path("neer_add_courses/",nviews.neer_add_courses,name="neer_add_courses"),
    path("neer_app_course_list/",nviews.neer_app_course_list,name="neer_app_course_list"),
    path("neer_course_edite/<id>/",nviews.neer_course_edite,name="neer_course_edite"),
    path("update_collage_informations/",nviews.update_collage_informations,name = "update_collage_informations"),
    path("add_mission/",nviews.add_mission,name="add_mission"),
    path("add_vission/",nviews.add_vission,name="add_vission"),
    path("update_mission/<id>/",nviews.update_mission, name="update_mission"),
    path("update_vission/<id>/",nviews.update_vission,name="update_vission"),
    path("delete_mission/<id>/",nviews.delete_mission,name="delete_mission"),
    path("delete_vission/<id>/",nviews.delete_vission,name="delete_vission"),
    path("mission_list_or_vission_list/<type>/", nviews.mission_list_or_vission_list, name="mission_list_or_vission_list"),
    path("none_aproval_photos/",nviews.none_aproval_photos,name="none_aproval_photos"),
    path("aprove_a_photo/<id>/",nviews.aprove_a_photo, name = "aprove_a_photo"),
    path("delete_a_photo/<id>/",nviews.delete_a_photo, name = "delete_a_photo"),
    path("add_photo_into_gelarry/",nviews.add_photo_into_gelarry,name="add_photo_into_gelarry"),
    path("create_a_post/<id>/",nviews.create_a_post,name="create_a_post"),
    path("none_aproval_post/",nviews.none_aproval_post,name="none_aproval_post"),
    path("aprove_a_post/<id>/",nviews.aprove_a_post, name = "aprove_a_post"),
    path("update_a_post/<id>/",nviews.update_a_post, name = "update_a_post"),
    path("delete_a_post/<id>/",nviews.delete_a_post, name = "delete_a_post"),
    path("my_posts/<id>/",nviews.my_posts, name="my_posts"),
    path("update_contuct_info/", nviews.update_contuct_info, name="update_contuct_info"),
    path("public_messages/", nviews.public_messages, name="public_messages"),
    path("create_a_notices_for_user_and_other/<id>/",nviews.create_a_notices_for_user_and_other, name="create_a_notices_for_user_and_other"),
    path("delete_a_notice/<id>/", nviews.delete_a_notice, name="delete_a_notice"),







    path("user_login/",views.user_login,name = "user_login"),
    path("user_logout/",views.user_logut, name = "user_logout"),
    path("user_profile/<str:username>/",views.user_profile,name="user_profile"),
    path("change_password/",views.change_password, name = "change_password"),
    path("user_profile_edite/<str:username>/",views.user_profile_edite,name="user_profile_edite"),
    path("appy_to_become_a_sutdent/<id>/",views.appy_to_become_a_sutdent,name = "appy_to_become_a_sutdent"),
    path("save_student_info/",views.save_student_info,name="save_student_info"),
  

    # principal view urls
    path("add_department_head/<str:username>/",a__views.add_department_head,name="add_department_heads"),
    path("add_department_by_principal/",a__views.add_department_by_principal,name="add_department_by_principal"),
    path("department_list/",a__views.department_list,name="department_list"),
    path("edite_department/<id>/",a__views.edite_department,name="edite_department"),
    path("delete_department/<id>/",a__views.delete_department,name="delete_department"),
    path("show_dep_head/<id>/",a__views.show_dep_head,name="show_dep_head"),
    path("list_of_dephead/",a__views.list_of_dephead,name = "list_of_dephead"),
    path("update_head_of_department/<id>/",a__views.update_head_of_department,name="update_head_of_department"),
    path("delete_head_of_department/<id>/",a__views.delete_head_of_department,name="delete_head_of_department"),
    path("subject_list/<id>/",a__views.subject_list,name="subject_list"),
    path("add_subject/<id>/",a__views.add_subject,name="add_subject"),
    path("edite_subject/<id>/",a__views.edite_subject,name="edite_subject"),
    path("delete_subjects/<id>/",a__views.delete_subjects, name="delete_subjects"),
    path("not_aproval_teacher_list/",a__views.not_aproval_teacher_list,name="not_aproval_teacher_list"),
    path("aprove_a_techer/<id>/",a__views.aprove_a_techer,name="aprove_a_techer"),
    path("create_a_session/",a__views.create_a_session, name = "create_a_session"),
    path("result_sheet/<student_id>/<semester_id>/" , a__views.result_sheet, name="result_sheet"),
    path("published_student/<id>/", a__views.published_student, name="published_student"),

    # head of the department
    path("add_teacher_by_Head_of_dep/<str:username>/",ab_views.add_teacher_by_Head_of_dep,name="add_teacher_by_Head_of_dep"),
    path("save_teacher/", ab_views.save_teacher_information, name="save_teacher"),
    path("Teacher_list/<id>/",ab_views.Teacher_list,name="Teacher_list"),
    path("edite_teacher_information/<id>/",ab_views.edite_teacher_information,name = "edite_teacher_information"),
    path("delete_teacher_information/<id>/<user_id>/",ab_views.delete_teacher_information,name="delete_teacher_information"),
    path("view_none_aproval_Student/<id>/", ab_views.view_none_aproval_Student, name = "view_none_aproval_Student"),
    path("aprove_a_studnet/<id>/<id2>/",ab_views.aprove_a_studnet, name="aprove_a_studnet"),
    path("get_student_list/<id>/",ab_views.get_student_list,name = "get_student_list"),
    path("Update_a_student_data/<id>/",ab_views.Update_a_student_data, name = "Update_a_student_data"),
    path("Delete_a_student_data/<id>/<userid>/",ab_views.Delete_a_student_data,name = "Delete_a_student_data"),
    path("enable_or_desible_a_student/<id>/<str:type>/<userid>/",ab_views.enable_or_desible_a_student,name="enable_or_desible_a_student"),
    
    
    #Teacher Views of TPIS
    path("take_addtedance/<id>/",abc_views.take_addtedance,name = "take_addtedance"),
    path("save_attendence_info/",abc_views.save_attendence_information,name = "save_attendence_info"),
    path("view_attendence/<id>/", abc_views.view_attendence, name = "view_attendence"),
    path("add_mark_for_sudent/<id>/", abc_views.add_mark_for_sudent, name="add_mark_for_sudent"),
    path("save_marks_info/<id>/", abc_views.save_marks_info, name="save_marks_info"),


    #AllUser Alluser All User
    path("apply_for_leave/<id>/", views.apply_for_leave,name = "apply_for_leave"),
    path("View_apply_for_leave_applications/", views.View_apply_for_leave_applications, name="View_apply_for_leave_applications"),
    path("aprove_a_applications/<id>/<user_id>/", views.aprove_a_applications, name= "aprove_a_applications"),
    path("denied_a_applications/<id>/<user_id>/", views.denied_a_applications, name= "denied_a_applications"),
    path("view_aproved_application/", views.view_aproved_application, name="view_aproved_application"),
    path("My_leaving_applications/<id>/", views.My_leaving_applications, name = "My_leaving_applications"),
    path("sent_massege_to_user/<user_id>/",views.sent_massege_to_user,name="sent_massege_to_user"),
    path("message_sent_and_get/<user_id>/<sender_id>/", views.message_sent_and_get, name="message_sent_and_get"),
    path("clearallmessnotifications/", views.clear_all_notification, name = "clear_all_notification"),



    path("view_alr2/",views.view_alr2, name = "view_alr2"),






    #Student work
    path("view_my_result/",abcd_views.view_my_result, name = "view_my_result"),
]

if settings.DEBUG:
       
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
