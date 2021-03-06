from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from accountapp.views import AccountCreateView, AccountDetailView, AccountUpdateView, AccountDeleteView

app_name = 'accountapp' #주소를 일일이 쓰기 힘드기 때문에 설정

# 127.0.0.1:800/accounts/hellow_world/ =

urlpatterns = [
    # path('login/', LoginView.as_view(templates_name='accountapp/login.html'),
    #      name='login'),
    path('login/',LoginView.as_view(template_name='accountapp/login.html'),name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    # name 설정도 주소를 일일이 쓰기 힘드기 때문에 설정
    path('create/', AccountCreateView.as_view(), name='create'),
    path('detail/<int:pk>', AccountDetailView.as_view(), name='detail'),
    path('update/<int:pk>', AccountUpdateView.as_view(), name='update'),   ## pk - 프라이머리 키 -> 숫자로 되어있다
    path('delete/<int:pk>', AccountDeleteView.as_view(), name='delete'),
]