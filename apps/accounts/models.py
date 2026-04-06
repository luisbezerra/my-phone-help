from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    hwid = models.CharField("ID do Hardware", max_length=255, unique=True, null=True, blank=True)
    is_active_license = models.BooleanField("Licença Ativa", default=True)

    def __str__(self):
        return f"Perfil: {self.user.username}"
