from django.shortcuts import render
from django.shortcuts import render
from django.http import JsonResponse
from .models import *
import json
from django.shortcuts import render, get_object_or_404


from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def home_view(request):
    return render(request, 'core/index.html')


def save_event(request):
    if request.method == 'POST':
        event_data = json.loads(request.body)
        print(event_data)
        event, created = Event.objects.update_or_create(
            id=event_data.get('id', None),
            defaults={
                'title': event_data.get('title'),
                'start': event_data.get('start'),
                'end': event_data.get('end'),
                'pes': event_data.get('pes'),
                'desligamento': event_data.get('desligamento'),
                'servico': event_data.get('servico'),
                'postes': event_data.get('postes'),
                'apoio_linha_viva': event_data.get('apoio_linha_viva'),
                'concluir': event_data.get('concluir'),
                'status': event_data.get('status'),
                'encarregado': event_data.get('encarregado')
            }
        )
        
        return JsonResponse({'id': event.id, 'created': created})

    return JsonResponse({'error': 'Invalid request method'}, status=400)

def get_events(request):
    events = list(Event.objects.values())
    return JsonResponse(events, safe=False)

def edit_event(request, event_id):
    if request.method == 'POST':
        event_data = json.loads(request.body)
        event = get_object_or_404(Event, id=event_id)
        event.title = event_data.get('title', event.title)
        event.start = event_data.get('start', event.start)
        event.end = event_data.get('end', event.end)
        event.pes = event_data.get('pes', event.pes)
        event.desligamento = event_data.get('desligamento', event.desligamento)
        event.servico = event_data.get('servico', event.servico)
        event.postes = event_data.get('postes', event.postes)
        event.apoio_linha_viva = event_data.get('apoio_linha_viva', event.apoio_linha_viva)
        event.concluir = event_data.get('concluir', event.concluir)
        event.status = event_data.get('status', event.status)
        event.encarregado = event_data.get('encarregado', event.encarregado)
        event.save()
        return JsonResponse({'message': 'Event updated successfully.'})
    return JsonResponse({'error': 'Invalid request method.'}, status=400)

def delete_event(request, event_id):
    if request.method == 'DELETE':
        event = get_object_or_404(Event, id=event_id)
        event.delete()
        return JsonResponse({'message': 'Event deleted successfully.'})
    return JsonResponse({'error': 'Invalid request method.'}, status=400)


def get_obras(request):
    obras = Obra.objects.all().values('projeto', 'nome', 'municipio')
    obras_list = list(obras)
    return JsonResponse(obras_list, safe=False)

def get_encarregados(request):
    encarregados = Encarregado.objects.all().values('nome', 'tipo')
    encarregados_list = list(encarregados)
    return JsonResponse(encarregados_list, safe=False)