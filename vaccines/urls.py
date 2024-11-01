from django.urls import path
from .views import VaccinesDetail, VaccineUpdateView, VaccineDeleteView
from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path("sobre/", views.about, name="about"),
    
    # vacinas para marcar a acesso
    path("listar_vacinas/", views.list_vaccines, name='list-vaccines'),
    path("marcar_vacina/", views.formScheduledVacina, name='form-scheduled-vacina'),
    path("vacinas_agendadas/", views.vaccinesScheduled , name='scheduled_vaccine'),
    
    #calendário
    path("calendario/", views.calendar_vaccines, name='calendar-vaccines'),
    path("api/user-vaccines/", views.allevents, name='allevents'),
    
    # vacinas de administração do admin
    path("registro_vacina/", views.register_vaccine, name='register-vaccine'),
    path("Vacina_detalhe/<int:pk>", VaccinesDetail.as_view(), name='vaccine-detail'),
    path("Vacina_detalhe/<int:pk>/update", VaccineUpdateView.as_view(), name='vaccine-update'),
    path("Vacina_detalhe/<int:pk>/delete", VaccineDeleteView.as_view(), name='vaccine-delete'),

]
