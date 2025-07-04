from django.contrib import admin
from .models import ChaiVarity, ChaiReview, Store, StoreOwner

# Register your models here.
class ChaiReviewInline(admin.TabularInline):
    model = ChaiReview
    extra= 2

class ChaiVarietyAdmin(admin.ModelAdmin):
    list_display =('name', 'type', 'description', 'date_added')
    inlines = [ChaiReviewInline]

class StoreAdmin(admin.ModelAdmin):
    list_display = ('name','location','image' )

class StoreOwnerAdmin(admin.ModelAdmin):
    list_display = ('store', 'owner','contact_number',)

# Register your models here.


admin.site.register(ChaiVarity, ChaiVarietyAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(StoreOwner, StoreOwnerAdmin)


