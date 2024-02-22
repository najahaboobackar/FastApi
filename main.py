from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
class Person(BaseModel):
    id : int
    firstname:str
    lastname:str
    isMale:bool

@app.get("/", status_code=200)
def get_Person_info():
    return {"message": "car info running"}

@app.get("/getpersonbyid/{person_id}",status_code=200)
def getPerson_By_id(person_id: int):
    return {"message is ":f"your person id is{person_id}"}
@app.post('/addpersoninfo',status_code=200)
def addPerson_info(person:Person):
    return{
        "id":person.id,
        "firstname":person.firstname,
        "lastname":person.lastname,
        "isMale":person.isMale,
    }
    