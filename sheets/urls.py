from django.urls import path

from . import views

app_name = 'sheets'
urlpatterns = [
    path('', views.index, name='index'),
    path('sheeteditor/', views.sheetEditor, name='sheetedit'),

    #path('<int:question_id>/results/', views.results, name='results'),
    #path('<int:question_id>/vote/', views.vote, name='vote'),
]
