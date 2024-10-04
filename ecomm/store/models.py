from django.db import models
from django.contrib.auth.models import User

# Create your models here.


#1
class Customer(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name=models.CharField(max_length=200, null=True)
    email=models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.name
    
#2
class Product(models.Model):
    name = models.CharField(max_length=200, null= True)
    price = models.DecimalField(max_digits=8,decimal_places=2)
    digital = models.BooleanField(default=False, null=True,blank=False )
    image = models.ImageField(null=True, blank=True)


    def __str__(self):
        return self.name
    
    @property
    def imageURL(self):
        try:
            url=self.image.url
        except:
            url=''
        return url


#3
class Order(models.Model):
    customer=models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    date_ordered=models.DateTimeField(auto_now_add=True)
    complete=models.BooleanField(default=False, null=True)
    transaction_id=models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.id)
    
    @property
    def shipping(self):
        shipping=False
        orderitems = self.orderitem_set.all()
        for i in orderitems:
            if i.product.digital == False:
                shipping = True
        return shipping

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_product_total for item in orderitems])
        return total
    
    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total


#4
class OrderItem(models.Model):
    product=models.ForeignKey(Product, on_delete=models.SET_NULL,blank=True, null=True)
    order=models.ForeignKey(Order, on_delete=models.SET_NULL,blank=True, null=True)
    quantity=models.IntegerField(default=0, null=True, blank=True)
    date_added=models.DateTimeField(auto_now_add=True)

    @property
    def get_product_total(self):
        get_total= self.product.price * self.quantity
        return get_total



#5
class ShippingAddress(models.Model):
    customer=models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    order=models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    address=models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200, null=True)
    zipcode = models.IntegerField(default=110023, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __self__(self):
        return self.address

