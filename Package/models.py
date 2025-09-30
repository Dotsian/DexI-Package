from __future__ import annotations

from tortoise import fields, models


class SayLog(models.Model):
    id = fields.IntField(pk=True)
    message = fields.TextField()

    class Meta:
        table = "saylog"

    def __str__(self) -> str:
        return str(self.pk)
