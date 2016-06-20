from django.db import models


class Publisher(models.Model):
    '''
    出版商有名称，地址，所在城市、省，国家，网站
    '''
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=60, blank=True)
    state_province = models.CharField(max_length=30, blank=True)
    country = models.CharField(max_length=50, blank=True)
    website = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Author(models.Model):
    '''
    作者有姓，有名及email地址
    '''
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField(blank=True, verbose_name='e-mail')

    def __str__(self):
        return u'%s %s' % (self.first_name, self.last_name)


class Book(models.Model):
    '''
    书籍有书名和出版日期
    '''
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.title
