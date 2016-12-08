from django.conf.urls import url

from . import views

urlpatterns = [
    url(r"^signup/$", views.signup, name="account_signup"),
    url(r"^login/$", views.login, name="account_login"),
    url(r"^logout/$", views.logout, name="account_logout"),

    url(r"^password/change/$", views.password_change,
        name="account_change_password"),
    url(r"^password/set/$", views.password_set, name="account_set_password"),

    url(r"^inactive/$", views.account_inactive, name="account_inactive"),

    # E-mail
    url(r"^email/$", views.email, name="account_email"),
    url(r"^confirm-email/$", views.email_verification_sent,
        name="account_email_verification_sent"),
    url(r"^confirm-email/(?P<key>[-:\w]+)/$", views.confirm_email,
        name="account_confirm_email"),

    # password reset
    url(r"^password/reset/$", views.password_reset,
        name="account_reset_password"),
    url(r"^password/reset/done/$", views.password_reset_done,
        name="account_reset_password_done"),
    url(r"^password/reset/key/(?P<uidb36>[0-9A-Za-z]+)-(?P<key>.+)/$",
        views.password_reset_from_key,
        name="account_reset_password_from_key"),
    url(r"^password/reset/key/done/$", views.password_reset_from_key_done,
        name="account_reset_password_from_key_done"),

    # profile
    url(r"^profile/$", views.profile, name="account_profile"),
    url(r"^profile/(?P<username>\w+)/$", views.profiles, name="otherprofiles"),
    url(r"^myHive/$", views.myHive, name="my_hive"),

    url(r'^settings/$', views.settings, name='settings'),
    url(r'^(?P<hive_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^delete_user/$', views.DeleteUser, name = 'delete'),
    url(r'^search/$', views.SearchUserbase, name = 'search'),
    url(r'^view_pdf/$', views.view_pdf, name = 'search'),


]
