from django.urls import path

from Libraryapp import views
0
urlpatterns = [
    path('', views.log_fun,name='log'),
    path('logdata', views.logdata_fun),

    path('admin_reg', views.admin_reg_fun,name='admin_reg'),
    path('regdata', views.regdata_fun),

    path('student_reg', views.student_reg_fun,name='student_reg'),
    path('sregdata', views.sregdata_fun),

    path('home', views.home_fun,name='home'),

    path('add_book',views.addbook_fun, name='add_book'),
    path('readdata',views.readdata_fun),

    path('display_book', views.displaybook_fun, name='display_book'),

    path('update/<int:id>', views.update_fun, name='up'),
    path('delete/<int:id>', views.delete_fun, name='del'),

    path('log_out', views.log_out_fun, name='log_out'),

    path('assign_book',views.assignbook_fun, name='assign_book'),
    path('areaddata', views.areaddata_fun),
    path('sreaddata',views.sreaddata_fun),

    path('issuebook',views.issuebook_fun,name='issue_book'),

    path('updt/<int:id>',views.updated_fun ,name='upd'),
    path('del/<int:id>', views.deleted_fun, name='dele'),

    path('issuedbook',views.issuedbook_fun,name='issued_book'),

    path('studenthome',views.studenthome_fun,name='student_home'),

    path('profile',views.profile_fun,name='profile'),

    path('urreaddata',views.update_profile_fun,name='update_profile'),
    path('ureaddata',views.ureaddata_fun)




]