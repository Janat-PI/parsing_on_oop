from fastapi import FastAPI

from main.scripts import Response, Parsing


categories = {
    "monitors": 'monitory_bishkek'
}

response = Response(category=categories["monitors"])
parsing = Parsing(response=response)


app = FastAPI()

results = parsing.build()

@app.get("/index")
def index():
    return {
        "data": "Hello PythonDor!"
    }


@app.get("/get_data")
def get_data():
    return {
        "results": results
    }


@app.get("/movie/{id}")
def get_movie(id: int):
    return {
        "data": f"it is film with id {id}"
    }
    # request = DataBase.get("id"=id)