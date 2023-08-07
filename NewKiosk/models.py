from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=50) 

class Product(models.Model):
    product_name = models.CharField(max_length=50)
    id = models.AutoField(primary_key=True)
    product_detail = models.CharField(max_length=50, blank=True, default="")
    price = models.IntegerField(default=0)
    category = models.ForeignKey('Category', related_name='product', on_delete=models.CASCADE)
    is_soldout = models.BooleanField(default=False)
    quantity = models.IntegerField(default=0)
    
class Order(models.Model):
    products = models.ManyToManyField('Product', through='Product_Order', related_name= 'ordered')
    payment = models.CharField(max_length=50)
    is_takeout = models.BooleanField(default=True)
    total_price = models.IntegerField()
    
class Product_Order(models.Model):
    product = models.ForeignKey('Product', related_name='orders', on_delete=models.CASCADE, null = True)
    order = models.ForeignKey('Order', related_name='order_detail',on_delete=models.SET_NULL, null = True)
    

    #product = models.ForeignKey('Product', related_name='order_detail', on_delete=models.SET_NULL, null = True)
    #quantity = models.IntegerField()
    #order_num = models.IntegerField() #상품주문개수
    #id = models.AutoField(primary_key=True)
    #payment = models.CharField(max_length=50)
    #is_takeout = models.BooleanField(default=True)
    #total_price = models.IntegerField() #상품개수 * 단가 #
    
#class Product_OrderDetail(models.Model):
#    order = models.ForeignKey(Order, related_name='order_details', on_delete=models.CASCADE)
#    id = models.ForeignKey(Product, related_name='product_order_details', on_delete=models.CASCADE)
#    quantity = models.IntegerField(default=1)  # 상품 주문 수량  
   