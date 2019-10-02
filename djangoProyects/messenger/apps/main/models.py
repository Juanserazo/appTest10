from django.db import models

class Manager(models.Model):
    id = models.AutoField(primary_key = True)
    state = models.BooleanField('State', default = True)
    create_date = models.DateField('Creation Date',auto_now = False, auto_now_add = True)
    modify_date = models.DateField('Modify Date', auto_now = True, auto_now_add = False)
    Delete_date = models.DateField('Delete Date', auto_now = True, auto_now_add = False)
    class Meta:
        #Para solo llamarla
        abstract = True

class Social(models.Model):
    facebook = models.URLField('Facebook', null = True, blank = True)
    instagram = models.URLField('Twitter', null = True, blank = True)
    web = models.URLField('Web', null = True, blank = True)
    class Meta:
        #Para solo llamarla
        abstract = True

class Category(Manager):
    name = models.CharField('Name', max_length = 150, unique = True)
    image = models.ImageField('Image', upload_to = 'category/')
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    def __str__(self):
        return self.name

class Author(Manager, Social):
    first_name = models.CharField('First Name', max_length = 150)
    last_name = models.CharField('Last Name', max_length = 150)
    email = models.CharField('E-mail', max_length = 200)
    description = models.TextField('Description')
    image = models.ImageField('Author Image', null = True, blank = True, upload_to = 'author/' )
    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'
    def __str__(self):
        return '{0},{1}'.format(self.first_name,self.last_name)