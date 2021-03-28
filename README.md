# BlogIntegracion

Un blog de integración de repaso de CodingDojo! 

## Instalación

1. Forkear el repositorio
2. Clonar localmente
3. Crear base de datos Postgres: `name: blog; user: postgres; password:postgres`
4. Crear entorno virtual y activarlo: `virtualenv .venv && .venv/bin/activate` 
5. Instalar requerimientos: `pip install -r requirements.txt`
6. Migrar base de datos: `python manage.py migrate`
7. ¡Correr servidor! `python manage.py runserver`

## Branches y commits

Crearemos una branch por cada nueva funcionalidad que agreguemos:

`git checkout -b branchName` -> Crea una branch y cambia a la misma

Después la empujaremos a Github:

`git add .` (o lo que sea)
`git commit -m  "mensaje"` 
`git push origin <nombre-de-la-branch>`

#### Hecho con ❤ por ⛩


