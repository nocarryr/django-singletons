from __future__ import absolute_import, print_function, unicode_literals

from django.db import models

class SingletonModel(models.Model):

    class Meta:
        abstract = True

    @classmethod
    def get_or_create(cls, **kwargs):
        try:
            obj = cls.objects.get(id=1)
        except cls.DoesNotExist:
            obj = cls(**kwargs)
            obj.save()
        return obj
        
    def save(self, *args, **kwargs):
        self.id=1
        super(SingletonModel, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass
