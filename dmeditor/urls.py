from django.urls import path

from . import views

app_name = 'dmeditor'
urlpatterns = [
    path('', views.index, name='index'),
    path('allyeditor/', views.allyEditor, name='allyedit'),
    path('itemeditor/', views.itemEditor, name='itemedit'),
    path('submitAlly/', views.submitAlly, name='submitally'),
    path('submitItem/', views.submitItem, name='submititem'),
    #path('<int:question_id>/results/', views.results, name='results'),
    #path('<int:question_id>/vote/', views.vote, name='vote'),
]
