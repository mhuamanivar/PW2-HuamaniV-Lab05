<div align="center">
  <table width="1000px">
    <theader>
      <tr>
        <td><img src="https://github.com/rescobedoq/pw2/blob/main/epis.png?raw=true" alt="EPIS" style="width:50%; height:auto"/></td>
        <th>
          <span style="font-weight:bold;">UNIVERSIDAD NACIONAL DE SAN AGUSTIN</span><br />
          <span style="font-weight:bold;">FACULTAD DE INGENIERÍA DE PRODUCCIÓN Y SERVICIOS</span><br />
          <span style="font-weight:bold;">DEPARTAMENTO ACADÉMICO DE INGENIERÍA DE SISTEMAS E INFORMÁTICA</span><br />
          <span style="font-weight:bold;">ESCUELA PROFESIONAL DE INGENIERÍA DE SISTEMAS</span>
        </th>
        <td><img src="https://github.com/rescobedoq/pw2/blob/main/abet.png?raw=true" alt="ABET" style="width:50%; height:auto"/></td>
      </tr>
    </theader>
    <tbody>
      <tr><td colspan="3"><span style="font-weight:bold;">Formato</span>: Guía de Práctica de Laboratorio</td></tr>
      <tr><td><span style="font-weight:bold;">Aprobación</span>:  2022/03/01</td><td><span style="font-weight:bold;">Código</span>: GUIA-PRLD-001</td><td><span style="font-weight:bold;">Página</span>: 1</td></tr>
    </tbody>
  </table>
</div>

<div align="center">
    <span style="font-weight:bold;">INFORME DE LABORATORIO</span><br />
</div>

<div align="center">
  <table width="1000px">
    <theader>
      <tr><th colspan="6">INFORMACIÓN BÁSICA</th></tr>
    </theader>
    <tbody>
      <tr><td>ASIGNATURA:</td><td colspan="5">Programación Web 02</td></tr>
      <tr><td>TÍTULO DE LA PRÁCTICA:</td><td colspan="5">Django</td></tr>
      <tr><td>NÚMERO DE PRÁCTICA:</td><td>05</td><td>AÑO LECTIVO:</td><td>2023 A</td><td>NRO. SEMESTRE:</td><td width="60px">  III  </td></tr>
      <tr><td>FECHA DE PRESENTACIÓN:</td><td>20/06/2023</td><td>HORA DE PRESENTACIÓN:</td><td colspan="3">23:59</td></tr>
      <tr>
        <td colspan="4">NOMBRE:
          <ul>
            <li>Melsy Melany Huamaní Vargas</li>
          </ul>
        </td>
        <td>NOTA:</td><td></td>
      </tr>
      <tr>
        <td colspan="6" width="1000px">DOCENTES:
          <ul>
            <li>Anibal Sardon Paniagua</li>
          </ul>
        </td>
      </tr>
    </tbody>
  </table>
</div>


##
## APLICACIÓN LIBRARY


***Part 1: The local Library website (Instalando django)***

Se utiliza el sistema Windows para usar las herramientas necesarias para crear los proyectos.<br/><br/>

- Creando el ambiente y activandolo.
    ```sh
    C:\Users\melsy\Lab05>mkdir my_env
    C:\Users\melsy\Lab05>cd my_env
    C:\Users\melsy\Lab05\my_env>python -m venv C:\Users\melsy\Lab05\my_env
    C:\Users\melsy\Lab05\my_env>Scripts\activate.bat
    (my_env) C:\Users\melsy\Lab05\my_env>
    ```
    <br/>

- Actualizando el pip de python.
    ```sh
    (my_env) C:\Users\melsy\Lab05\my_env>python.exe -m pip install --upgrade pip
    Requirement already satisfied: pip in c:\users\melsy\lab05\my_env\lib\site-packages (22.3.1)
    Collecting pip
      Using cached pip-23.1.2-py3-none-any.whl (2.1 MB)
    Installing collected packages: pip
      Attempting uninstall: pip
        Found existing installation: pip 22.3.1
        Uninstalling pip-22.3.1:
          Successfully uninstalled pip-22.3.1
    Successfully installed pip-23.1.2
    ```
    <br/>

- Instalando Django con pip.
    ```sh
    (my_env) C:\Users\melsy\Lab05\my_env>pip install Django
    Collecting Django
      Using cached Django-4.2.2-py3-none-any.whl (8.0 MB)
    Collecting asgiref<4,>=3.6.0 (from Django)
      Using cached asgiref-3.7.2-py3-none-any.whl (24 kB)
    Collecting sqlparse>=0.3.1 (from Django)
      Using cached sqlparse-0.4.4-py3-none-any.whl (41 kB)
    Collecting tzdata (from Django)
      Using cached tzdata-2023.3-py2.py3-none-any.whl (341 kB)
    Installing collected packages: tzdata, sqlparse, asgiref, Django
    Successfully installed Django-4.2.2 asgiref-3.7.2 sqlparse-0.4.4 tzdata-2023.3
    ```
    <br/>

- Mostrando los paquetes instalados con ``pip list``.
    ```sh
    (my_env) C:\Users\melsy\Lab05\my_env>pip list
    Package    Version
    ---------- -------
    asgiref    3.7.2
    Django     4.2.2
    pip        23.1.2
    setuptools 65.5.0
    sqlparse   0.4.4
    tzdata     2023.3
    ```
    <br/>

***Part 2: Creating a skeleton website***

- Creación del proyecto library en la carpeta Scripts.

    ```sh
    (my_env) C:\Users\melsy\Lab05\my_env>cd Scripts
    (my_env) C:\Users\melsy\Lab05\my_env\Scripts>django-admin startproject library
    ```
    <br/>

- Creación de la aplicación catalog.

    ```sh
    (my_env) C:\Users\melsy\Lab05\my_env\Scripts>cd library
    (my_env) C:\Users\melsy\Lab05\my_env\Scripts\library>python manage.py startapp catalog
    ```
    <br/>

- Registro de la aplicación catalog dentro del archivo ``settings.py``.

    ```py
    # Application definition

    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'catalog.apps.CatalogConfig',
    ]
    ```
    <br/>

- Especificación de la base de datos dentro del archivo ``settings.py``, no se necesita hacer cambios.

    ```py
    # Database
    # https://docs.djangoproject.com/en/4.2/ref/settings/#databases

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
    ```
    <br/>
  
- Otros ajustes del proyecto: TimeZone dentro del archivo ``settings.py``.

    ```py
    # Internationalization
    # https://docs.djangoproject.com/en/4.2/topics/i18n/

    LANGUAGE_CODE = 'en-us'

    TIME_ZONE = 'America/Lima'

    USE_I18N = True

    USE_TZ = True
    ```
    <br/>

- Conectar el URL mapper dentro del archivo ``urls.py``.

    - Se añade estas líneas al final del archivo para agregar un nuevo elemento a la lista ``urlpatterns``, que incluye un oath para redirigir peticiones con patrón ``catalog/`` al módulo ``catalog.urls``.

      ```py
      # Use include() to add paths from the catalog application
      from django.urls import include

      urlpatterns += [
          path('catalog/', include('catalog.urls')),
      ]
      ```
      <br/>

    - Ahora añadimos estas líneas nuevamente al final para redireccionar la URL raíz ``127.0.0.1:8000`` al URL ``127.0.0.1:8000/catalog/``.

      ```py
      #Add URL maps to redirect the base URL to our application
      from django.views.generic import RedirectView
      urlpatterns += [
          path('', RedirectView.as_view(url='catalog/', permanent=True)),
      ]
      ```
      <br/>

    - También añadimos estas líneas para habilitar el servicio de archivos estáticos.

      ```py
      # Use static() to add URL mapping to serve static files during development (only)
      from django.conf import settings
      from django.conf.urls.static import static

      urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
      ```
      <br/>

- Crear archivo urls.py en carpeta catalog para definir la ``urlpatterns`` importada colocando las siguientes líneas.

    ```py
    from django.urls import path
    from . import views

    urlpatterns = [

    ]
    ```
    <br/>

- Prueba del framework del sitio web.

    - Ejecutamos las migrations de la base de datos

      ```sh
      (my_env) C:\Users\melsy\Lab05\my_env\Scripts\library>python manage.py makemigrations
      No changes detected
      (my_env) C:\Users\melsy\Lab05\my_env\Scripts\library>python manage.py migrate
      Operations to perform:
        Apply all migrations: admin, auth, contenttypes, sessions
      Running migrations:
        Applying contenttypes.0001_initial... OK
        Applying auth.0001_initial... OK
        Applying admin.0001_initial... OK
        Applying admin.0002_logentry_remove_auto_add... OK
        Applying admin.0003_logentry_add_action_flag_choices... OK
        Applying contenttypes.0002_remove_content_type_name... OK
        Applying auth.0002_alter_permission_name_max_length... OK
        Applying auth.0003_alter_user_email_max_length... OK
        Applying auth.0004_alter_user_username_opts... OK
        Applying auth.0005_alter_user_last_login_null... OK
        Applying auth.0006_require_contenttypes_0002... OK
        Applying auth.0007_alter_validators_add_error_messages... OK
        Applying auth.0008_alter_user_username_max_length... OK
        Applying auth.0009_alter_user_last_name_max_length... OK
        Applying auth.0010_alter_group_name_max_length... OK
        Applying auth.0011_update_proxy_permissions... OK
        Applying auth.0012_alter_user_first_name_max_length... OK
        Applying sessions.0001_initial... OK
      ```
      <br/>

    - Corremos el servidor (modificar)

      ```sh
      (my_env) C:\Users\melsy\Lab05\my_env\Scripts\library>python manage.py runserver
      Watching for file changes with StatReloader
      Performing system checks...

      System check identified no issues (0 silenced).
      June 19, 2023 - 20:46:06
      Django version 4.2.2, using settings 'library.settings'
      Starting development server at http://127.0.0.1:8000/
      Quit the server with CTRL-BREAK.

      [19/Jun/2023 20:46:17] "GET / HTTP/1.1" 301 0
      Not Found: /catalog/
      [19/Jun/2023 20:46:17] "GET /catalog/ HTTP/1.1" 404 2329
      Not Found: /favicon.ico
      [19/Jun/2023 20:46:18] "GET /favicon.ico HTTP/1.1" 404 2446
      [19/Jun/2023 20:46:35] "GET / HTTP/1.1" 301 0
      Not Found: /catalog/
      [19/Jun/2023 20:46:35] "GET /catalog/ HTTP/1.1" 404 2329
      Not Found: /favicon.ico
      [19/Jun/2023 20:46:35] "GET /favicon.ico HTTP/1.1" 404 2446
      ```
      <br/>

- (Desafío: Observar lo sucedido) En la url ``http://127.0.0.1:8000`` se puede ver la salida correctamente, debido a que aun no hay páginas definidas en el módulo ``catalog.urls``. Además, se ve que aunque hayamos ingresado a ese link, con la configuración anterior y el mapeo de URLs, este se redirige automáticamente a ``http://127.0.0.1:8000/catalog/``.

    <img src="img" style="width:70%"/><br/>
    <br/>

***Part 3: Using models***

- Definiendo los modelos del Library.

    - Modelo Genre, se crea la clase ``Genre`` que representa un género literario.

      ```py
      class Genre(models.Model):
          name = models.CharField(max_length=200, help_text='Enter a book genre (e.g. Science Fiction)')

          def __str__(self):
              return self.name
      ```
      <br/>

    - Modelo Book, se aumenta el import ``reverse`` con ``from django.urls import reverse`` y la clase ``Book`` que representa un libro, pero no un libro específico.

      ```py
      class Book(models.Model):
          title = models.CharField(max_length=200)

          # Foreign Key used because book can only have one author, but authors can have multiple books
          # Author is a string rather than an object because it hasn't been declared yet in the file
          author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)

          summary = models.TextField(max_length=1000, help_text='Enter a brief description of the book')
          isbn = models.CharField('ISBN', max_length=13, unique=True,
                                  help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')

          # ManyToManyField used because genre can contain many books. Books can cover many genres.
          # Genre class has already been defined so we can specify the object above.
          genre = models.ManyToManyField(Genre, help_text='Select a genre for this book')

          def __str__(self):
              return self.title

          def get_absolute_url(self):
              # Returns the URL to access a detail record for this book.
              return reverse('book-detail', args=[str(self.id)])
      ```
      <br/>

    - Modelo BookInstance, se importa ``uuid`` con ``import uuid`` para las instancias únicas de los libros y se crea la clase ``BookInstance`` que representa una copia específica de un libro.

      ```py
      class BookInstance(models.Model):

          id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular book across whole library')
          book = models.ForeignKey('Book', on_delete=models.RESTRICT, null=True)
          imprint = models.CharField(max_length=200)
          due_back = models.DateField(null=True, blank=True)

          LOAN_STATUS = (
              ('m', 'Maintenance'),
              ('o', 'On loan'),
              ('a', 'Available'),
              ('r', 'Reserved'),
          )

          status = models.CharField(
              max_length=1,
              choices=LOAN_STATUS,
              blank=True,
              default='m',
              help_text='Book availability',
          )

          class Meta:
              ordering = ['due_back']

          def __str__(self):
              return f'{self.id} ({self.book.title})'
      ```
      <br/>

    - Modelo Author, se crea la clase ``Author`` que representa a un autor de libros.

      ```py
      class Author(models.Model):
          
          first_name = models.CharField(max_length=100)
          last_name = models.CharField(max_length=100)
          date_of_birth = models.DateField(null=True, blank=True)
          date_of_death = models.DateField('Died', null=True, blank=True)

          class Meta:
              ordering = ['last_name', 'first_name']

          def get_absolute_url(self):
              # Returns the URL to access a particular author instance.
              return reverse('author-detail', args=[str(self.id)])

          def __str__(self):
              return f'{self.last_name}, {self.first_name}'
      ```
      <br/>

- Reiniciando y ejecutando las migraciones a base de datos.
    ```sh
    (my_env) C:\Users\melsy\Lab05\my_env\Scripts\library>python manage.py makemigrations
    Migrations for 'catalog':
      catalog\migrations\0001_initial.py
        - Create model Author
        - Create model Book
        - Create model Genre
        - Create model BookInstance
        - Add field genre to book

    (my_env) C:\Users\melsy\Lab05\my_env\Scripts\library>python manage.py migrate
    Operations to perform:
      Apply all migrations: admin, auth, catalog, contenttypes, sessions
    Running migrations:
      Applying catalog.0001_initial... OK
    ```
    <br/>

- (Desafío: Crear modelo Languague) Se crea la clase ``Language`` para que tenga un campo en caso de tener un libro en otro idioma.

    ```py
    class Language(models.Model):

        name = models.CharField(max_length=200,
                                help_text="Enter the book's natural language (e.g. English, French, Japanese etc.)")

        def __str__(self):
            return self.name
    ```
    <br/>

    - Se hacen nuevamente las migraciones a base de datos.

      ```sh
      (my_env) C:\Users\melsy\Lab05\my_env\Scripts\library>python manage.py makemigrations
      Migrations for 'catalog':
        catalog\migrations\0002_language.py
          - Create model Language

      (my_env) C:\Users\melsy\Lab05\my_env\Scripts\library>python manage.py migrate
      Operations to perform:
        Apply all migrations: admin, auth, catalog, contenttypes, sessions
      Running migrations:
        Applying catalog.0002_language... OK
      ```
      <br/>


***Part 4: Django admin site***

- Registrando los modelos en el archivo ``admin.py`` de la aplicación ``catalog`` colocando lo siguiente.

    ```py
    from .models import Author, Genre, Book, BookInstance

    admin.site.register(Book)
    admin.site.register(Author)
    admin.site.register(Genre)
    admin.site.register(BookInstance)
    ```
    <br/>

- Creando un superusuario para el proyecto.

    - Creamos el superusuario con el usuario ``mhuamanivar``, el correo electrónico proveniente de la UNSA y una contraseña común.

      ```sh
      (my_env) C:\Users\melsy\Lab05\my_env\Scripts\library>python manage.py createsuperuser
      Username (leave blank to use 'melsy'): mhuamanivar
      Email address: mhuamanivar@unsa.edu.pe
      Password:
      Password (again):
      This password is too common.
      This password is entirely numeric.
      Bypass password validation and create user anyway? [y/N]: y
      Superuser created successfully.
      ```
      <br/>

    - Corremos el servidor para verificar posteriormente la página.

      ```sh
      (my_env) C:\Users\melsy\Lab05\my_env\Scripts\library>python manage.py runserver
      Watching for file changes with StatReloader
      Performing system checks...

      System check identified no issues (0 silenced).
      June 20, 2023 - 10:28:23
      Django version 4.2.2, using settings 'library.settings'
      Starting development server at http://127.0.0.1:8000/
      Quit the server with CTRL-BREAK.
      ```
      <br/>

- Iniciando sesión y usando el sitio.

    - Se ingresa a la URL ``http://127.0.0.1:8000/admin`` con los datos de superusuario.

      <img src="img" style="width:70%"/><br/>
      <br/>

    - Se puede apreciar la siguiente página a continuación.

      <img src="img" style="width:70%"/><br/>
      <br/>

    - Añadimos libros en el library y observamos opciones.

      - Se hace click en ``add`` que se encuentra en ``Books`` y aparece lo siguiente.

        <img src="img" style="width:70%"/><br/>
        <br/>

      - Luego se apreta el botón ``+`` de ``Author`` para añadir nuevos autores o en ``Genre`` para añadir nuevos géneros. Por ejemplo añadimos ``Science Fiction``, ``Fantasy``, ``Western`` y ``French Poetry`` como lo hace en la guía, también aumentamos ``Romance`` luego damos en ``Save``.

        <img src="img" style="width:70%"/><br/>
        <br/>

      - Aquí se puede ver la lista de los géneros añadidos.

        <img src="img" style="width:70%"/><br/>
        <br/>

      - Luego añadimos libros para tenerlos en la aplicación ``Library``. Por ejemplo, el libro ``La máquina del tiempo``, primero añadimos al autor ``Herbert Wells``.

        <img src="img" style="width:70%"/><br/>
        <br/>

      - Después añadimos los datos faltantes y se guarda con ``Save and add other`` para añadir otro.

        <img src="img" style="width:70%"/><br/>
        <br/>

      - Repetimos el proceso con unos libros más (el último solo guardamos con ``Save``) y aquí se puede ver la lista de los libros añadidos.

        <img src="img" style="width:70%"/><br/>
        <br/>

      - Si damos click a un libro, por ejemplo ``El archivo de las tormentas``, este muestra el título y se puede editar, además salen botones para guardar y añadir otro, guardar y continuar editando, y guardar.

        <img src="img" style="width:70%"/><br/>
        <br/>

      - Además si se da click en ``history`` esto es lo que se verá a continuación.

        <img src="img" style="width:70%"/><br/>
        <br/>

      - Ahora se da click en ``home`` para regresar a la página principal, y podemos ver nuestras acciones.

        <img src="img" style="width:70%"/><br/>
        <br/>

    - Añadimos instancias de libros en el library y observamos opciones

      - Se hace click en ``Book instances``.

        <img src="img" style="width:70%"/><br/>
        <br/>

      - Para crear una nueva instancia, click en ``ADD BOOK INSTANCE`` y se añaden instancias de los libros.

        <img src="img" style="width:70%"/><br/>
        <br/>

      - Ejemplo de crear una instancia de un libro en mantenimiento.

        <img src="img" style="width:70%"/><br/>
        <br/>

      - Ejemplo de crear una instancia de un libro disponible.

        <img src="img" style="width:70%"/><br/>
        <br/>

      - Ejemplo de crear una instancia de un libro en calidad de prestamo.

        <img src="img" style="width:70%"/><br/>
        <br/>

      - Ejemplo de crear una instancia de un libro no disponible.

        <img src="img" style="width:70%"/><br/>
        <br/>

      - Finalmente, auí se puede ver todas las instancias de libros creadas.

        <img src="img" style="width:70%"/><br/>
        <br/>

- Configuraciones avanzadas

    - Registramos una clase ModelAdmin, colocando lo siguiente en el archivo ``admin.py`` de ``catalog``.

      ```py
      from django.contrib import admin
      from .models import Author, Genre, Book, BookInstance

      # admin.site.register(Book)
      # admin.site.register(Author)
      admin.site.register(Genre)
      # admin.site.register(BookInstance)

      # Define the admin class
      class AuthorAdmin(admin.ModelAdmin):
          pass

      # Register the admin class with the associated model
      admin.site.register(Author, AuthorAdmin)


      # Register the Admin classes for Book using the decorator
      @admin.register(Book)
      class BookAdmin(admin.ModelAdmin):
          pass

      # Register the Admin classes for BookInstance using the decorator
      @admin.register(BookInstance)
      class BookInstanceAdmin(admin.ModelAdmin):
          pass
      ```
      <br/>

    - Sin embargo, al estar ``pass`` vacío no cambiará nada en el comportamiento de administración, por lo que podemos configurar una vista de lista cambiando la clase ``AuthorAdmin``.
    
      - Se configura para mostrar apellido, nombre, nacimiento y fallecimiento.
        ```py
        class AuthorAdmin(admin.ModelAdmin):
            list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
        ```
        <br/>

      - Se ve en la lista de autores lo siguiente con el cambio de vista.

        <img src="img" style="width:70%"/><br/>
        <br/>
    
    - También se configura una vista para el modelo ``Book``, por lo que se cambia la clase ``BookAdmin``.

      - Se configura para mostrar el título, autor y genero

        ```py
        @admin.register(Book)
        class BookAdmin(admin.ModelAdmin):
            list_display = ('title', 'author', 'display_genre')
        ```
        <br/>

      - Por otro lado abrimos el archivo ``models.py`` de catalog para crear una cadena de texto de los primeros valores del campo ``genre`` con una ``short_description`` (descripción corta) usando las siguientes líneas dentro de la clase ``Book``.

        ```py
        def display_genre(self):
            return ', '.join([ genre.name for genre in self.genre.all()[:3] ])
        
        display_genre.short_description = 'Genre'
        ```
        <br/>

      - Se ve en la lista de libros con los cambios de vista.

        <img src="img" style="width:70%"/><br/>
        <br/>

    - Para añadir filtros de lista podemos ir nuevavamente al archivo ``admin.py`` y modificar la clase ``BookInstanceAdmin``
    
      - Se crean filtros con el atributo ``list_filter``.

        ```py
        @admin.register(BookInstance)
        class BookInstanceAdmin(admin.ModelAdmin):
            list_filter = ('status', 'due_back') # Se agregó esto
        ```
        <br/>

      - Se puede ver la lista de instancias de libros con un filtro en el lado derecho.

        <img src="img" style="width:70%"/><br/>
        <br/>

    - Para controlar que campos son desplegados en los autores, entonces continuamos en archivo ``admin.py`` y modificamos la clase ``AuthorAdmin``
    
      - Se añade la línea de ``fields`` para organizar que campos son desplegados.

        ```py
        class AuthorAdmin(admin.ModelAdmin):
            list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
            fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')] # Se agregó esto
        ```
        <br/>

      - Se puede ver la nueva vista de detalles de autor, al hacer click en uno de los autores.

        <img src="img" style="width:70%"/><br/>
        <br/>

    - También se puede añadir seccion en la lista de detalle, por ejemplo en las instancias de libros, modificamos la clase ``BookInstanceAdmin`` en el archivo ``admin.py``.
    
      - Se modifica la clase con ``fieldsets``.

        ```py
        @admin.register(BookInstance)
        class BookInstanceAdmin(admin.ModelAdmin):
            list_filter = ('status', 'due_back')

            # Se agregó lo siguiente
            fieldsets = (
                (None, {
                    'fields': ('book', 'imprint', 'id')
                }),
                ('Availability', {
                    'fields': ('status', 'due_back')
                }),
            )
        ```
        <br/>

      - Se puede ver la nueva vista de detalles de instancias de libros, al hacer click en uno de ellos.

        <img src="img" style="width:70%"/><br/>
        <br/>

    - Registros asociados a una instancia de libro, para ello también se modifica el archivo ``admin.py``.
    
      - Se añade la clase ``BooksInstanceInline`` y se agrega ``inlines`` en la clase ``BookAdmin``.

        ```py
        class BooksInstanceInline(admin.TabularInline):
            model = BookInstance

        @admin.register(Book)
        class BookAdmin(admin.ModelAdmin):
            list_display = ('title', 'author', 'display_genre')
            inlines = [BooksInstanceInline] # Se agregó esto
        ```
        <br/>

      - Se puede ver la nueva vista de detalles de un libro, y observas las instancias de libro asociados.

        <img src="img" style="width:70%"/><br/>
        <br/>

- (Desafío: Modificar BookInstance y Author) Modificar clase ``BookInstance`` para mostrar libros, estado, fecha de retorno e id y ``Author`` para mostrar la lista de sus libros

    - Se modifica la clase ``BookInstanceAdmin`` para agregar lo solicitado.
    
      - El resultado de la clase resultaria de la siguiente manera.

        ```py
        class BookInstanceAdmin(admin.ModelAdmin):
            list_display = ('book', 'status', 'due_back', 'id') # Se agregó esto
            list_filter = ('status', 'due_back')

            fieldsets = (
                (None, {
                    'fields': ('book', 'imprint', 'id')
                }),
                ('Availability', {
                    'fields': ('status', 'due_back')
                }),
            )
        ```
        <br/>

      - Se puede ver la nueva vista de las instancias de los libros.

        <img src="img" style="width:70%"/><br/>
        <br/>
    
    - Se modifica la clase ``AuthorAdmin`` del archivo ``admin.py``  y también se añade la clase ``BooksInline``.
    
      - El resultado de la clase resultaria de la siguiente manera.

        ```py
        class BooksInline(admin.TabularInline):
            model = Book

        class AuthorAdmin(admin.ModelAdmin):
            list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
            fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
            inlines = [BooksInline] # Se agregó esto
        ```
        <br/>

      - Se puede ver la nueva vista de Autor con lista de sus libros en la parte inferior.

        <img src="img" style="width:70%"/><br/>
        <br/>


***Part 5: Creating our home page***

- Creando la página principal.

    - URL mapping, para definir un patrón URL y una función vista (index) que será llamada si el patrón es detectado Entonces modificamos el archivo ``urls.py`` de ``catalog`` para que funcione y colocamos lo siguiente.

      ```py
      urlpatterns = [
          path('', views.index, name='index'),
      ]
      ```
      <br/>
    
    - Vista basada en funciones que procesan una consulta HTTP y genera una pagina HTML usando los datos colocados en la base de datos. Para crear esta vista modificamos el archivo ``views.py`` de ``catalog``.

      ```py
      from django.shortcuts import render
      from .models import Book, Author, BookInstance, Genre

      def index(request):

          # Extrae los registros usando objects.all()
          num_books = Book.objects.all().count()
          num_instances = BookInstance.objects.all().count()

          # Libros disponibles (status = 'a')
          num_instances_available = BookInstance.objects.filter(status__exact='a').count()
          
          num_authors = Author.objects.count()

          context = {
              'num_books': num_books,
              'num_instances': num_instances,
              'num_instances_available': num_instances_available,
              'num_authors': num_authors,
          }

          # Crea y retorna una página HTML
          return render(request, 'index.html', context=context)
      ```
      <br/>
    
    - Se crea las plantillas (``base_generic.html`` y ``index.html``) y la hoja de estilo ``styles.css``.

      - Se crea la plantilla ``base_generic.html`` dentro de ``catalog\templates\``.

        ```html
        <!DOCTYPE html>
        <html lang="en">

        <head>
            {% block title %}
            <title>Local Library</title>
            {% endblock %}
            <meta charset="utf-8" />
            <meta name="viewport" content="width=device-width, initial-scale=1" />
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet"
                integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous" />
            <!-- Add additional CSS in static file -->
            {% load static %}
            <link rel="stylesheet" href="{% static 'css/styles.css' %}" />
        </head>

        <body>
            <div class="container-fluid">
                <div class="row">
                    <div class="col-sm-2">
                        {% block sidebar %}
                        <ul class="sidebar-nav">
                            <li><a href="{% url 'index' %}">Home</a></li>
                            <li><a href="">All books</a></li>
                            <li><a href="">All authors</a></li>
                        </ul>
                        {% endblock %}
                    </div>
                    <div class="col-sm-10 ">{% block content %}{% endblock %}</div>
                </div>
            </div>
        </body>

        </html>
        ```
        <br/>

      - También se crea la hoja de estilo ``styles.css`` dentro de ``catalog\static\css\``.

        ```css
        .sidebar-nav {
            margin-top: 20px;
            padding: 0;
            list-style: none;
        }
        ```
        <br/>

      - Por último, la plantilla ``index.html`` dentro de ``catalog\templates``.

        ```html
        {% extends "base_generic.html" %}

        {% block content %}
        <h1>Local Library Home</h1>

        <p>Welcome to <em>LocalLibrary</em>, a very basic Django website developed as a tutorial example on the Mozilla Developer Network.</p>

        <h2>Dynamic content</h2>

        <p>The library has the following record counts:</p>
        <ul>
            <li><strong>Books:</strong> {{ num_books }}</li>
            <li><strong>Copies:</strong> {{ num_instances }}</li>
            <li><strong>Copies available:</strong> {{ num_instances_available }}</li>
            <li><strong>Authors:</strong> {{ num_authors }}</li>
        </ul>

        {% endblock %}
        ```
        <br/>

    - Ahora corremos el servidor para verificar posteriormente la página principal.

      ```sh
      (my_env) C:\Users\melsy\Lab05\my_env\Scripts\library>python manage.py runserver
      Watching for file changes with StatReloader
      Performing system checks...

      System check identified no issues (0 silenced).
      June 20, 2023 - 15:56:58
      Django version 4.2.2, using settings 'library.settings'
      Starting development server at http://127.0.0.1:8000/
      Quit the server with CTRL-BREAK.

      [20/Jun/2023 15:57:06] "GET /catalog/ HTTP/1.1" 200 1431
      [20/Jun/2023 15:57:06] "GET /static/css/styles.css HTTP/1.1" 200 80
      ```
      <br/>

    - Abrimos la página con la URL ``http://127.0.0.1:8000/``, la cual se redirige a ``http://127.0.0.1:8000/catalog/`` y observamos lo siguiente.

      <img src="img" style="width:70%"/><br/>
      <br/>

- (Desafío: Sobreescribir ``title block`` en ``index.html``) Modificar el bloque de título preestablecido por la plantilla ``base_generic.html`` en ``index.html``.

    - Se modifica el archivo ``index.html`` para sobreescribir el título, en este caso, el nuevo título es solo Library.
    
      - El resultado del archivo resultaria de la siguiente manera.

        ```html
        {% extends "base_generic.html" %}

        # Se añade las siguientes tres líneas para sobreescribir título
        {% block title %}
            <title>Library</title> 
        {% endblock %}

        {% block content %}
        <h1>Local Library Home</h1>

        <p>Welcome to <em>LocalLibrary</em>, a very basic Django website developed as a tutorial example on the Mozilla Developer Network.</p>

        <h2>Dynamic content</h2>

        <p>The library has the following record counts:</p>
        <ul>
            <li><strong>Books:</strong> {{ num_books }}</li>
            <li><strong>Copies:</strong> {{ num_instances }}</li>
            <li><strong>Copies available:</strong> {{ num_instances_available }}</li>
            <li><strong>Authors:</strong> {{ num_authors }}</li>
        </ul>

        {% endblock %}
        ```
        <br/>

      - La página principal con su nuevo título se vería de la siguiente forma.

        <img src="img" style="width:70%"/><br/>
        <br/>

***Part 6: Generic list and detail views***

- Definiendo los modelos del Library.

    - Modelo Genre, se crea la clase ``Genre`` que representa un género literario.

      ```py
      class Genre(models.Model):
          name = models.CharField(max_length=200, help_text='Enter a book genre (e.g. Science Fiction)')

          def __str__(self):
              return self.name
      ```
      <br/>


***Part 7: Sessions framework***

- Definiendo los modelos del Library.

    - Modelo Genre, se crea la clase ``Genre`` que representa un género literario.

      ```py
      class Genre(models.Model):
          name = models.CharField(max_length=200, help_text='Enter a book genre (e.g. Science Fiction)')

          def __str__(self):
              return self.name
      ```
      <br/>

***Part 8: User authentication and permissions***

- Definiendo los modelos del Library.

    - Modelo Genre, se crea la clase ``Genre`` que representa un género literario.

      ```py
      class Genre(models.Model):
          name = models.CharField(max_length=200, help_text='Enter a book genre (e.g. Science Fiction)')

          def __str__(self):
              return self.name
      ```
      <br/>


***Part 9: Working with forms***

- Definiendo los modelos del Library.

    - Modelo Genre, se crea la clase ``Genre`` que representa un género literario.

      ```py
      class Genre(models.Model):
          name = models.CharField(max_length=200, help_text='Enter a book genre (e.g. Science Fiction)')

          def __str__(self):
              return self.name
      ```
      <br/>

***Part 10: Testing a Django web application***

- Definiendo los modelos del Library.

    - Modelo Genre, se crea la clase ``Genre`` que representa un género literario.

      ```py
      class Genre(models.Model):
          name = models.CharField(max_length=200, help_text='Enter a book genre (e.g. Science Fiction)')

          def __str__(self):
              return self.name
      ```
      <br/>


***Part 11: Deploying Django to production***

- Definiendo los modelos del Library.

    - Modelo Genre, se crea la clase ``Genre`` que representa un género literario.

      ```py
      class Genre(models.Model):
          name = models.CharField(max_length=200, help_text='Enter a book genre (e.g. Science Fiction)')

          def __str__(self):
              return self.name
      ```
      <br/>



##
## COMMITS MÁS IMPORTANTES

<br/>

<img src="commits" style="width:70%"/><br/><br/>

##
## CUESTIONARIO

- **Resalte un aprendizaje que adquiri ́o al momento de estudiar Django.**

  respuesta

<br/>
<br/>

##
## REFERENCIAS

- https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Tutorial_local_library_website
- https://github.com/mdn/django-locallibrary-tutorial
- https://github.com/rescobedoq/pw2/tree/main/labs/lab05