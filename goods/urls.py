from django.urls import path
from goods import views

urlpatterns = [
    path("",views.GoodsHome.as_view(), name='home'),
    path("card-page/<slug:gd_slug>/",views.CardPage.as_view(),name='card-page'),
    path("category/<slug:cat_slug>",views.GoodsCategory.as_view(), name='cat'),
    path('tag/<slug:tag_slug>/', views.GoodsTags.as_view(), name='tag'),
    path('add-prod/', views.AddProd.as_view(), name='add-prod'),
    path('about/', views.about, name='about'),
    path('delete-prod/<slug:slug>', views.DeletePage.as_view(), name='delete-prod'),
    path('login/', views.login, name='login'),

]