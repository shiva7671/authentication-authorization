
from django.contrib import admin
from django.urls import path
from testapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.home_view),
    path("transactions/",views.transact_view),
    path("settlements/",views.settlement_view),
    path("account/",views.account_view),
    path("signup/",views.signup_view, name="signup"),
    path("signin/",views.signin_view, name="signin"),
    path("logout/",views.logout_view)
]
