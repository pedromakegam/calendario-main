from django.db import models
from datetime import datetime, timedelta
import pytz

# Defina o fuso horário desejado
timezone = pytz.timezone('America/Sao_Paulo')

class Event(models.Model):
    title = models.CharField(max_length=200)
    start = models.DateTimeField()
    end = models.DateTimeField(null=True, blank=True)
    pes = models.CharField(max_length=200, blank=True, null=True)
    desligamento = models.CharField(max_length=10, blank=True, null=True)
    servico = models.CharField(max_length=200, blank=True, null=True)
    postes = models.IntegerField(default=0, blank=True, null=True)
    apoio_linha_viva = models.CharField(max_length=10, blank=True, null=True)
    concluir = models.BooleanField(default=False)
    status = models.CharField(max_length=50, blank=True, null=True)
    encarregado = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.title

    def parse_date(self, date_str):
        # Attempt to parse the date string with multiple formats
        formats = ["%d/%m/%Y %H:%M", "%d/%m/%Y", "%Y-%m-%dT%H:%M:%S.%fZ"]
        for fmt in formats:
            try:
                dt = datetime.strptime(date_str, fmt)
                # Converta a data para o fuso horário definido
                return timezone.localize(dt)
            except ValueError:
                continue
        # If all formats fail, raise an error
        raise ValueError(f"Date format for '{date_str}' is not supported")

    def save(self, *args, **kwargs):
        # Define horário padrão de início e fim
        default_start_hour = 6  # 6:00 AM
        default_end_hour = 9  # 9:00 AM

        # Verifica e converte o campo start para o formato correto se for string
        if isinstance(self.start, str):
            self.start = self.parse_date(self.start)
        elif not self.start:
            # Define o horário de início padrão se não estiver definido
            self.start = timezone.localize(datetime.now().replace(hour=default_start_hour, minute=0, second=0, microsecond=0))

        # Verifica e converte o campo end para o formato correto se for string
        if self.end and isinstance(self.end, str):
            self.end = self.parse_date(self.end)
        elif not self.end:
            # Define o horário de fim padrão se não estiver definido
            self.end = self.start + timedelta(hours=default_end_hour - default_start_hour)

        # Verifica se end é anterior ao start e ajusta se necessário
        if self.end <= self.start:
            self.end = self.start + timedelta(hours=default_end_hour - default_start_hour)

        super().save(*args, **kwargs)

class Obra(models.Model):
    nome = models.CharField(max_length=100, blank=True, null=True)
    projeto = models.CharField(max_length=100, blank=True, null=True)
    municipio = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        return self.nome


class Encarregado(models.Model):
    nome = models.CharField(max_length=50, blank=True, null=True)
    tipo = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.nome