from django.db import models
from django.core.validators import MinLengthValidator
from ckeditor.fields import RichTextField
# Create your models here.

class Article(models.Model):
    author = models.ForeignKey("auth.User",on_delete= models.CASCADE,verbose_name ="YAZAR")#user tablosunu isaret eder user silinirse inputlarida siliniz on deletede
    title = models.CharField(max_length=30, validators=[MinLengthValidator(5)],verbose_name ="BASLIK")
    content = RichTextField()
    created_date = models.DateTimeField(auto_now_add=True,verbose_name ="OLUSTURULMA TARIHI") #O ANKI TARIHI DIREK ATAR
    article_image = models.FileField(blank = True, null = True,verbose_name="MAKALEYE FOTOGRAF YUKLEYIN")
    def __str__(self):
        return self.title #direk title ismini gosterir

    class Meta:
        ordering = ['-created_date']
class Comment(models.Model):
    article = models.ForeignKey(Article,on_delete=models.CASCADE,verbose_name = "MAKALE",related_name="comments")
    comment_author = models.CharField(max_length=50,verbose_name ="ISIM")
    comment_content = models.CharField(max_length=200, verbose_name ="YORUM")
    comment_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.comment_content
    class Meta:
        ordering = ['-comment_date']


 