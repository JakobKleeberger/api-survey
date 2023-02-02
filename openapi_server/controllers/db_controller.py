import json

import pymongo
from openapi_server.models.survey import Survey
from openapi_server.models.question import Question
from bson import ObjectId


class mongo_adapter():
    def __init__(self):
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        db_name = "api-survey"
        sur_col = "surveys"
        que_col = "questions"
        mydb = myclient[db_name]
        self.sur_col = mydb[sur_col]
        self.que_col = mydb[que_col]

    def insertSurvey(self, survey):
        sur_dict = {"name": survey.name, "start_date": survey.start, "end_date": survey.end, "published": survey.published}
        ins = self.sur_col.insert_one(sur_dict)
        return ins.__inserted_id

    def getSurvey(self, id):
        query = {"_id": ObjectId(id)}
        return self.sur_col.find_one(query)

    def updateSurvey(self, id, key, value):
        query = {"_id": ObjectId(id)}
        newvalues = { "$set": { key: value } }
        return self.sur_col.update_one(query, newvalues)

    def dropSurvey(self, id):
        query = {"_id": ObjectId(id)}
        return self.sur_col.delete_one(query)

    def insertQuestion(self, surv_id,  question):
        sur_dict = {"surv_id": surv_id, "question": question.question, "question-type": question.question_type, "answers": question.answers}
        ins = self.sur_col.insert_one(sur_dict)
        return ins.__inserted_id

    def getQuestions(self, id):
        query = {"surv_id": id}
        return self.sur_col.find(query)

    def getQuestion(self, surv_id, question_id):
        query = {"surv_id": surv_id, "_id": ObjectId(question_id)}
        return self.sur_col.find_one(query)

    def deleteQuestion(self, surv_id, question_id):
        query = {"surv_id": surv_id, "_id": ObjectId(question_id)}
        return self.sur_col.delete_one(query)

if __name__ == '__main__':
    db = mongo_adapter()
    sid = db.insertSurvey(Survey(name="test"))
    print(sid)
    print(db.getSurvey(sid))
    print(db.getQuestions(sid))
    qid = db.insertQuestion(sid, Question(question="Wie gehts?", question_type="multi", answers="1:nein,2:doch,3:ohh"))
    print(db.getQuestions(sid))
    print(db.getQuestion(sid, qid))
    db.updateSurvey(sid, "published", True)
    print(db.getSurvey(sid))
    db.dropSurvey(sid)
    print(db.getSurvey(sid))




