
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('admin_login/',views.admin_login,name='admin_login'),
    path('admin_logout/',views.admin_logout,name='admin_logout'),
    path('add_emp/',views.add_emp,name='add_emp'),
    path('view_emp/',views.view_emp,name='view_emp'),
    
    path('update_emp/<int:id>/', views.update_emp, name='update_emp'),
    path('delete_emp1/<int:id>/',views.delete_emp1,name='delete_emp1'),
    path('update_records/<int:id>', views.update_records, name='update_records'),
   

    


]
