# ProyectoSupermercado

Este proyecto surge de la idea de aplicar lo visto en el curso de Python de CoderHouse
Dentro de ProyectoSupermercado se tiene la AppAdministración en donde se crearon cuatro clases de las que sería útil tener registros en la administración de un supermercado

Estas clases son las siguientes: artículos, clientes, proveedores, y empleados. Para cada una de ellas, se crearon entre dos y cuatro atirbutos
Este desarrollo está en models.py

Dentro de la carpeta de AppAdministracion, en templates/AppAdministracion se crearon archivos html para cada una de las clases. Además, se creo un inicio.html, que es a donde se ingresa sin ninguna especificación.
Los archivos html heredan de padre.html la estructura general de la pagina

Por otra parte, se creo un formulario para cada una de las clases, para que se pudieran cargar datos desde la página, dentro del archivo forms.py
Estos datos se guardarán en la base de datos db.sqlite

Finalmente, se creo una vista para poder buscar categorias de los artículos del supermercado. Luego de buscar cierta categória en la base de datos, si esta existe, se mostrará cuál es el nombre y código del producto. En caso de que no exista, se especifica que no hay datos con la descripción que se desea buscar
