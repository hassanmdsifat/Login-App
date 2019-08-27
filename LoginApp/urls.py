from django.urls import path,include
from . import views
from rest_framework import routers
app_name="LoginApp"
router=routers.DefaultRouter()
urlpatterns = [
    path('',views.index,name="index"),
    path('login/',views.login,name="login"),
    path('register/',views.register,name='register'),
    path('dashboard/',views.dashboard,name="dashboard"),
    path('logout/',views.logout,name='logout'),
    path('addcustomer/',views.addcustomer,name='addcustomer'),
    path('showcustomerlist/',views.showAllCustomer,name='showcustomerlist'),
    path('delete/<int:c_id>/',views.deletecustomer,name='deletecustomer'),
    path('edit/<int:c_id>/',views.editcustomer,name='editcustomer'),
    path('addorder/',views.addorder,name="addorder"),
    path('showorderlist/',views.allorder,name="showorderlist"),
    path('deleteorder/<int:o_id>/',views.deleteorder,name='deleteorder'),
    path('api/customerapi/',views.customerAPI.as_view()),
    path('api/orderapi/',views.orderAPI.as_view()),
    path('api/customerapi/<int:pk>/',views.customerdetailAPI.as_view())
    #path('getapi/',views.get_api_list),
]
