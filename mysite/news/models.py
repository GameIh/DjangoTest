from django.db import models

# Create your models here.

class News(models.Model):
    title = models.CharField(max_length=150,verbose_name='Наименование')
    content = models.TextField(blank=True,verbose_name='Контент')
    created_at = models.DateField(auto_now_add=True,verbose_name='Дата создания')
    updated_at = models.DateField(auto_now=True,verbose_name='Дата редактирования')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d',verbose_name='Картинка',blank=True)
    is_published = models.BooleanField(default=True,verbose_name='Опубликовано')
    category = models.ForeignKey('Category',on_delete=models.PROTECT, null=True,verbose_name='Категория')



    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['id']

class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Наименование категории')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']