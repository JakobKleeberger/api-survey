# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class SetStart(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id=None, start_date=None):  # noqa: E501
        """SetStart - a model defined in OpenAPI

        :param id: The id of this SetStart.  # noqa: E501
        :type id: int
        :param start_date: The start_date of this SetStart.  # noqa: E501
        :type start_date: str
        """
        self.openapi_types = {
            'id': int,
            'start_date': str
        }

        self.attribute_map = {
            'id': 'id',
            'start_date': 'start-date'
        }

        self._id = id
        self._start_date = start_date

    @classmethod
    def from_dict(cls, dikt) -> 'SetStart':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SetStart of this SetStart.  # noqa: E501
        :rtype: SetStart
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this SetStart.


        :return: The id of this SetStart.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SetStart.


        :param id: The id of this SetStart.
        :type id: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def start_date(self):
        """Gets the start_date of this SetStart.


        :return: The start_date of this SetStart.
        :rtype: str
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this SetStart.


        :param start_date: The start_date of this SetStart.
        :type start_date: str
        """
        if start_date is None:
            raise ValueError("Invalid value for `start_date`, must not be `None`")  # noqa: E501

        self._start_date = start_date