from django.urls import path
from.import views 
urlpatterns = [
    path('',views.helloworld,name="home"),
    path('about/',views.about,name="about"),
    path('login/',views.login_user , name="login"),
    path('logout/',views.logout_user,name="logout"),
    path('signup/',views.signup_user ,name="signup"),
    path('Product/<int:pk>',views.product,name="Product"),
    path('category/<str:cat>',views.Category,name="category"),
]



