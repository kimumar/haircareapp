from django.db import models
from django.forms import Textarea, TextInput, Select
from django.forms import ModelForm

from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

class Setting(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )

    title = models.CharField(max_length=200)
    blogs_img1 = models.ImageField(blank=True, null=True, upload_to='images/')
    gallery_img1 = models.ImageField(blank=True, null=True, upload_to='images/')
    gallery_img2 = models.ImageField(blank=True, null=True, upload_to='images/')
    gallery_img3 = models.ImageField(blank=True, null=True, upload_to='images/')
    gallery_img4 = models.ImageField(blank=True, null=True, upload_to='images/')
    gallery_img5 = models.ImageField(blank=True, null=True, upload_to='images/')
    gallery_img6 = models.ImageField(blank=True, null=True, upload_to='images/')
    gallery_img7 = models.ImageField(blank=True, null=True, upload_to='images/')
    gallery_img8 = models.ImageField(blank=True, null=True, upload_to='images/')
    gallery_img9 = models.ImageField(blank=True, null=True, upload_to='images/')
    gallery_img10 = models.ImageField(blank=True, null=True, upload_to='images/')
    gallery_img11 = models.ImageField(blank=True, null=True, upload_to='images/')
    gallery_img12 = models.ImageField(blank=True, null=True, upload_to='images/')
    gallery_img13 = models.ImageField(blank=True, null=True, upload_to='images/')
    gallery_img14 = models.ImageField(blank=True, null=True, upload_to='images/')
    gallery_img15 = models.ImageField(blank=True, null=True, upload_to='images/')
    gallery_img16 = models.ImageField(blank=True, null=True, upload_to='images/')
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=200, choices=STATUS)
    
    def __str__(self):
        return self.title





class BookingMessage(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Closed', 'Closed'),
    )

    BODY = (
        ('Professional Makeup', 'Professional Makeup'),
        ('Manicure Pedicure', 'Manicure Pedicure'),
        ('Body Treatment', 'Body Treatment'),
        ('Haircut&Colouring', 'Haircut&Colouring'),
    )

    name = models.CharField(blank=True, null=True, max_length=200)
    email = models.CharField(blank=True, null=True, max_length=200)
    date = models.CharField(blank=True, null=True, max_length=200)
    time = models.CharField(blank=True, null=True, max_length=200)
    body = models.CharField(blank=True, null=True, max_length=200, choices=BODY, default='Professional Makeup')
    phone = models.CharField(blank=True, null=True, max_length=200)
    message = models.TextField(blank=True, null=True, max_length=500)
    status = models.CharField(blank=True, null=True, max_length=200, choices=STATUS)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


BODY = (
    ('Professional Makeup', 'Professional Makeup'),
    ('Manicure Pedicure', 'Manicure Pedicure'),
    ('Body Treatment', 'Body Treatment'),
    ('Haircut&Colouring', 'Haircut&Colouring'),
)


class BookingForm(ModelForm):
    class Meta:
        model = BookingMessage
        fields = ['name', 'email', 'date', 'time', 'body', 'phone', 'message']

        

class CommentMessage(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Read', 'Read'),
    )
    name = models.CharField(blank=True, null=True, max_length=200)
    email = models.CharField(blank=True, null=True, max_length=200)
    website = models.CharField(blank=True, null=True, max_length=200)
    message = models.TextField(blank=True, null=True, max_length=500)
    status = models.CharField(blank=True, null=True, max_length=200, choices=STATUS)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class CommentForm(ModelForm):
    class Meta:
        model = CommentMessage
        fields = ['name', 'email', 'website', 'message']
       

class Post(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Read', 'Read'),
    )
    form_image = models.ImageField(blank=True, null=True, upload_to='images/')
    date = models.CharField(blank=True, null=True, max_length=200)
    title = models.CharField(blank=True, null=True, max_length=200)
    post = models.TextField(blank=True, null=True)
    status = models.CharField(blank=True, null=True, max_length=200, choices=STATUS)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'date', 'post']
   