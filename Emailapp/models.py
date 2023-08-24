from django.db import models

# Create your models here.

class SendMail(models.Model):
    toemail = models.EmailField(max_length=50)
    subject = models.CharField(max_length=100)
    messages = models.TextField('500')
    file = models.FileField(upload_to='files',max_length=300)
    
    def __str__(self):
        return self.toemail
    
    class Meta:
        db_table ="email"
                
# from django import forms
    
# class mailForm(forms.ModelForm):
#     class Meta:
#         model = SendMail
#         fields = '__all__'
        