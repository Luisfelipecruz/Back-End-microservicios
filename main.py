from fastapi import FastAPI
from controller import usuarioController, materiaEstudianteController, agendamientoController, grafoController
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
origins = [
        'http://localhost:3000'
]
app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
)

app.include_router(usuarioController.router)
app.include_router(materiaEstudianteController.router)
app.include_router(agendamientoController.router)
app.include_router(grafoController.router)
