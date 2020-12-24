from django.db import models

class sectionList(models.Model):
    id_section = models.AutoField(primary_key=True)
    section = models.CharField(max_length = 50)

    def __str__(self):
        return self.section

class titleList(models.Model):
    id_title = models.AutoField(primary_key=True)
    id_section = models.ForeignKey(sectionList, on_delete=models.PROTECT)
    title = models.CharField(max_length = 50)
    article_text = models.TextField(null=True)

    def __str__(self):
        return self.title
