#!/usr/bin/python3

"""
BaseModel module
defines the BaseModel class that will serve as the base class for other models.
"""

import uuid
from datetime import datetime
import models


class BaseModel():
    """defines all common methods for other classes"""

    def __init__(self, *args, **kwargs):
        """initialize a new instances of base model"""
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                if key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """returns a string representation of the instance"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """updates the public instance attribute
           updated_at with currnet datetime"""

        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all key:value of __dict__"""
        dictionary = self.__dict__.copy()
        dictionary['__class__'] = self.__class__.__name__
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()

        return dictionary
