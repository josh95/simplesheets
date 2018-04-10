from django.urls import path

from . import views

app_name = 'sheets'
urlpatterns = [
    path('', views.index, name='index'),
    path('sheeteditor/', views.sheetEditor, name='sheetedit'),
    path('sheetMain/', views.sheetMain, name='sheetmain'),
    path('checkUser/', views.checkUser, name='checkuser'),
    path('saveChanges/', views.saveChanges, name='savechanges'),
    path('getLevels/', views.getLevels, name='getlevels'),
    path('getAllyDeets/', views.getAllyDeets, name='getallydeets'),
    path('getItemDeets/', views.getItemDeets, name='getitemdeets'),
    path('deleteSheet/', views.deleteSheet, name='deletesheet'),
    #path('<int:question_id>/results/', views.results, name='results'),
    #path('<int:question_id>/vote/', views.vote, name='vote'),
]
