from django.db import models
class Category(models.Model):
    name = models.CharField(max_length=15, verbose_name= "Mini name ")
    full_name = models.CharField(max_length=20, verbose_name= "Full name")

    def __str__(self):
        return f"{self.name}-{self.full_name}"


    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категорий"





class Car(models.Model):
    name = models.CharField(max_length=15)
    brand = models.CharField(max_length=30)
    full_price = models.IntegerField()
    discount_price = models.IntegerField(default=0)
    data = models.DateField()
    category = models.ForeignKey(Category, related_name="categories", on_delete=models.CASCADE)
    discount = models.IntegerField()

    def __str__(self):
        return self.brand

    def save(self, *args, **kwargs):
        if  self.discount == 0:
            self.discount = self.full_price
        else:
            self.discount_price = self.full_price *( 1 - self.discount/100)
        super().save(*args, **kwargs)



