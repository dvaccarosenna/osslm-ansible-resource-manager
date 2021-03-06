# coding: utf-8

from __future__ import absolute_import
from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class InlineResponse2003(Model):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, name: str=None, type: str=None):
        """
        InlineResponse2003 - a model defined in Swagger

        :param name: The name of this InlineResponse2003.
        :type name: str
        :param type: The type of this InlineResponse2003.
        :type type: str
        """
        self.swagger_types = {
            'name': str,
            'type': str
        }

        self.attribute_map = {
            'name': 'name',
            'type': 'type'
        }

        self._name = name
        self._type = type

    @classmethod
    def from_dict(cls, dikt) -> 'InlineResponse2003':
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_response_200_3 of this InlineResponse2003.
        :rtype: InlineResponse2003
        """
        return deserialize_model(dikt, cls)

    @property
    def name(self) -> str:
        """
        Gets the name of this InlineResponse2003.

        :return: The name of this InlineResponse2003.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """
        Sets the name of this InlineResponse2003.

        :param name: The name of this InlineResponse2003.
        :type name: str
        """

        self._name = name

    @property
    def type(self) -> str:
        """
        Gets the type of this InlineResponse2003.

        :return: The type of this InlineResponse2003.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str):
        """
        Sets the type of this InlineResponse2003.

        :param type: The type of this InlineResponse2003.
        :type type: str
        """

        self._type = type

