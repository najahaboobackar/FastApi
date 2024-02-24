from fastapi import FastAPI,status,HTTPException
from pydantic import BaseModel
from database import SessionLocal
import models

app = FastAPI()
db=SessionLocal()

class OurBaseModel(BaseModel):
    class Config():
        orm_model=True


class Person(OurBaseModel):
    id : int
    firstname:str
    lasttname:str
    isMale:bool
@app.get('/',response_model=list[Person],status_code=status.HTTP_200_OK)
def getallPerson():
    getallModel=db.query(models.Person).all()
    return getallModel
@app.post('/addperson',response_model=Person,status_code=status.HTTP_201_CREATED)
def addPerson(person:Person):
    newPerson=models.Person(
        id=person.id,
        firstname=person.firstname,
        lasttname=person.lasttname,
        isMale=person.isMale
    )
    findperson=db.query(models.Person).filter(models.Person.id==person.id).first()
    if findperson is not None: 
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE,detail="the person this id is already existing")  
    db.add(newPerson)
    db.commit()
    return newPerson
    
    
    

#@app.get("/", status_code=200)
#def get_Person_info():
 #   return {"message": "car info running"}

#@app.get("/getpersonbyid/{person_id}",status_code=200)
#def getPerson_By_id(person_id: int):
 #   return {"message is ":f"your person id is{person_id}"}
#@app.post('/addpersoninfo',status_code=200)
#def addPerson_info(person:Person):
 #   return{
  #      "id":person.id,
   #     "firstname":person.firstname,
    #    "lastname":person.lastname,
     #   "isMale":person.isMale,