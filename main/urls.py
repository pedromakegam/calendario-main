from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('', home_view, name='home'),
    path('api/save_event/', save_event, name='save_event'),
    path('api/get_events/', get_events, name='get_events'),
    path('api/delete_event/<int:event_id>/', delete_event, name='delete_event'),
    path('api/edit_event/<int:event_id>/', edit_event, name='edit_event'),
     path('api/get_obras/', get_obras, name='get_obras'),
    path('api/get_encarregados/', get_encarregados, name='get_encarregados'),









    





    

    # Aqui estamos definindo a rota para a sua view home
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)