from django.db import models
from django.contrib import admin
from softdelete.models import *
from softdelete.admin import *

class TestModelOne(SoftDeleteObject):
    extra_bool = models.BooleanField(default=False)
    
class TestModelTwo(SoftDeleteObject):
    extra_int = models.IntegerField()
    tmo = models.ForeignKey(TestModelOne,related_name='tmts')
    
class TestModelThree(SoftDeleteObject):
    tmos = models.ManyToManyField(TestModelOne, through='TestModelThrough')
    extra_int = models.IntegerField(blank=True, null=True)

class TestModelThrough(SoftDeleteObject):
    tmo1 = models.ForeignKey(TestModelOne, related_name="left_side")
    tmo3 = models.ForeignKey(TestModelThree, related_name='right_side')

class TestModelSafeDeleteCascade(SoftDeleteObject):
    softdelete_policy = SoftDeleteObject.SOFT_DELETE_CASCADE
    extra_int = models.IntegerField()

class TestModelSoftDelete(SoftDeleteObject):
    softdelete_policy = SoftDeleteObject.SOFT_DELETE
    parent = models.ForeignKey(TestModelSafeDeleteCascade, related_name='x')

class TestModelDefault(SoftDeleteObject):
    parent = models.ForeignKey(TestModelSoftDelete, related_name='y')


admin.site.register(TestModelOne, SoftDeleteObjectAdmin)
admin.site.register(TestModelTwo, SoftDeleteObjectAdmin)
admin.site.register(TestModelThree, SoftDeleteObjectAdmin)
admin.site.register(TestModelThrough, SoftDeleteObjectAdmin)
admin.site.register(TestModelSafeDeleteCascade, SoftDeleteObjectAdmin)
admin.site.register(TestModelSoftDelete, SoftDeleteObjectAdmin)
admin.site.register(TestModelDefault, SoftDeleteObjectAdmin)
