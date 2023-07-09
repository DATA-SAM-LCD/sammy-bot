# Sammy Bot 🤖

Bot para la comunidad DATA SAM

Está hecho en Python y usa, principalmente, la librería [discord.py](https://discordpy.readthedocs.io/en/latest/index.html).

Cabe destacar que usamos de referencia el repositorio de [Nightkingale](https://github.com/Nightkingale/Raichu). Créditos para él y los contribuidores por el laburo que hicieron 👏.

## Instalación

Los siguientes comandos nos van a servir para obtener un entorno de trabajo en condiciones:

```shell
# Clonamos repositorio
>> git clone https://github.com/DATA-SAM-LCD/sammy-bot.git
>> cd ./sammy-bot

# Creamos entorno virtual
>> python -m virtualenv venv # o python -m venv venv
>> venv/Scripts/activate # En Windows. En Linux es: source venv/bin/activate
(venv) >> pip install -r requirements.txt 
```

Necesitaremos crear un .env en el root del proyecto. Pueden copiar y pegar el archivo `.env.example` y renombrarlo como `.env`. Los tokens y ids los pueden obtener de Discord Developers. Hay una [guía sobre esto en la documentación de discord.py](https://discordpy.readthedocs.io/en/latest/discord.html). Esto les habilitará a la creación de un bot propio para realizar las pruebas.

En caso de que tengan problemas con esta última parte, avisen en el [canal de texto correspondiente a este proyecto](https://discord.gg/YMJGEzbKMG).


## Cómo colaborar?

Preparamos un documento en Notion para que puedan tener todo lo necesario para colaborar. Igualmente y de forma resumida les dejamos todos lo que necesitan:

- [Documento Notion](https://jcrodriguez.notion.site/C-mo-arranco-con-git-y-GitHub-81b2b07ee8f64d08bf1652bd12e6d28a?pvs=4)
- Control de versiones, [git](https://git-scm.com/)
- Cuenta en [GitHub](https://github.com/)
- IDE para programar. Puede ser [VSCode](https://code.visualstudio.com/) (ideal), [Sublime Text](https://www.sublimetext.com/), [PyCharm](https://www.jetbrains.com/es-es/pycharm/)