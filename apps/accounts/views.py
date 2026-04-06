from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from .models import UserProfile

class HardwareLoginAPIView(APIView):
    permission_classes = [] # Permite que qualquer um tente logar

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        hwid_sent = request.data.get('hwid')

        # 1. Validação básica de campos
        if not username or not password or not hwid_sent:
            return Response({"detail": "Faltam dados de login ou ID do computador."}, status=400)

        # 2. Autentica Usuário e Senha padrão do Django
        user = authenticate(username=username, password=password)
        
        if user:
            # Pega ou cria o perfil vinculado a esse usuário
            profile, _ = UserProfile.objects.get_or_create(user=user)
            
            # 3. Lógica da "Trava de PC"
            if not profile.hwid:
                # Primeiro acesso: Registra o PC atual como o oficial desta conta
                profile.hwid = hwid_sent
                profile.save()
                return Response({"status": "sucesso", "message": "Primeiro acesso: PC vinculado!"}, status=200)
            
            if profile.hwid == hwid_sent:
                # Acesso no mesmo PC de sempre: Liberado
                return Response({"status": "sucesso", "message": "Acesso autorizado."}, status=200)
            else:
                # Tentativa de usar a conta em outro PC: Bloqueado
                return Response({"status": "erro", "message": "Esta licença já pertence a outro computador."}, status=403)
        
        return Response({"status": "erro", "message": "Usuário ou senha incorretos."}, status=401)

