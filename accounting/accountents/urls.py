from django.urls import path
from . import views

# urls
urlpatterns = [
    path('',views.Accountents_HomePage_View.as_view(),name="accountents_home"),
    path('<int:pk>',views.Accountents_InfoPage_View.as_view(),name="accountents_info"),
    path('add/',views.Accountents_AddPage_View.as_view(),name="accountetns_add"),
    path('delete/<int:pk>',views.Accountents_DeletPage_View.as_view(),name="accountetns_delete"),
    path('edit/<int:pk>',views.Accountents_EditPage_View.as_view(),name="accountetns_edit"),
]
