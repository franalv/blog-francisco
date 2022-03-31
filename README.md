BLOG

El presente Blog es un proyecto creado para Coder House. El mismo se encuentra desarrollado bajo el lenguaje Python con el framework Django. La funcionalidad básica del mismo consiste en una pantalla inicial donde el usuario puede ver la página inicial del mismo creada en un html denominado "index.html", en el cual se visualizan las publicaciones realizadas por el autor del blog.

En la barra de navegación superior se encuentran las pestañas "Crear Publicación", "Buscar Publicaciones", "Suscribirse" y "Contacto".

La pestaña "Crear Publicación" está dedicada al Administrador del blog ya que desde allí puede redactar los textos que luego serán publicados en la página inicial del blog. Una vez redireccionado a la respectiva sección, se encuentra un formulario para insertar datos a la base de datos. La vista está realizada a través de una herencia del HTML "Index"

La pestaña "Buscar Publicaciones" sirve para buscar publicaciones realizadas en el blog. Dentro de la sección, se encuentra un formulario de búsqueda a la base de datos. La vista está realizada a través de una herencia del HTML "Index"

La pestaña "Suscribirse" tiene la utilidad de suscribirse a las novedades del blog para que se notifique via mail cuando el Administrador del sitio haga una nueva publicación. La vista está realizada a través de una herencia del HTML "Index"

La pestaña "Contacto" tiene la finalidad de contactarse con el Administrador del blog para realizar consultas, sugerencias u otro tipo de aportes. La vista está realizada a través de una herencia del HTML "Index"
