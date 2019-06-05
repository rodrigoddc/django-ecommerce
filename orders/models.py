from django.db import models
from shop.models import Product


class Order(models.Model):
    first_name = models.CharField(verbose_name='nome', max_length=60)
    last_name = models.CharField(verbose_name='sobrenome', max_length=60)
    email = models.EmailField()
    address = models.CharField(verbose_name='endereço', max_length=150)
    postal_code = models.CharField(verbose_name='cep', max_length=30)
    city = models.CharField(verbose_name='cidade', max_length=100)
    created = models.DateTimeField(verbose_name='criado', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='atualizado', auto_now=True)
    paid = models.BooleanField(verbose_name='pago', default=False)

    class Meta:
        ordering = ('-created', )

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE, verbose_name='pedido')
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE, verbose_name='Produto')
    price = models.DecimalField(verbose_name='preço', max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(verbose_name='quantidade', default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity
