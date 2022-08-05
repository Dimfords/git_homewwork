from tabnanny import verbose
from django.db import models


class warehouseadapp(models.Model):
    choices = (
            ('M', 'Male'),
            ('F', 'Female')
        )

    title = models.CharField(max_length=150, verbose_name="Наименование", blank=True)
    content = models.TextField(blank=True, verbose_name="Контент")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата публикации")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Обновлено")
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name="Фото", blank=True)
    is_published = models.BooleanField(default=True, verbose_name="Опубликовано", blank=True)
    qr_decode = models.CharField(max_length=15, verbose_name="Уникальный номер Биг-Бега", blank=True)
    crop = models.CharField(max_length=15, verbose_name="Культура", blank=True)
    # slug = models.SlugField(unique=True)
    # text_from_qr_code = models.CharField(max_length=150, verbose_name="Информация из QR-code")

    def __str__(self):
        return self.title

class Meta:
    verbose_name = "warehousedbapp"
    verbose_name_plural = "warehousedbapps"




