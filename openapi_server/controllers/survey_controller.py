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
from openapi_server.interfaces.db_controller import mongo_adapter

ma = mongo_adapter('localhost', 27017)

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
        qid = ma.insertQuestion(survey_id, Question(create_question.question, create_question.question_type, create_question.answers))

    return str(ma.getQuestion(survey_id, qid))


def create_survey(create_survey=None):  # noqa: E501
    """Create Survey

     # noqa: E501

    :param create_survey: 
    :type create_survey: dict | bytes

    :rtype: Union[Survey, Tuple[Survey, int], Tuple[Survey, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        create_survey = CreateSurvey.from_dict(connexion.request.get_json())  # noqa: E501
        return ma.insertSurvey(Survey(name=create_survey.name))


def delete_question(survey_id, question_id):  # noqa: E501
    """Delete Question

     # noqa: E501

    :param survey_id: 
    :type survey_id: int
    :param question_id: 
    :type question_id: int

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    ma.deleteQuestion(survey_id, question_id)
    return f'Question {question_id} was deleted from survey {survey_id}'


def delete_survey(survey_id):  # noqa: E501
    """Delete Survey

     # noqa: E501

    :param survey_id: 
    :type survey_id: int

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    ma.deleteSurvey(survey_id)
    return f'Survey {survey_id} was deleted'


def get_question(survey_id, question_id):  # noqa: E501
    """Get Question

     # noqa: E501

    :param survey_id: 
    :type survey_id: int
    :param question_id: 
    :type question_id: int

    :rtype: Union[Question, Tuple[Question, int], Tuple[Question, int, Dict[str, str]]
    """
    return str(ma.getQuestion(survey_id, question_id))


def list_questions(survey_id):  # noqa: E501
    """List Questions

     # noqa: E501

    :param survey_id: 
    :type survey_id: int

    :rtype: Union[Questions, Tuple[Questions, int], Tuple[Questions, int, Dict[str, str]]
    """
    return ' '.join(str(e) for e in list(ma.getQuestions(survey_id)))


def publish_survey(survey_id, publish=None):  # noqa: E501
    """Publish Survey

     # noqa: E501

    :param survey_id: 
    :type survey_id: int
    :param publish: 
    :type publish: dict | bytes

    :rtype: Union[Survey, Tuple[Survey, int], Tuple[Survey, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        publish = Publish.from_dict(connexion.request.get_json())  # noqa: E501
        ma.updateSurvey(survey_id, 'published', True)
    return f'Survey {survey_id} is published'


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
        ma.updateSurvey(survey_id, 'end_date', set_end.end_date)
    return f'Date set to {set_end.end_date}'


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
        ma.updateSurvey(survey_id, 'start_date', set_start.start_date)
    return f'Date set to {set_start.start_date}'
