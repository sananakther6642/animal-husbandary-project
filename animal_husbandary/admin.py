from django.contrib import admin
from animal_husbandary.models import staff, vaccine, staflog, feedback, customer, animal, food

# Register your models here.

admin.site.register(staff)
admin.site.register(food)
admin.site.register(vaccine)
admin.site.register(customer)
admin.site.register(animal)


admin.site.register(staflog)
admin.site.register(feedback)
