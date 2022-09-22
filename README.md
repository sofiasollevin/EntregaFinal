#Proyecto CoderHouse - Sofía Levin, Nicolás Cide, Fátima Albornoz y Santiago Ferrero

Esta es una página web que tiene por objetivo entregar a los usuarios una serie de servicios relacionados con el Campeonato Mundial de Futbol de Qatar 2022. 

En primer lugar, el sitio tiene la posibilidad de registrar usuarios con sus datos de XXXXXXXXXXX, y guarda esos datos en una base de datos SQLite.

En la página de Inicio, que es la primer página del sitio, se muestra una serie de fotos que van cambiando a medida que pasan los segundos, y también se pueden cambiar con las flechas para el costado. 

Desde la página de Inicio a su vez, se puede acceder a las diferentes secciones del sitio, presionando en los botones en el margen superior de la pantalla, con las siguientes categorías: Noticias, Selecciones,  Chat, Contactos, About us, así como también la posibilidad de registrarse en la página presionando el botón Register

A su vez, en la parte inferior de la página de Inicio, existen accesos directos a cada una de estas mismas categorías, con una breve reseña que describe en qué consiste cada vista, y un mapa acompañado de una breve descripción de Qatar. 

Al presionar en cada uno de los botones mencionados, el sitio nos direcciona a otras URLs, recorriendo así el contenido del sitio. 

En primer lugar, tenemos la URL de Noticias, donde el usuario podrá acceder a las últimas noticias relevantes relacionadas con el Campeonato. Las noticias se despliegan incluyendo una foto, un texto descriptivo, y un botón de Leer más, que permite ampliar la noticia al presionar sobre el mismo. Se puede ver esta funcionalidad en la primer noticia, Grupos del Mundial Qatar 2022, la cual instrumentamos a modo de ejemplo. En el resto de las noticias, la página direcciona al usuario a otra página que muestra el mensaje de Pagina en Construcción, al presionar Leer más. 

En segundo lugar, tenemos la URL de Selecciones. En ella se puede apreciar las banderas de cada uno de los países participantes del Mundial (se colocaron las banderas de Argentina, Brasil y Uruguay a modo de ejemplo, para agregar el resto de los países es exactamente el mismo procedimiento seguido). Por otro lado, en la parte inferior de la página, existe un campo de Búsqueda, donde se pueden listar los jugadores de una Selección, al escribir el país pertinente. 

Se han ingresado datos para los países de Argentina y Uruguay, a modo de ejemplo. Estos datos se encuentran guardados en una base de datos SQLite asociada a cada país. 

Continuando con el sitio, se ha incluido una aplicación de mensajería, donde los usuarios pueden unirse a distintas salas, y participar de conversaciones multiusuario. Para acceder a esta funcionalidad, se debe presionar sobre el botón Chat. Al ingresar, el sistema va a solicitar que introduzca la sala en la cual quiere hablar, y el nombre del usuario con el cual quiere figurar. 

Luego se despliega la historia de los mensajes enviados en dicha sala, y el usuario tiene la posibilidad de enviar nuevos mensajes. 

Por otro lado, también existe la categoría Contactos, la cual nos direcciona a una URL en la que el usuario puede enviar mensajes de contacto con los administradores de la página. Allí puede ingresar sus datos Email, Nombre, Contacto telefónico y el mensaje que desea hacer llegar. Los datos y el respectivo mensaje ingresado, son guardados en una Base de Datos SQLite, también pudiendo ser visualizada desde la vista Admin.

La última categoría es la de About Us, en la que se despliega una declaración de la misión del sitio, en la parte superior, y en la parte inferior se realiza una pequeña presentación de cada uno de los integrantes del equipo.

Para finalizar, se presenta una lista con las URLs del proyecto para poder interactuar con el mismo:

Inicio: http://localhost:8000/
Noticias: http://localhost:8000/noticias
Selecciones: http://localhost:8000/selecciones
Chat: http://localhost:8000/AppChat
Contactos: http://localhost:8000/contactos
About Us: http://localhost:8000/nosotros
Admin: http://localhost:8000/admin/ 

Este último enlace, cuenta con dos usuarios. El primero tiene permisos de lectura, escritura y el segundo sólo de lectura.

Usuario Administrador: admin 
Password: admin

Usuario: usuario
Password: sinprivilegios

Participación de cada integrante:
Sofía Levin: views, formularios, html, base de datos
Nicolás Cide: models, urls, html, migraciones
Fátima Albornoz: views, urls, app chat, admin
Santiago Ferrero: models, formularios, app chat, readme
La coordinación del trabajo y el resto del trabajo se hizo en conjunto por zoom.
 
