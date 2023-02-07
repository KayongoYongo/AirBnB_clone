#!/usr/bin/python3
"""Definses the base model classs"""
from uuid import uuid4
from datetime import datetime


class BaseModel:
        """Represents the base model for the AirBnB project"""

        def __init__(self, *args, **kwargs):
            self.id = str(uuid.uuid4())
            self.created_at = datetime.today()
            self.updated_at = datetime.today()


