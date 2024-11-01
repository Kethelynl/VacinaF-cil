from django.core.management.base import BaseCommand
from django.core.mail import send_mail
from django.utils import timezone
from vaccines.models import MarcVaccine

class Command(BaseCommand):
    help = 'Envia notificações de email para vacinas marcadas no dia atual'

    def handle(self, *args, **kwargs):
        # Obtém a data atual
        hoje = timezone.now().date()
        
        # Seleciona vacinas marcadas para hoje
        marcacoes_hoje = MarcVaccine.objects.filter(next_dose=hoje)
        
        for marcacao in marcacoes_hoje:
            user_email = marcacao.user.email
            if user_email:
                send_mail(
                    subject='Lembrete de Vacina',
                    message=f'Olá, {marcacao.user.username}! Hoje você tem uma vacina marcada: {marcacao.vaccines.name_vacinne}. Não se esqueça!',
                    from_email='kethcavalari@gmail.com',  
                    recipient_list=[user_email],
                )
                self.stdout.write(self.style.SUCCESS(f'Email enviado para {user_email} sobre a vacina {marcacao.vaccines.name_vacinne}'))
            else:
                self.stdout.write(self.style.WARNING(f'O usuário {marcacao.user.username} não possui um email cadastrado.'))
