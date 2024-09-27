from django.db import models
from django.utils import timezone


class BaseModelQuerySet(models.QuerySet):
    def delete(self):
        return self.update(deleted_at=timezone.now(), is_active=False)


class BaseManager(models.Manager):
    def get_queryset(self):
        return BaseModelQuerySet(self.model, using=self._db).filter(deleted_at__isnull=True, is_active=True)


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True, editable=False)
    is_active = models.BooleanField(default=True, editable=False)

    objects = BaseManager()

    class Meta:
        abstract = True

    def delete(self, **kwargs):
        self.is_active = False
        self.deleted_at = timezone.now()
        self.save()

    def hard_delete(self, **kwargs):
        super().delete(**kwargs)


class Nome(BaseModel):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()


class Categoria(BaseModel):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)


class Produto(BaseModel):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
