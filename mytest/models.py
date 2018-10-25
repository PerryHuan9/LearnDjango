from django.db import models


class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
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
