from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('',
        auth_views.LoginView.as_view(template_name='diary/login.html', redirect_authenticated_user=True),
        name='login'
    ),
    path('intern/companies/',
        views.InternListView.as_view(),
        name='intern_list'
    ),
    path('placement/companies/',
        views.PlacementListView.as_view(),
        name='placement_list'
    ),
    path('placement/companies/remarks/<int:pk>',
        views.RemarksListView.as_view(),
        name='remark_list'
    ),
    path('placement/companies/add_remark/',
        views.CreateRemarkView.as_view(),
        name='create_remark'
    ),
    path('logout/',
        auth_views.LogoutView.as_view(),
        name='logout'
    ),
    path('thanks/',
        views.ThanksPage.as_view(),
        name='thanks'
    ),
]
