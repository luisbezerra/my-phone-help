from django.db import models

class Brand(models.Model):
    name = models.CharField("Nome da Marca", max_length=100, unique=True)
    logo = models.ImageField("Logo da Marca", upload_to="brands/logos/", null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Device(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name="devices")
    model_name = models.CharField("Modelo do Aparelho", max_length=150)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return f"{self.brand.name} - {self.model_name}"
