"""Partner_Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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

from Partner_App  import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('employees/', views.EmployeeListView),

    path('employees/<int:pk>/detail/', views.EmployeeDetailView),

    path('employees/<int:pk>/delete/', views.EmployeeDeleteView),

    path('employees/create/', views.EmployeeCreateView),

    path('employees/<int:pk>/update/', views.EmployeeUpdateView),



    path('get_all_employees/', views.get_all_employees,
              name='employees'),

    path('get_employee_detail/<int:pk>/', views.get_single_object,
             name='employee_detail'),

    path('delete_employee/<int:pk>/', views.delete_object,
                name='employee_delete'),

    path('create_employee/', views.create_object,
                name='employee_create'),

    path('update_employee/<int:pk>/', views.update_object,
                 name='employee_update'),
]









