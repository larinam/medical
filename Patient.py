# -*- coding: utf-8 -*-
__author__ = 'alarin'


class Patient:
    """Сущность Пациент."""
    name = ""
    age = ""
    state = "alive"

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.state = "alive"