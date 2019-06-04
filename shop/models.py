from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(verbose_name='nome', max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True, db_index=True)
    created_at = models.DateTimeField(verbose_name='criado em', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='atualizado em', auto_now=True)

    class Meta:
        ordering = ('name', )
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(verbose_name='nome', max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)
    description = models.TextField(verbose_name='descrição', blank=True)
    price = models.DecimalField(verbose_name='preço', max_digits=10, decimal_places=2)
    available = models.BooleanField(verbose_name='disponível', default=True)
    stock = models.PositiveIntegerField()
    created_at = models.DateTimeField(verbose_name='criado em', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='atualizado em', auto_now=True)
    image = models.ImageField(verbose_name='imagem', upload_to='products/%Y/%m/%d', blank=True)

    class Meta:
        ordering = ('name', )
        index_together = (('id', 'slug'),)
        verbose_name = 'produto'
        verbose_name_plural = 'produtos'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])
