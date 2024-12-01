from django.contrib import admin
from django.urls import include, path
from pagina import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('pagina/', views.index, name='pagina'),
    path('pag/', views.pag, name='pag'),
    path('pag2/', views.pag2, name='pag2'),
    path('pag3/', views.pag3, name='pag3'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('database/', include('database.urls')), 
    path('chat-response/', views.chat_response, name='chat_response'), 
]
