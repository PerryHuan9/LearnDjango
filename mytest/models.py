from django.db import models
import datetime


class Musician(models.Model):
    # 添加unique表示该字段的值在表中必须独一无二
    first_name = models.CharField(max_length=50, unique=True)
    # ForeignKey,MangToManyField和OneToOneField也有该参数，不过不为第一个参数，其第一个参数为模型
    # 其它类型的键均可以设置一个备注名verbose_name,默认为第一个参数，默认值是属性名的下划线转为空格的值
    last_name = models.CharField(max_length=50, verbose_name='LAST NAME')
    instrument = models.CharField(max_length=100)
    # blank为True允许为空，null为True时表示该字段为空时设置为NULL
    type = models.CharField(max_length=50, blank=True, null=True)
    gender = models.CharField(max_length=10, choices=(('m', 'man'), ('w', 'woman')), default='m', help_text='性别')
    # 主键字段是只可读的，如果修改该字段，便会重新创建一个数据
    id = models.CharField(max_length=10, primary_key=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()

    def __str__(self):
        return self.name


'''
多对多关系，例子：一种披萨有多种配料，一种配料存在于多种披萨中，这形成了多对多的关系
'''


class Topping(models.Model):
    name = models.CharField(max_length=50)
    taste = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Pizza(models.Model):
    # 只能在一个模型中设置下列属性，不能两个模型都设
    toppings = models.ManyToManyField(Topping)
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name


# 面对复杂的多对多关系时，加一个中间类会容易处理

class Person(models.Model):
    name = models.CharField(max_length=88)

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(Person, through='Membership')

    def __str__(self):
        return self.name


# 为多对多关系使用中间模型
class Membership(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date_joined = models.DateField()
    invite_reason = models.CharField(max_length=64)

    def __str__(self):
        return str(self.person) + '->' + str(self.group)


'''
    单对单关系

'''


class Place(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)

    def __str__(self):
        return "%s the place" % self.name


class Restaurant(models.Model):
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)
    place = models.OneToOneField(Place, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return "%s the restaurant named " % self.place.name


class Waiter(models.Model):
    name = models.CharField(max_length=50)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    def __str__(self):
        return "{} the waiter at {}".format(self.name, self.restaurant)
