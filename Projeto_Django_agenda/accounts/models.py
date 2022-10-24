from dataclasses import field, fields
from django.db import models
from contatos.models import Contato
from django import forms


class FormContaro(forms.ModelForm):
    class Meta:
        model = Contato
        exclude = ('mostrar',)
