from django.db import models

# Create your models here.


class Profile(models.Model):
    RELIGION=(
        ('Muslim','Muslim'),
        ('Hindu','Hindu'),
        ('Christian','Christian'),
        ('Bouddho','Bouddho')
    )

    GENDER=(
        ('Male','Male'),
        ('Female','Female'),
        ('Others','others')


    )


    Name = models.CharField(max_length=25,null=True,blank=True)
    Image = models.ImageField(upload_to='Profile_pic/',default='default/def.jpg',blank=True,null=True)
    Email = models.EmailField(max_length=30,blank=True,null=True)
    Age = models.PositiveIntegerField(blank=True,null=True)
    Address = models.TextField(max_length=200,blank=True,null=True)
    Phone_no = models.TextField(max_length=15,blank=True,null=True)
    Date_of_birth = models.TextField(max_length=12,blank=True,null=True)
    Religion = models.CharField(max_length=9,choices=RELIGION)
    Gender = models.CharField(max_length=6,choices=GENDER)

    def __str__(self):
        return str(self.Name)






