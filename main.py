import uvicorn
from fastapi import FastAPI

from Database.database import Database
from Controllers.Controllers import *

from starlette import status
from starlette.responses import JSONResponse
from Repositories.BaseRepositoryImpl import InstanceNotFoundError


def create_fastapi_app():
    fastapi_app = FastAPI()

    @fastapi_app.exception_handler(InstanceNotFoundError)
    async def instance_not_found_exception_handler(request, exc):
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"message": str(exc)},
        )

    

    autor_controller = AutorController()
    fastapi_app.include_router(autor_controller.router, prefix="/autores")

    libro_controller = LibroController()
    fastapi_app.include_router(libro_controller.router, prefix="/libros")

    genero_controller = GeneroController()
    fastapi_app.include_router(genero_controller.router, prefix="/generos")

    editorial_controller = EditorialController()
    fastapi_app.include_router(editorial_controller.router, prefix="/editoriales")

    usuario_controller = UsuarioController()
    fastapi_app.include_router(usuario_controller.router, prefix="/usuarios")

    prestamo_controller = PrestamoController()
    fastapi_app.include_router(prestamo_controller.router, prefix="/prestamos")
    

    

   

    return fastapi_app


def run_app(fastapi_app: FastAPI):
    uvicorn.run(fastapi_app, host="0.0.0.0", port=8080)


if __name__ == "__main__":
    db = Database()
    db.create_tables()
    app = create_fastapi_app()
    run_app(app)