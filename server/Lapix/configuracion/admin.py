#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib import admin
from exileui.admin import exileui
import models

# Register your models here.


exileui.register(models.Sede)
