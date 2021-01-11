from django.db import models

class sectionList(models.Model):
    id_section = models.AutoField(primary_key=True)
    section = models.CharField(max_length = 50, verbose_name="Раздел")

    def __str__(self):
        return self.section

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class titleList(models.Model):
    id_title = models.AutoField(primary_key=True)
    id_section = models.ForeignKey(sectionList, on_delete=models.PROTECT, verbose_name="Раздел")
    title = models.CharField(max_length = 50, verbose_name="Пост")
    article_text = models.TextField(null=True, verbose_name="Текст")

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

