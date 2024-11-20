from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    name = models.CharField(max_length = 100)
    email = models.EmailField(max_length = 100)
    phone_number = models.CharField(max_length=10, blank=True, null=True, validators =[RegexValidator("[0-9]{10}")])

    def __str__(self):
        return str(self.user)

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    image = models.ImageField(upload_to="", default="")

    def __str__(self):
        return self.name

class Feature(models.Model):
    class Ram(models.TextChoices):
        FOUR = "4GB", "4 GB"
        EIGHT = "8GB", "8 GB"
        SIXTEEN = "16GB", "16 GB"
        THREETWO = "32GB", "32 GB"
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    brand = models.CharField(max_length=20, null=True)
    model = models.CharField(max_length=20, null=True)
    processor = models.CharField(max_length=20, null=True)
    ram = models.CharField(max_length=5, choices=Ram.choices, default=Ram.FOUR)
    weight = models.DecimalField(max_digits=3, decimal_places=2, validators=[MinValueValidator(0.5), MaxValueValidator(5.0)], default=0,null=True)
    feature = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return str(self.product) + " Feature: " + self.feature

class Review(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE) 
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    content = models.TextField()
    datetime = models.DateTimeField(default=now)

    def __str__(self):
        return str(self.customer) +  " Review: " + self.content

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    date_ordered = models.DateTimeField(default=now)
    complete = models.BooleanField(default=False)
    total = models.IntegerField(null=True, default=0)

    def __str__(self):
        return str(self.id) + " " + str(self.total)

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0)
    date_added = models.DateTimeField(default=now)

    def __str__(self):
        return str(self.order)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total

class UpdateOrder(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    desc = models.CharField(max_length=500)
    date = models.DateField(default=now)

    def __str__(self):
        return str(self.order_id)

class CheckoutDetail(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    phone_number = models.CharField(max_length=10, blank=True, null=True, validators =[RegexValidator("[0-9]{10}")])
    total_amount = models.CharField(max_length=10, blank=True,null=True)
    address = models.CharField(max_length=300)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=100, validators =[RegexValidator("[0-9]{6}")])
    payment = models.CharField(max_length=100, blank=True)
    date_added = models.DateTimeField(default=now)

    def __str__(self):
        return self.address

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    desc = models.CharField(max_length=1000)

    def __str__(self):
        return self.name