from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('', index, name='home'),
    # path('main/', main, name='home'),
    # path('add_BB', add_BB, name='add_BB'),
    path('add_BB',views.add_bb_view.as_view(), name='add_BB'),
    path('<int:pk>', views.qr_code_detect.as_view()),
    path('<int:pk>/post-json/', post_json),
    path('scan_qr',scan_qr_create_view, name='scan_qr'),

    path('login/',views.loginPage, name='login'),
    path('logout/',views.logoutUser, name='logout'),
]