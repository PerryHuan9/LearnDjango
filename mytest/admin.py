from django.contrib import admin

from .models import Musician, Album, Pizza, Topping


class AlbumAdmin(admin.TabularInline):
    model = Album
    extra = 1


class MusicianAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['instrument', 'type', 'gender']}),
        ('name_info', {'fields': ['first_name', 'last_name'], 'classes': ['show']}),

    ]
    inlines = [AlbumAdmin]
    list_display = ('id','first_name', 'last_name', 'instrument', 'type')


admin.site.register(Musician, MusicianAdmin)


class ToppingAdmin(admin.ModelAdmin):
    list_display = ('name', 'taste')


class PizzaAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')


admin.site.register(Topping, ToppingAdmin)
admin.site.register(Pizza, PizzaAdmin)

from .models import Person, Group, Membership


class MembershipInline(admin.TabularInline):
    model = Membership
    extra = 1


class PersonAdmin(admin.ModelAdmin):
    inlines = [MembershipInline]
    pass


class GroupAdmin(admin.ModelAdmin):
    inlines = [MembershipInline]
    pass


class MembershipAdmin(admin.ModelAdmin):
    pass


admin.site.register(Person, PersonAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Membership, MembershipAdmin)

'''
单对单测试
'''
from .models import Place, Restaurant, Waiter


class WaiterInline(admin.TabularInline):
    model = Waiter
    extra = 1


class WaiterAdmin(admin.ModelAdmin):
    pass


class PlaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'address')


class RestaurantAdmin(admin.ModelAdmin):
    inlines = [WaiterInline]


admin.site.register(Place, PlaceAdmin)
admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(Waiter, WaiterAdmin)

