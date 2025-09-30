from __future__ import annotations

from django.db import models


class SayLog(models.Model):
    message = models.TextField()

    class Meta:
        db_table = "saylog"

    def __str__(self):
        return str(self.pk)
