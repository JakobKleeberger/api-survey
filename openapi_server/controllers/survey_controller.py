import connexion
import six
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.create_question import CreateQuestion  # noqa: E501
from openapi_server.models.create_survey import CreateSurvey  # noqa: E501
from openapi_server.models.publish import Publish  # noqa: E501
from openapi_server.models.question import Question  # noqa: E501
from openapi_server.models.questions import Questions  # noqa: E501
from openapi_server.models.set_end import SetEnd  # noqa: E501
from openapi_server.models.set_start import SetStart  # noqa: E501
from openapi_server.models.survey import Survey  # noqa: E501
from openapi_server import util


def create_question(survey_id, create_question=None):  # noqa: E501
    """Create Question

     # noqa: E501

    :param survey_id: 
    :type survey_id: int
    :param create_question: 
    :type create_question: dict | bytes

    :rtype: Union[Question, Tuple[Question, int], Tuple[Question, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        create_question = CreateQuestion.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_survey(create_survey=None):  # noqa: E501
    """Create Survey

     # noqa: E501

    :param create_survey: 
    :type create_survey: dict | bytes

    :rtype: Union[Survey, Tuple[Survey, int], Tuple[Survey, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        create_survey = CreateSurvey.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_survey(survey_id):  # noqa: E501
    """Delete Survey

     # noqa: E501

    :param survey_id: 
    :type survey_id: int

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    return 'do some magic!'


def list_questions(survey_id):  # noqa: E501
    """List Questions

     # noqa: E501

    :param survey_id: 
    :type survey_id: int

    :rtype: Union[Questions, Tuple[Questions, int], Tuple[Questions, int, Dict[str, str]]
    """
    return 'do some magic!'


def publish(survey_id, publish=None):  # noqa: E501
    """Publish

     # noqa: E501

    :param survey_id: 
    :type survey_id: int
    :param publish: 
    :type publish: dict | bytes

    :rtype: Union[Survey, Tuple[Survey, int], Tuple[Survey, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        publish = Publish.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def set_end(survey_id, set_end=None):  # noqa: E501
    """Set End-Date

     # noqa: E501

    :param survey_id: 
    :type survey_id: int
    :param set_end: 
    :type set_end: dict | bytes

    :rtype: Union[Survey, Tuple[Survey, int], Tuple[Survey, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        set_end = SetEnd.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def set_start(survey_id, set_start=None):  # noqa: E501
    """Set Start-Date

     # noqa: E501

    :param survey_id: 
    :type survey_id: int
    :param set_start: 
    :type set_start: dict | bytes

    :rtype: Union[Survey, Tuple[Survey, int], Tuple[Survey, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        set_start = SetStart.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
