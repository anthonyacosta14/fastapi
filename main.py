from data.database import database
from typing import Union

from fastapi import FastAPI, Request
from data.modelo.menu import Menu
from data.dao.dao_trofeos import DaoTrofeos
from typing import Annotated
from fastapi import Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="templates")



@app.get("/")
def read_root(request:Request):
    dao = DaoTrofeos()
    trofeos = dao.get_all(database)
    return templates.TemplateResponse(
    request=request, name="principal.html", context={"trofeos": trofeos}
)


@app.get("/formaddalumnos")
def form_add_alumnos(request: Request):
    return templates.TemplateResponse(
    request=request, name="formaddAlumnos.html"
    )

@app.post("/add_trofeos")
def add_trofeos(request: Request, nombre: Annotated[str, Form()] = None):
    if nombre is None:
        dao = DaoTrofeos()
        trofeos = dao.get_all(database) 
        return templates.TemplateResponse(
            request=request, name="principal.html", context={"trofeos": trofeos}
        )
    
    dao = DaoTrofeos()
    dao.insert(database, nombre)  
    
    trofeos = dao.get_all(database)  
    
    return templates.TemplateResponse(
        request=request, name="principal.html", context={"trofeos": trofeos}
    )

@app.post("/delete_trofeo")
def delete_trofeo(request: Request, id: Annotated[int, Form()] = None):
    if id is None:
        return templates.TemplateResponse(
            request=request, name="principal.html", context={"error": "ID no proporcionado"}
        )
    
    dao = DaoTrofeos()
    dao.delete(database, id)
    
    trofeos = dao.get_all(database)
    return templates.TemplateResponse(
        request=request, name="principal.html", context={"trofeos": trofeos}
    )

@app.post("/update_trofeo")
def update_trofeo(request: Request, id: Annotated[int, Form()] = None, nombre: Annotated[str, Form()] = None):
    if id is None or nombre is None:
        return templates.TemplateResponse(
            request=request, name="principal.html", context={"error": "ID o nombre no proporcionado"}
        )
    
    dao = DaoTrofeos()
    dao.update(database, id, nombre)
    
    trofeos = dao.get_all(database)
    return templates.TemplateResponse(
        request=request, name="principal.html", context={"trofeos": trofeos}
    )



@app.get("/datos_personales", response_class=HTMLResponse)
async def test(request: Request):
    
    return templates.TemplateResponse(
        request=request, name="datos_personales.html", context={"nombre": "El messias del futbol"}                                                      
    )

@app.get("/equipos", response_class=HTMLResponse)
async def read_item(request: Request):

    return templates.TemplateResponse(
        request=request, name="equipos.html"                                                  
    )

@app.get("/memes")
def hola(request: Request):

     return templates.TemplateResponse(
        request=request, name="memes.html" , 
        
    )


