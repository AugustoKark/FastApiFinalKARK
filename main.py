import uvicorn
from fastapi import FastAPI

from Database.database import Database
from Controllers.Implement.AutorController import AutorController
from Controllers.Implement.DomicilioController import DomicilioController
from Controllers.Implement.LibroController import LibroController
from Controllers.Implement.LocalidadController import LocalidadController
from Controllers.Implement.PersonaController import PersonaController

# from config.database import Database
# from controllers.address_controller import AddressController
# from controllers.bill_controller import BillController
# from controllers.category_controller import CategoryController
# from controllers.client_controller import ClientController
# from controllers.order_controller import OrderController
# from controllers.order_detail_controller import OrderDetailController
# from controllers.product_controller import ProductController
# from controllers.review_controller import ReviewController


def create_fastapi_app():
    fastapi_app = FastAPI()

    

    autor_controller = AutorController()
    fastapi_app.include_router(autor_controller.router, prefix="/autores")

    domicilio_controller = DomicilioController()
    fastapi_app.include_router(domicilio_controller.router, prefix="/domicilios")

    libro_controller = LibroController()
    fastapi_app.include_router(libro_controller.router, prefix="/libros")

    localidad_controller = LocalidadController()
    fastapi_app.include_router(localidad_controller.router, prefix="/localidades")

    persona_controller = PersonaController()
    fastapi_app.include_router(persona_controller.router, prefix="/personas")

    

   

    return fastapi_app


def run_app(fastapi_app: FastAPI):
    uvicorn.run(fastapi_app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    db = Database()
    db.create_tables()
    app = create_fastapi_app()
    run_app(app)