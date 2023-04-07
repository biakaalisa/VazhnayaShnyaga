from fastapi import FastAPI
from typing import Union

app = FastAPI() #создание экземпляра приложения

mentors = [
    {
        "id": 1,
        "name": "Beber Abeber",
        "tags": ["JS", "FaastAPI", "Pytn"]
    },
    {
        "id": 2,
        "name": "Galkov",
        "tags": ["JS", "FaastAPI", "Pytn"]
    },
    {
        "id": 3,
        "name": "Aoba",
        "tags": ["JS", "FaastAPI", "Pytn"]
    }
]

@app.get("/AllMentors") #показывает какой путь должен быть прописан в строке, чтобы выполнить функцию (указывает маршрут )
def get_mentors():      # возвращает массив со всеми менторами
    return mentors 

@app.get("/PathMentors/{mentor_id}") #берем переменную из URL 
def get_mentors(mentor_id: int):      #передаем пер-ю из URL в ф-ю
    for mentor in mentors:      #пробегаем по всему массиву с менторами и ищем ментора с нужным нам id
        if(mentor["id"] == mentor_id):
            return mentor 
        
@app.get("/QueryMentors") #query-запрос, url-строка будет с ?
def get_mentors(mentor_id: int): #получается зсчет данной конструкции
    for mentor in mentors:
        if(mentor["id"] == mentor_id):
            return mentor 

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q} 




#взаимодействие с имеюимися данными, вызов различных процедур

from pydantic import BaseModel

class Mentor(BaseModel):  # BaseModel проверяет корректность заполнения типов
    id: int
    name: str
    tags: list[str]

mentors = [
    Mentor (id = 1, name = "Beber Abeber", tags = ["JS", "FaastAPI", "Pytn"]), 
    Mentor (id = 2, name = "Galkov", tags = ["JS", "FaastAPI", "Pytn"]), 
    Mentor (id = 3, name = "Aoba", tags = ["JS", "FaastAPI", "Pytn"]), 
]

@app.get("/mentors")
def get_mentors() -> list[Mentor]:   #конструкция для типизации (показывает, что ф-я возвращает массив менторов)
    return mentors  

class GetMentorInput(BaseModel):
    id: int

@app.get("/mentors")
def get_mentors(request: GetMentorInput) -> list[Mentor]: #(request: GetMentorInput) показывает, что пользователь может отправить json c данными о id ментора
    return mentors  

@app.post("/QueryMentors") # метод для отправки данных
def get_mentors(mentor_id: int) -> Mentor:
    for mentor in mentors:
        if(mentor.id == mentor_id): # mentor.id через точку, т.к. работаем с классом
            return mentor  
        



#заполнение пользователем пустового массива данных

class BaseMentor(BaseModel):
    name: str
    tags: list[str]

class GetMentor(BaseMentor):    #пример наследования классов
    id: int

class CreateMentor(BaseMentor):
    pass

mentors: list[GetMentor] = [ ]      #хрен пойми что

@app.get("/get_mentors")
def get_mentors(r) -> list[GetMentor]: 
    return mentors  

@app.post("/create_mentors")           #создание массивов и их отправка
def create_mentors(request: CreateMentor) -> int: 
    id = len(mentors)+1
    mentors.append(
        GetMentor(id = id, name=request.name, tags=request.tags)
    )
    return id

@app.delete("/delete_mentors/{id}")           #удаление созданных ранее массивов менторов по id
def delete_mentors(id:int):
    for mentor in mentors:
        if(mentor.id == id):
            mentors.remove(mentor)    




#Обработка ошибок в FastAPI

from fastapi import HTTPException
 
@app.delete("/exeption_mentors/{id}")   
def exeption_mentors(id:int):
    for mentor in mentors:
        if mentor.id not in mentors:
            raise HTTPException(status_code=404, detail="Ментор не найден") #кастомная ошибочка
        



# Кастомные заголовки

from fastapi import Header

@app.post("/get_my_browser")
def get_my_browser(request: CreateMentor, user_agent: str | None = Header(default=None)): #request - запрос браузеру
    return user_agent #User agent – программный элемент браузера, обозначающий человека, пользующимся им. Cодержит несколько строк, необходимых для идентификации.




# cookies. Хранятся в виде словаря. Смотреть значения кук удобно в мозиле, в хранилище инспектора

from fastapi import Response

@app.post("/create_cookie")
def create_cookie(response: Response): #ответ от браузера
    response.set_cookie(key="MentorCookie", value="1f")  #назначает куку MentorCount на 1f
    return {"message": "Come to the dark side, we have cookies"}

from fastapi import Cookie

@app.post("/count_cookie")      #название ебливых переменных, изменяемых в куках и самой ебливой куки(ключ) должны бать одинаковыми, ебись они конем, иначе нифия не будет работать
def count_mentor_cookie(response: Response, MentorCookieCount: int = Cookie(default = 0)): 
    response.set_cookie(key="MentorCookieCount", value=MentorCookieCount+1)

    if MentorCookieCount > 3:
        response.set_cookie(key="MentorCookieCount", max_age=0) # max_age указывает количество секунд до истечения срока действия файла cookie. Если равно 0 или отриц.числу кука сразу удаляется