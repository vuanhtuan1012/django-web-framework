# Django Web Framework  <!-- omit in toc -->

Comprehensive notes covering key concepts of the [Django Web Framework](https://www.coursera.org/learn/django-web-framework) course.

- [Introduction to Django](#introduction-to-django)
  - [Hyper Text Markup Language (HTML) vs. HTML5](#hyper-text-markup-language-html-vs-html5)
  - [Vitual Environment](#vitual-environment)
  - [Django Project Structure](#django-project-structure)
    - [Don't Repeat Yourself (DRY) Principle](#dont-repeat-yourself-dry-principle)
    - [What is a project?](#what-is-a-project)
    - [Project package](#project-package)
    - [Object-Relational Mapping (ORM)](#object-relational-mapping-orm)
    - [Web Server Gateway Interface (WSGI)](#web-server-gateway-interface-wsgi)
    - [Asynchronous Server Gateway Interface (ASGI)](#asynchronous-server-gateway-interface-asgi)
    - [Synchronous vs. Asynchronous Web Apps](#synchronous-vs-asynchronous-web-apps)
    - [Concurrency vs. Parallelism](#concurrency-vs-parallelism)
  - [Django-admin vs. `manage.py` commands](#django-admin-vs-managepy-commands)
  - [App structure](#app-structure)
  - [Web Framework](#web-framework)
    - [Three-tier Architecture](#three-tier-architecture)
    - [Model-View-Control (MVC) Architecture](#model-view-control-mvc-architecture)
    - [Model-View-Template (MVT) Architecture](#model-view-template-mvt-architecture)
- [Views](#views)
  - [Class-Based Views](#class-based-views)
  - [Function-Based Views vs. Class-Based Views](#function-based-views-vs-class-based-views)
  - [HyperText Transfer Protocol (HTTP)](#hypertext-transfer-protocol-http)
    - [HTTP Request](#http-request)
    - [HTTP Response](#http-response)
    - [HTTP Methods](#http-methods)
    - [HTTP Versions](#http-versions)
    - [HOL Blocking](#hol-blocking)
    - [HTTP Status Codes](#http-status-codes)
    - [HTTP Secure (HTTPS)](#http-secure-https)
  - [Request and Response Objects](#request-and-response-objects)
    - [HttpRequest Object](#httprequest-object)
    - [HttpResponse Object](#httpresponse-object)
  - [Understanding URLs](#understanding-urls)
  - [Parameters](#parameters)
    - [Path Parameter](#path-parameter)
    - [Path Converters](#path-converters)
    - [Query Parameter](#query-parameter)
    - [Body Parameter](#body-parameter)
  - [URL Dispatcher](#url-dispatcher)
    - [URL Mapping](#url-mapping)
    - [Regular Expressions in URLs](#regular-expressions-in-urls)
    - [URL Pattern Convention](#url-pattern-convention)
    - [URL Namespacing](#url-namespacing)
    - [`reverse` Function](#reverse-function)
  - [Error Handling](#error-handling)
  - [Method Resolution Order (MRO)](#method-resolution-order-mro)
  - [Naming Convention](#naming-convention)
- [Models](#models)
  - [Field Types](#field-types)
  - [Model Relationships](#model-relationships)
  - [Migrations](#migrations)
  - [Django ORM (Object Relationship Mapping)](#django-orm-object-relationship-mapping)
    - [Manager](#manager)
    - [QuerySet](#queryset)
    - [CRUD Operations](#crud-operations)
  - [Common Problems](#common-problems)
    - [N+1 Problem](#n1-problem)
    - [Sequential Scan (Seq Scan) Problem](#sequential-scan-seq-scan-problem)
    - [Fetching Too Many Columns Problem](#fetching-too-many-columns-problem)
    - [Too many JOINs Problem](#too-many-joins-problem)
  - [Django Form](#django-form)
    - [Form Fields](#form-fields)
    - [Form Rendering](#form-rendering)
    - [Reading From Contents](#reading-from-contents)
    - [Cross-Site Request Forgery (CSRF) Attack](#cross-site-request-forgery-csrf-attack)
  - [Django Admin](#django-admin)
    - [Customizing User Admin](#customizing-user-admin)
    - [Customizing Model Admin](#customizing-model-admin)
    - [Permissions](#permissions)
    - [Enforcing Permissions](#enforcing-permissions)
  - [Database Configuration](#database-configuration)
    - [Setup Steps](#setup-steps)
    - [Environment Variables vs. Configuration Files](#environment-variables-vs-configuration-files)
- [Templates](#templates)


## Introduction to Django

### Hyper Text Markup Language (HTML) vs. HTML5

- **HTML** (Hyper Text Markup Language) is the **standard language for structuring** web pages.
- **HTML5** is the **newest version** of HTML, adding modern features for today's web.
- **Key differences:**
  - HTML5 **introduced semantic tags** *such as* `<header>`, `<footer>`, `<nav>`, `<section>`, `<article>`, `<aside>`, so browsers and developers understand page structure better, improve code readability. Since these tags have **built-in meaning,** they tell the browser (and developers, screen renders, search engines) **what the content represents.**
    - `<header>` $\rightarrow$ top of a page or section.
    - `<nav>` $\rightarrow$ navigation menu.
    - `<article>` $\rightarrow$ self-contained content (blog post, news article, post).
    - `<section>` $\rightarrow$ logical grouping of related content.
    - `<aside>` $\rightarrow$ sidebar or related info.
    - `<footer>` $\rightarrow$ bottom of a page or section.
  - HTML **uses mostly** `<div>` for layout. It has **no meaning** by default.
    - is just a **generic container.**
    - used mainly for grouping elements for styling or scripting.
    - does not describe the purpose of its content.
  - HTML5 introduces **new form inputs,** *such as* `email`, `date`, `number`, `range`, `color` and **new attributes** *such as* `placeholder`, `required`, `pattern`, `autofocus`.
  - HTML5 **adds client-side storage** like `localStorage`, `sessionStorage`, `IndexedDB`, application cache / service workers while HTML had only cookies.
  - HTML5 **supports multimedia** without plugins like Flash.
  - HTML5 adds `<canvas>` for **drawing graphics** and animations and improves SVG support.

### Vitual Environment

Python **recommends using a virtual environment to build** Python applications.

A virtual environment is an **isolated environment** having its copy of the interpreter and libraries so that there's **no clash** with the global installation of Python.

Python's virtual environment is set-up with the help of a built-in module named `venv`.

### Django Project Structure

- In Django,
  - **a project** represents the **entire web application.**
  - **an app** is a **sub-module of a project.**
- An **app** is typically used to implement functionality for some specific purpose.
  - **apps can be self-contained,** meaning they do not rely on other apps to function.
  - **apps can be used or reused** in may different projects. This leads nicely to the **[DRY principle](#dont-repeat-yourself-dry-principle).**
  - an **app should be feature targeted,** and it's best suited for one and only one thing.
- In bref, **a Django web application is a project that contains many apps.**

#### Don't Repeat Yourself (DRY) Principle

The DRY principle stands for **Don't Repeat Yourself.** It's a fundamental guideline in software development that says:

> Every piece of knowledge should have a **single, unambiguous, authoritative** representation within a system.

In simple terms, it **prevents duplicating code, logic, or data.**

- The DRY principle leads to less maintenance, fewer bugs, and better readability.
- The DRY principle applies to coding and refactoring, database schema design, API design, infrastructure/configuration, and documentation.

#### What is a project?

- A Django project **is a Python package containing** the database configuration used by various sub-modules (apps) and other Django-specific settings.
- The `startproject` command of Django-admin is used to **create a new Django project.** It creates the folder of the given name (is called *project directory*), inside which there is another folder of the same name (is called *project package*) and the script `manage.py`.

  ```cmd
  > django-admin startproject <project_name>
  ```
  - **Project directory** is created when we create a Django project. It contains `manage.py` and *project package folder.*
  - **Project package** contains a `settings.py` file and other files.
- The `manage.py` script **has the same role as** the `django-admin` utility. It can perform everything that the `django-admin` utility does. However, using `manage.py` is **more straightforward,** especially if we are required to work on a single project.
- The `startapp` command is used to create a new app. An app is also represented by a folder of a specific file system.
  ```cmd
  > python manage.py startapp <app_name>
  ```
- Django manages the database operations with the **[ORM technique](#object-relational-mapping-orm).**
- [Migration](#migrations) refers to **generating a database table whose** structure matches the data model declared in the app.
  ```cmd
  > python manage.py makemigration
  ```
- The `migrate` command **synchronizes the database state** with the currently declared models and migrations.
  ```cmd
  > python manage.py migrate
  ```
- The `runserver` command **starts** Django's built-in **development server** on the local machine.
  ```cmd
  > python manage.py runserver
  ```

#### Project package

When a project is created, the inner folder with (the same project name) is a Python package. The `startproject` template places 4 more files in the package folder.

> *For a folder to be recognized by Python as a package, it must have a file `__init__.py`.*

- `settings.py` contains **configuration settings** for the Django project, including the `INSTALLED_APPS` list where newly created apps must be added.
- `urls.py` defines the **URL patterns** for both the project and the app, **routing requests** to the appropriate view functions. Every time the client **browser requests a URL,** the Django server looks to **match its pattern** and **routes the application to the mapped view.**
- `asgi.py` is used by the application servers following the [ASGI](#asynchronous-server-gateway-interface-asgi) standard to **serve asynchronous web applications.**
- `wsgi.py` is the **entry point for** such **[WSGI](#web-server-gateway-interface-wsgi)-compatible servers** to serve classical web application.

#### Object-Relational Mapping (ORM)

**ORM** stands for **Object-Relational Mapping.** It's a programming techinque used to **interact with a relational database** (like PostgreSQL, MySQL, or SQLite) **using objects** in a programming language **instead of writing raw SQL queries.**

ORM **automatically maps:**
- Database tables $\rightarrow$ Classes.
- Rows $\rightarrow$ Objects.
- Columns $\rightarrow$ Object attributes.

The ORM internally generates and run the SQL.

**Benefits** of ORM:
- **Less SQL.** We work mainly with our language's objects, not manual SQL strings.
- **Faster development.** CRUD operations are simplified.
- **Database independence.** Most ORMs work with many database engines.
- **Security.** ORMs help prevent SQL injection by parameterizing queries.
- **Maintainable code.** Models and relationships are clean and structured.

**Donwsides** of ORM:
- **Can be slower** than optimized SQL queries.
- May **hide what queries are** actually being executed.
- Complex queries **sometimes require raw SQL** anyway.

#### Web Server Gateway Interface (WSGI)

**WSGI** stands for **Web Server Gateway Interface.** It's a Python web standard (**specification**) that **defines how** Python **web applications communicate with web servers.**

**Before WSGI,** *every framework and server had its own protocol,* nothing was compatible. WSGI unified everything. It **allows any WSGI-compatible framework** (*Flask, Django <=2.1, Pyramid*) to **run on any WSGI-compatible server** (*Gunicorn, uWSGI, mod_wsgi*).

WSGI is **synchronous** and **designed for traditional** HTTP request/response cycles: no async, no WebSockets, no long-lived connections.

A **WSGI server** is a program that *implements the WSGI specification* and *runs a Python WSGI application.* It handles:
- receiving HTTP requests from clients.
- passing them to the Python application via the WSGI interface.
- returning the responses to the client.

#### Asynchronous Server Gateway Interface (ASGI)

**ASGI** stands for **Asynchronous Server Gateway Interface.** It's also a Python web standard that defines how web servers comunicate with Python applications, similar to WSGI, but **designed for async use cases.**

**Mordern apps need** WebSockets, long-runing connections, non-blocking async I/O, [concurrency](#concurrency-vs-parallelism) without threads, so ASGI was created to **support both synchronous and asynchronous Python code,** including real-time features.

**ASGI is a specification,** not code. It **defines a common interface** between ASGI servers (*e.g.,* Uvicorn) and ASGI applications (*e.g.,* FastAPI, Django 3+).

An **ASGI server** is a program that *implements the ASGI specification* and *runs ASGI-compatible Python app.*

**ASGI is** the **modern Python web standard** for async apps.
- It **supports both** synchronous and asynchronous code.
- It **enables** WebSockets, streaming, and high [concurrency](#concurrency-vs-parallelism).

#### Synchronous vs. Asynchronous Web Apps

- A **synchronous** web app **handles one request at a time** per worker, following a simple *request $\rightarrow$ process $\rightarrow$ response* pattern. Its characteristics:
  - **Blocking I/O:** while a request is being processed, the worker can't handle another.
  - **Thread/process based concurrency:** to handle more users, it needs to add more worker processes or threads.
  - **Straightforward code:** no `async`/`await`.
  - Great for CPU-bound or simple I/O-bound actions.
- An **asynchronous** web app **handles requests using an event loop,** allowing a single worker to server thousands of connections without blocking. Its characteristics:
  - **Non-blocking I/O:** tasks pause with `await` while waiting *such as* Database I/O, HTTP calls, File system I/O, WebSockets.
  - **Concurrency through** `async`/`await`, not threads.
  - **Ideal for high-scale** or real-time applications.
- Async **shines when** we have **lots of waiting,** not lots of computing.

#### Concurrency vs. Parallelism

- **Simple definition:**
  - **Concurrency** = doing many things **seemingly** at the same time.
    - Tasks **overlap in time.**
    - A single worker switches between tasks.
    - Like multitasking.
  - **Parallelism** = doing many things **exactly** at the same time.
    - Tasks run **at the same instant.**
    - Requires multiple CPU cores, multiple workers.
- **Technical definition:**
  - **Concurrency:** multiple tasks make progress **during overlapping time periods.**
    - does **not require** multiple cores.
    - achieved through: `async`/`await` (event loop), coroutines, cooperative multitasking, context switching.
  - **Parallelism:** multiple tasks execute **at exactly the same moment.**
    - **requires** multiple CPU cores, multiple processes, CPU parallelism.
- **In Python:**
  - **Concurrency** helps with **I/O-bound tasks** like web requests, database calls, file reads, sleep timers. Examples:
    - `asyncio` (single-thread event loop),
    - threading (even though GIL limits CPU parallelism),
    - non-blocking I/O.
  - **Parallelism** helps with **CPU-bound tasks** like heavy computations, machine learning workloads, image processing, compression/encryption. Examples:
    - `multiprocessing`,
    - C-extension parallel code,
    - NumPy operations (internally parallel).

### Django-admin vs. `manage.py` commands

- Both can be used to **perform the same tasks,** but there are **some subtle differences,** and the choice of usage will depend on how we want to work on project.
- `django-admin` is Django's **command line utility** for administrative tasks. This utility is present **in the scripts folder** of the Django **environment directory.** Django admin utility is executed from inside the terminal.

  *It can also be launched via the call of module* `python -m django`.

- `manage.py` is a script that is the **local version** of Django admin and is located **inside the project folder.** It **sets** the Django settings module environment variable so that it **points to** our project `settings.py` file.
- `manage.py` is a file that **is automatically created** each time we create a Django project, it is **specific to** the virtual environment **of the project.**
- When working on a **single Django project,** developers tend to **use** `manage.py`.
- However, if we need to switch between **multiple Django settings files,** use the **Django admin command** with Django settings module or the settings command line option.

> `manage.py` is more convenient to use than `django-admin`. It runs inside the project folder. When using `django-admin`, you must set `--settings` variable to the required project's `settings.py` file.

### App structure

- An app is **responsible for performing one single task** out of the many involved in the complete web application, represented by the Django project.
- The `startapp` command option of the `manage.py` script creates a default folder structure for the app of that name.

  ```cmd
  > python manage.py startapp <app_name>
  ```
- The folder structure looks like this
  ```
  demoproject
  │   db.sqlite3
  │   manage.py
  │
  ├───demoapp
  │   │   admin.py
  │   │   apps.py
  │   │   models.py
  │   │   tests.py
  │   │   views.py
  │   │   __init__.py
  │   │
  │   └───migrations
  │           __init__.py
  │
  └───demoproject
      │   asgi.py
      │   settings.py
      │   urls.py
      │   wsgi.py
      │   __init__.py
  ```
- `views.py`

  **A [view](#views)** is a **user-defined function** that's **called** when Django's **[URL dispatcher](#url-dispatcher) identifies** the client's request URL and **matches** it with a URL pattern defined in the `urls.py` file.
- `models.py`. The **data models required** for processing in the app **are created** in this file.

  **A data [model](#models)** is a Python **class based on** `django.db.models` class. All the models present here **are migrated** to the database tables.

### Web Framework

- Frameworks are **designed to support** the developer in building the web application.
- **The purpose** of a web framework is to make application **development easier** and to **provide** the developer with a **clean structure** that keeps things in order and allows for changes and modifications.
- Frameworks also allow for **code reusability** facilitated by existing code. They **provide a solid foundation** on which to build web application.
- A web application is split into two parts:
  - **Front-end** is the part of the website that the **user interacts with** via web browser.
  - **Back-end** is the part that **runs on a web server** and usually contains a database.

#### Three-tier Architecture

- Architecture refers to the fundamental structures of a software system.
- Three-tier architecture is a modular based approach to client-server architecture that splits the application into three logical parts:
  - the **presentation tier** is the **layer the users primarily interact with** through user interfaces from their desktop, laptop, or mobile devices. It's **commonly built with a UI framework** or library *such as* React, and it **communicates** with other tiers **by sending results through** the application interface.
  - the **data tier** usually **consists of database servers** for storing and retrieving information.
  - the **application tier** is what **ties** together the other **two tiers.** It **gets data** from the presentation layer and **persists** it in the data tier.

#### Model-View-Control (MVC) Architecture

- Most of the web frameworks implement the **MVC (Model-View-Control)** architecture.
- The MVC design pattern separates the entire web application development process into three layers: Model, View, and Controller.
  - The **Controller** intercepts the user requests. It **coordinates** with the View and Model layers to **send the appropriate response** back to the client.
  - The **Model** is responsible for **data definitions, processing logic** and **interaction** with the backend database.
  - The **View** is the **representation layer** of the application. It **takes care** of the **placement and formatting** of the result and **sends** it to the Controller, which in turn, redirects it to the client as the application's response.

#### Model-View-Template (MVT) Architecture

- The Django framework adapts a **Model-View-Template (MVT)** approach, a slight variation of the MVC approach.
- A Django application consists of four following components:
  - **URL Dispatcher** is the **entry point** that decides which part of the application handles the request. The `urls.py` module acts as the dispatcher. It **defines** the **URL patterns.** Each URL pattern is **mapped with a view function.**

    When the server receives a request in the client URL, the dispatcher matches its pattern with the patterns available in the `urls.py` module.

    It then routes the flow of the application toward its associated view.
  - The **View** function **reads** the path, query, and body parameters **included in** the client's request. It **uses** the client's and the model's data and **renders** its response using a template.

    *If required,* it uses this data to interact with the models to perform CRUD operations.

    > Django's View layer performs the **role of Controller** in MVC architecture.
  - A **Model** is a Python class. An app may have one or more model classes, conventionally put in the `models.py` file.

    Django **migrates the attributes** of the model class **to construct a database table** of a matching structure.

    [Django's ORM (Object Relational Mapper)](#django-orm-object-relationship-mapping) helps perform [CRUD operations](#crud-operations) in an object-oriented way instead of invoking SQL queries.
  - A **Template** is a web page **containing a mix of** static HTML and Django Template Language code blocks. It is **equivalent to the View** in the MVC architecture.

    Django's **template processor uses** any context data from the view inserted in these blocks to **formulate** a dynamic response.


## Views

- The **primary role** of a view function is to **fetch the data** from the client's request, **apply** the necessary processing logic, and **return an appropriate response** to the client.

  > A view function is a Python function that handles a web request and returns a web response.

- It **receives** the request as an `HttpRequest` object, and **returns** an `HttpResponse` object containing the response body, status code, and any relevant headers.
- View functions **often:**
  - handle GET/POST requests,
  - validate forms,
  - query models,
  - redirect users,
  - return JSON (for APIs).
- **Best practice:** view functions are placed in the application's `views.py` module.

  *For example:*

  ```python
  # views.py
  from django.shortcuts import render
  from django.http import HttpResponse, HttpRequest


  def home(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Hello World!")


  def welcome(request: HttpRequest) -> HttpResponse:
    context = {"name": "Alice"}
    return render(request, "welcome.html", context)
  ```

- View functions need to [be mapped to specific URLs](#url-dispatcher), ensuring that Django calls the appropriate view when a request targets that URL.

### Class-Based Views

- Class-based views are **views written as classes,** instead of functions (*function-based views*).
- Class-based views **repond** to HTTP requests using class **instance methods:** `get`, `post`, `put`, `delete`, `patch`.

  *For example:*

  ```python
  # views.py
  from django.views import View
  from django.http import HttpRequest, HttpResponse


  class HomeView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
      return HttpResponse("Response to GET request")

    def post(self, request: HttpRequest) -> HttpResponse:
      return HttpResponse("Response to POST request")
  ```
- They allow to **structure view logic** in an **object-oriented way,** making code more **reusable, organized,** and **extensible.**
  - **code reusability:** we can **create base classes** and let other views **inherit** behavior.
  - **cleaner** and **orgnized code:** logic is **grouped into class methods** instead of long function-based views.
  - **extensiblity:** we can override just the parts we need.
- Django provides many **built-in generic views** in the `django.views.generic` module, *such as:*
  - `ListView`: displays a list of objects.
  - `DetailView`: displays details of a single object.
  - `CreateView`: creates a new object.
  - `UpdateView`: updates an existing object.
  - `DeleteView`: deletes an object.
  - `TemplateView`: renders a template.

  These class-based views **simplify the process** of declaring view patterns **and reduce** the amount of boilerplate code we need to write. *For example:*

  ```python
  # views.py
  from django.views.generic import ListView

  from .models import Book


  class BookListView(ListView):
    model = Book
    template_name = "book_list.html"
    context_object_name = "books"
  ```
- Class-based views **allow** inheritance and **mixins.**
  - A mixin is a class **designed to be inherited alongside another** class to **add extra features,** but **not mean to stand alone.**
  - Mixins are **reusable,** contain **small, focused logic,** allow to **combine behaviors** cleanly.
  - When using mixins, always **place** them **before** the view class so that Python's **MRO (Method Resolution Order)** to find the mixin methods first. *For example:*

    ```python
    # views.py
    from django.views.generic import TemplateView


    class TitleMixin:
      title = ""

      def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = self.title
        return context


    class HomeView(TitleMixin, TemplateView):
      template_view = "home.html"
      title = "Home Page"
    ```

### Function-Based Views vs. Class-Based Views

- **The choice** of function-based views and class-based view **depends on** complexity, reusability, and clarity.
  - if the view is **simple** $\rightarrow$ use function-based views.
  - if the view is **complex or reusable** $\rightarrow$ use class-based views.
- **Use function-based views when:**
  - **simple view:** returns a template, handles one request method, has straightforward behavior.
  - no need for inheritance, need **maximum transparency and control.**
  - the view is **small and not reused.**
  - prefer **direct control.**
- **Use class-based views when:**
  - need to **handle multiple HTTP methods** cleanly.
  - want to **reuse or extend** behavior.
  - **using generic views** *such as* `ListView`, `DetailView`, `CreateView`, `UpdateView`, `DeleteView`, `FormView`.
  - need **cleaner, structured** code. Class-based views break behavior into clear override-able methods.
  - **need mixins:** authentication, permissions, etc.

### HyperText Transfer Protocol (HTTP)

- HTTP stands for **HyperText Transfer Protocol.**
- HTTP is **a core operational protocol** of the world wide web. It **enables** a web browser to **comunicate** with a web server.
- HTTP is a **request-response** based protocol. It works with a **client -> request -> server -> response** cycle.
  - A client (web browser) sends the **HTTP request** to a server.
  - The web server sends the **HTTP response** back to the browser.
- HTTP is **used for almost all communication on the web,** including: loading web pages, APIs and webservices, file transfers, form submissions, and so on.
- It's a **stateless protocol.**
  - Each HTTP **request is independent.**
  - Servers do **not remember past requests** unless cookies or sessions are used.

#### HTTP Request

An example of a HTTP request:

  ```text
  GET / HTTP/1.1
  Host: developer.mozilla.org
  Accept-Language: en
  ```

A HTTP request **consists of:**
- a **[method](#http-methods),** *e.g.,* `GET`
- a **path** (*resource location*), *e.g.,* `/`
- a **[version](#http-versions),** *e.g.,* `HTTP/1.1`
- **headers** *contain additional information* about the request and the client that is making the request. Headers can contain information **such as** the server name, the server port, the request method type, and the content type. **The content** of the header can **depend on** the specific client and server. *For example:*

  ```text
  Host: developer.mozilla.org
  Accept-Language: en
  ```
- and **optional body** of content that the client is sending (for certain request methods like `POST`, `PUT`).

#### HTTP Response

- HTTP responses **follow a format similar** to the request format.

  ```text
  HTTP/1.1 200 OK
  Date: Sat, 09 Oct 2010 14:28:02 GMT
  Server: Apache
  Last-Modified: Tue, 01 Dec 2009 20:18:22 GMT
  ETag: "51142bc1-7449-479b075b289I1b"
  Accept-Ranges: bytes
  Content-Length: 29769
  Content-Type: text/html
  ```

- Following the header, the response will **optionally contain a message body** consisting of the response content, *such as* the HTML document, the image file, and so forth.

  ```html
  <html>
    <body>
      <p>Hello world!</p>
    </body>
  </html>
  ```

- **[HTTP status code](#http-status-codes),** *e.g.,* `200`, contained **within the header indicate** if the HTTP request successfully completed. The code values are in the range of 100-599 and are grouped by purpose.
- The **status message,** *e.g.,* `OK`, is a text representation of the status code.

#### HTTP Methods

- HTTP mehod describes the **type of action** that client wants to perform and **comunicates** it to the server.
- The primary or the **most commonly used** HTTP methods are: `GET`, `POST`, `PUT`, `PATCH`, and `DELETE`.
- `GET` method:
  - is used to **retrieve information** from the given server.
  - is **safe.** It does *not change* server data.
  - is **idempotent.** The *same request* yields the *same result.*
  - data is **sent in the URL** (*query string*).
  - should **not be used** for **sensitive** data.

  *For example:* the following request **retrieves** user with id `5`.

    ```text
    GET /users/5
    ```
- `POST` method:
  - is used to **create new data** on the server.
  - is **NOT idempotent.** Sending a same request twice may create duplicates.
  - data is **sent** in the **body.**
  - is **used for** new submissions, uploads, form data.

  *For example:* the following request **creates** a new user.

    ```text
    POST /users
    {
      "name": "John"
    }
    ```
- `PUT` method:
  - is used to **fully update** an existing resource.
  - is **idempotent.** The *same request* yields the *same result.*
  - **replaces** the **entire resource unless** implemented otherwise.
  - must include the **full updated data.** If *any field is missing,* it may be overwritten or remove.

  *For example:* the following request **replaces** user with id `5` with the provided data.

    ```text
    PUT /users/5
    {
      "name": "John",
      "age": 25
    }
    ```
- `PATCH` method:
  - is used to **partially update** the resource. It tells the server to *update only* the provided fields.
  - is **idempotent.** The *same request* yields the *same result.*

  *For example:* the following request **updates only** the `age` of the user with id `5`.

    ```text
    PATCH /users/5
    {
      "age": 25
    }
    ```
- `DELETE` method:
  - is used to **remove a resource.**
  - is **idempotent.** Deleting the *same item repeatedly* gives the *same result.*
  - **removes data** from the server.

  *For example:* the following request **deletes** the user with id `5`.

  ```text
    DELTE /users/5
  ```

> **Note** that HTTP methods are **only conventions,** not enforcement. The developer's **code determines** whether the operation is actually **idempotent.**

#### HTTP Versions

The three most commonly used HTTP versions are `HTTP/1.1`, `HTTP/2`, and `HTTP/3`.

- `HTTP/1.1`
  - **text-based** protocol. It means **messages** are written in **human-readable** plain text.
  - **one request** per TCP connection (unless using `keep-alive`).
  - if one request is **delayed,** others are blocked due to **[HOL](#hol-blocking)** (*Head-of-Line*) **blocking.** Browsers open many parallel TCP connections to compensate.
  - **pros:**
    - simple, widely supported.
    - **works everywhere,** even on very old systems.
  - **cons:**
    - **significant latency** with many small resources (*e.g.,* 100+ assets per page).
    - inefficient for modern web workloads.
- `HTTP/2`
  - **binary framing** layer. It means the protocol **uses structured binary data frames** (*machine-readable packages*) instead of text. It's **more compact** than text and is **faster** to parse.
  - **multiplexing:** multiple simultaneous streams over a single TCP connection.
  - **header compression** (HPACK): smaller request $\rightarrow$ faster transfers.
  - stream prioritization.
  - **faster** than HTTP/1.1 **when** network quality is good.
  - **still suffers** from TCP-level [HOL blocking](#hol-blocking):
    - if packets are lost, the **entire connection stalls.**
    - **multiplexing doesn't help** because they share one TCP connection.
  - **pros:**
    - low latency.
    - more efficient for complex sites.
    - widespread support.
  - **cons:**
    - performance **drops significantly** on mobile or unstable networks.
- `HTTP/3`
  - **binary framing** layer.
  - runs over **QUIC,** which is built on **UDP** instead of TCP.
  - **QUIC** includes:
    - built-in **TLS 1.3** encryption.
    - stream-level flow control.
    - **connection migration.** Keep connection **alive when IP changes,** helpful for mobile.
  - no TCP HOL blocking $\rightarrow$ **stream are independent.**
  - **faster connection setup:**
    - no separate TCP + TLS handshake.
    - often **0-RTT** (zero round-trip time) **startup.**
  - handles packet loss gracefully.
  - **pros:**
    - **best** for modern mobile networks.
    - **extremely fast** in high-latency environments.
    - **robust when switching** networks, *e.g.,* Wi-Fi $\rightarrow$ mobile data.
  - **cons:**
    - **still rolling out** globally.
    - firewalls and enterprise networks sometimes **block UDP.**

#### HOL Blocking

- HOL blocking stands for **Head-Of-Line Blocking.**
- It is **a performance problem** that occurs in network protocols when **one slow** or lost packet **blocks all the packets behind** it, even if those later packets could otherwise have been processed.
- In `HTTP/1.1`
  - each TCP connection handles **one request at a time.**
  - if **one request is slow,** every request behind it in that connection **waits.**
  - browsers open many parallel connections to reduce this problem.
- In `HTTP/2`
  - **supports multiplexing,** multiple streams on one connection.
  - **still uses TCP,** which has packet-level HOL blocking:
    - if **one TCP packet is lost,** TCP must wait and retransmit it.
    - **all HTTP/2 streams** on that connection **pause until** the packet is recovered.
- In `HTTP/3`
  - **No** TCP HOL blocking.
  - uses **QUIC, built on UDP,** handles **streams independently.**
  - if **one packet is lost:**
    - only the **affected streams waits.**
    - all **other streams continue** normally.
- HOL blocking **makes website slower** because:
  - a **single lost** packet **affects all streams,** requests behind it.
  - **high-latency** or mobile networks suffer more.
  - **performance degrades** for real-time or resource-heavy website.
- **TCP has HOL blocking** because:
  - TCP **enforces strict, in-order delivery.**
  - **treats the connection as one** continuous byte stream.
  - if one packet is lost $\rightarrow$ whole connection halts.
- **QUIC solves** TCP's connection-wide **HOL blocking problem:**
  - built-on UDP $\rightarrow$ QUIC **controls** ordering + reliability **itself.**
  - multiple **independent streams** inside one connection.
  - packet loss **affects only** the stream involved.

#### HTTP Status Codes

- HTTP status codes are **three-digit numbers** that a web **server sends** back **in** an **HTTP response** to **tell the client** (browser, app, API, etc.) **what happened** to its request.
- They are grouped into **five categories,** each representing a different class of response.
- **1xx - Informational** indicates that the request **was received** and is **still being process.** The **most common informational responses** are:
  - **100 Continue:** server acknowledges request headers, client can send body.
  - **101 Switching Protocols:** server is switching protocols, *e.g.,* to WebSocket.
  - **102 Processing:** server **is working** but not finished. It's **not a final** response, it's **sent before** the final status code to **prevent** the client from **timing out** while the server is doing something that takes a long time, *e.g.,* large file operations, deep searches, etc.
- **2xx - Success** indicates that the request **was successfully processed** by the server. The **most common success responses** are:
  - **200 OK:** standard success response.
  - **201 Created:** a new resource was created, *e.g.,* after `POST`.
  - **202 Accepted:** the server **acccepted the request,** but **has not processed** it yet and **may process it later.** It's often used in APIs, **for asynchronous processing** (background jobs).
  - **204 No Content:** success, but no response body, common for `DELETE`.
- **3xx - Redirection** indicates to the client that **the requested resource** has **been moved to a different path.** Browsers, and most HTTP clients **automatically follow new URL** unless users explicitly disable that behavior. The **most common redirection responses** are:
  - **301 Moved Permanently:** resource moved to a new permanent URL, **method might change.**
  - **302 Found:** temporary redirect, **method might change.**
  - **304 Not Modified:** client can use a cached version.
  - **307 Temporary Redirect:** like 302, but **method must not change.**
  - **308 Permanent Redirect:** like 301 but **method must not change.**
- **4xx - Client Errors** indicates that the client made a bad request. The **most common client errors responses** are:
  - **400 Bad Request:** the request was malformed.
  - **401 Unauthorized:** authentification is required.
  - **403 Forbidden:** authentification OK, but access denied.
  - **404 Not Found:** resource not found.
  - **405 Method Not Allowed:** request method not allowed. It means the server **understands the method** but that method is **not allowed for** this specific resource.
  - **409 Conflict:** resource conflict, *e.g.,* duplicate data.
  - **429 Too Many Requests:** rate limiting.
- **5xx - Server Errors** indicates that the server failed to process a valid request. The **most common server errors responses** are:
  - **500 Internal Server Error:** generic server failure. It means the **server encountered** an **unexpected condition** and could **not fulfill** the request.
  - **501 Not Implemented:** server doesn't support the requested method. It means the server does **NOT recognize** the method.
  - **502 Bad Gateway:** indicates a **problem between servers.** A server acting as a **gateway or proxy** received an **invalid response** from an upstream server.
  - **503 Service Unavailable:** server overloaded or down for maintaince.
  - **504 Gateway Timeout:** upstream server didn't respond in time.

#### HTTP Secure (HTTPS)

- HTTPS stands for **HTTP Secure.**
- Uses **SSL/TLS encryption.**
  - **SSL (Secure Sockets Layer)** is **deprecated** and insecure now. SSL is **completely disabled** in modern browsers, severs.
  - **TLS (Transport Layer Security)** is the *newer and current* security protocol. **Only TLS 1.2 and TLS 1.3** are recommended today.
- **Benefits:**
  - **Data is encrypted,** so attacker can't read or tamper with it.
  - **Requires** an **SSL/TLS certificate** issued by a **trusted Certificate Authority** (CA).
  - **Ensures data integrity.** Information arrives unchanged.
  - **Protects** user privacy by **encrypting all transmitted data.**
- **How HTTPS works:**
  1. client $\rightarrow$ server: "Hello!". When we visit a HTTPS site, the browser **sends** the server a **hello message** which **contains:**
     - **supported encryption** methods,
     - **supported TLS** versions,
     - a **random number,** used to generate keys later.
  2. server $\rightarrow$ client: "Here's my certificate". The server **replies** with a message which **contains:**
     - its **SSL/TLS certificate,**
     - its **public keys,**
     - a **random number** of its own.
  3. the browser **checks** if the **certificate** is **valid and trusted,** then **creates a session key:**
     - **generates** a **secret symmetric key.**
     - **encrypts** this key **with** the **server's public key.**
     - **sends it back** to the server. **Only** the **server can decrypt** this because it has the private key.
  4. **secure encrypted tunnel is establish.**
      - Now, **both** browser and server **share** the same **secrete session key.**
      - They **use symmetric encryption** to **exchange data** securely.
  5. **encrypted data transfer begins.** Every request/response is encrypted: URLs (except domain), cookies, form data, API calls, headers (partially).

### Request and Response Objects

- Django **handles** the request and response **with the help of** `HttpRequest` and `HttpResponse` classes in the `django.http` module.
- Django **obtains** the `HttpRequest` object **from the context provided** by the server.
- As a client's **request received,** Django's **URL dispatcher** mechanism **invokes a view** that matches the URL pattern **and passes** this `HttpRequest` object **as the first argument** so that all the request metadata is available to the view for processing.

#### HttpRequest Object

The `HttpRequest` object **contains** metadata about the **client's request,** including method, GET and POST parameters, cookie, and user information. Some of the **main attributes and methods** of an `HttpRequest` object (*e.g.,* `request`) are:

- `request.method` **returns** the **HTTP method** that the client used to send request to the server.
- `request.GET` and `request.POST` return a **dictionary-like object** containing GET and POST parameters, respectively.
- `request.COOKIES` returns a dictionary of string keys and values.
- `request.FILES`: when user uploads one or more files with a multipart form, they're present in this attribute in the form of `UploadedFile` objects.
- `request.user` contains information about the current user. It's an object of `django.contrib.auth.models.User` class. If the user is unauthenticated, it returns `AnonymousUser`.
- `request.has_key()` helps check whether the `GET` or `POST` parameter dictionary has a value for the given key.

#### HttpResponse Object

The `HttpResponse` object is **used to construct the response** sent back to the client, including status codes, content, and headers. Some of the main attributes and methods of the `HttpResponse` object are:
- `status_code` returns the HTTP status code corresponding to the response.
- `content` returns the byte string of the response.
- `write()` creates a file-like object.

### Understanding URLs

URL stands for **Uniform Resource Locator.** It's simply an address where the files are stored. *For example:*
- `https://www.littlelemon.com/customers/5`.
- `https://www.littlelemon.com/menu/?year=2022`.

A URL is made up of multiple parts put together:
- **scheme** or referred as the **protocol** is located at the beginning of any url address and can be identified as `http` or `https`. The protocol **determines the set of rules** around the transmission and exchange data.
- **subdomain** is **located before the domain** and usually contains the home page and other important pages. The **most common subdomain** is World Wide Web represented by `www`.
- **domain,** *e.g.,* `littlelemon.com`, consists of two parts:
  - **second level domain** refers to an organization or the name of a company. *e.g.,* `littlelemon`.
  - **top level domain** is used to reference a country or category of the organization. *e.g.,* `.com` address can indicate a comercial entity.
- **path** also known as the **page path** directs the user to the **location of a resource.** *e.g.,* `/customers/5`, `/menu`.
- **query string** begins with a question mark symbol `?` and is **placed after** the URL path. It **contains parameters** represented as **key value pairs.** *e.g.,* `?year=2022`.

### Parameters

The view function in Django **receives** its **mandatory argument** as the **request object** from the server context. The client **may pass additional arguments** via different methods.

#### Path Parameter

- A path parameter is **a variable part** of the URL that is **used to identify a specific resource,** *such as* `/customers/5`, where `5` is an argument of the path parameter.
- There may be **multiple path parameters** in the URL, separated by the **path separtor,** the slash symbol `/`.
- **How it works:**
  - The URL dispatcher **maps the pattern to** the view function and identifies `5` as the customer id `pk` parameter.

    ```python
    path("custmers/<int:pk>/", views.customer_detail, name="customer_detail"),
    ```
  - The parameter **is parsed as** `pk` parameter and **picked** by the `views.customer_detail()` function.
  - The view `customer_detail` function needs an **additional parameter** `pk`, as shown in the following example, because an **argument was passed** inside the `urls.py` file.

    ```python
    def customer_detail(request: HttpRequest, pk: int):
      pass
    ```
  - The **parameter names** added inside the `path` function in the `urls.py` file **must match the ones added** inside the `customer_detail()` view function associated with it in the `views.py` file.
  - **Best pratice:** avoid overly **verbose parameter names** such as `customer_id`, **prefer** the conventional `pk`.

#### Path Converters

- The URL pattern treats the **identifiers in angular brackets** `<>` as the path parameters.
- **By default,** it **parses** the received **value to** the **string type.**
- Path parameters avaiblable are:
  - `str`: matches any **non-empty string** and **excludes** the path separator `/`. This is the default if a converter isn't included in the expression.
  - `path`: matches any **non-empty string** and **includes** the path separator `/`.
  - `int`: matches **zero or any positive** integer and **returns** an `int`.
  - `uuid`: matches a formatted UUID and **returns** a UUID instance.
  - `slug`: matches any slug string consisting of ASCII letters or numbers, **including** the hyphen and underscore characters.

#### Query Parameter

- A query string is a **sequence** of one or more **key-value pairs** concatenated by the ampersand symbol `&`. They're added to the URL **after** a question mark symbol `?`.

  *For example:* `https://www.littlelemon.com/customers/?name=John&age=35`
- The URL dispatcher **doesn't parse** these parameters. They **are fetched** by the view function **from** the request object it receives.
- The key-value pairs in the query string **are added** to the `request.GET` property. The request object's `GET` property is a **dictionary-like** object. Hence, values can be get as shown in the following example.

  ```python
  def customers(request: HttpRequest):
    name = request.GET.get("name")
    age = request.GET.get("age")
  ```

#### Body Parameter

- Body parameters are data sent in the **body of** a `POST` request, **typically** from an **HTML form,** which is not visible in the URL.
- Values can be get via request object's `POST` progerty, as demonstrated below.

  ```python
  def customers(request: HttpRequest):
    name = request.POST.get("name")
    age = request.POST.get("age")
  ```

### URL Dispatcher

- URL dispatcher is Django's **mechanism** that **uses patterns** that are defined by URL mapping in `urls.py` **to route request** to the correct view.
- **How it works:**
  1. a **request comes** in, *e.g.,* `/customers/5/`.
  2. Django **removes** the domain name and leading slashes.
  3. URL dispatcher **looks** at the `urlpatterns` list in `urls.py` file(s).
  4. It checks each pattern, from **top to bottom.**
  5. The **first matching pattern** triggers the **corresponding view.**
  6. Django **calls** that view and **returns** the response.

#### URL Mapping

- URL mapping is a **set of URL patterns** that **are defined** in `urls.py` file(s). It's a list of instruction or **a table of routes.**
- **Components** of URL mapping:
  1. **URL patterns:** written in `urls.py` using `path()` or `re_path()` function.
  2. **Views:** functions or classes that handle the request.
  3. **Arguments / Parameters:** dynamic segments like `<int>` or `<slug>`.
  4. **Names:** each URL can be given a `name` **for [reverse](#reverse-function)** URL lookup.

  *For example:*

  ```python
  path("home/", views.HomeView.as_view(), name="home")  # class-based view
  path("articles/<int:year>/<slug:title>/", views.articles, name="articles")  # function-based view
  ```

#### Regular Expressions in URLs

- Regular expressions are used to **define,** extract, and validate **dynamic URL paths** before they are sent to the associated view function.
- To **use regular expressions** in URLs, it needs to **import and use** the `re_path()` function from the `django.urls` module.

  *For example:*

  ```python
  from django.urls import path, re_path

  from . import views


  urlpatterns = [
    path("menu-item/10/", views.display_menu_item, name="static_path"),
    path("menu-item/<int:pk>/", views.display_menu_item, name="dynamic_path"),
    re_path(r"^menu-item/([0-9]{2})/$", views.display_menu_item, name="regex_path"),
  ]
  ```

#### URL Pattern Convention

Django follows a convention similar to directory in Unix:
- ending pattern with a **trailing slash:** to look like a "container" endpoints. *For example,* `"menu-item/10/"`.

  Django by default redirects URLs like `example.com/menu-item/10` to `example.com/menu-item/10/`. Hence, the pattern `menu-item/10/` works with both `example.com/menu-item/10` and `example.com/menu-item/10/`, but `menu-item/10` doesn't work with `example.com/menu-item/10/`.
- **NOT include** a leading slash.

  Django does not expect leading slash, so `/menu-item/10/` won't match `example.com/menu-item/10/`.
- use **kebab-case** for URL paths. *For example:* `menu-item`.

**Rule of thumb: never use** leading slash, **use trailing slash** to keep consistency, **use kebab-case** for naming URL paths.

#### URL Namespacing

- The **application namespace** is created **by defining** the `app_name` variable in the applications's `urls.py` module and assigning it the name of the app.

  ```python
  # demoapp/urls.py
  app_name = "demo_app"
  ```
- Django **differentiates** between **same-name URLs** in multiple apps with application namespace.
- The `app_name` defines the **application namespace** so that the views in this app are identified by it.

  ```shell
  >>> reverse("demo_app:index")
  "/demo/"
  ```
- We can also **define** the **instance namespace** in the `include` function **while adding** an app's `urlpatterns`. This namespace is called the **instance namespace.**

  ```python
  urlpatterns = [
    path("demo/", include("demoapp.urls", namespace="demo_app"))
  ]
  ```
- By convention, **use snake_case** for application namespace. *For example:* `demo_app`.

#### `reverse` Function

- `reverse()` function **does the opposite** of URL matching. It **takes** a URL name (and optionally parameters) and **returns** the **actual URL path** as a string.
- It's **useful to:**
  - **avoid hard-coding URLs** as strings.
  - **keep URLs consistent** even if our URL patterns change.
  - help when **generating links** inside views, models, forms, etc.

  *For example:*
  - URL name is defined in the `urls.py` module.

    ```python
    path("menu-items/<str:dish>/<int:pk>/", views.menu_items, name="menu_items")
    ```
  - Using `reverse()` function in the `views.py` module to get the actual URL path.

    ```python
    from django.urls import reverse

    url = reverse("menu_items", kwargs={"name": "pasta", "pk": 10})
    print(url)  # /menu/pasta/10/
    ```
- The `reverse()` function is **commonly used:**
  - **in views** to redirect.

    ```python
    from django.shortcuts import redirect
    from django.urls import redirect

    return redirect(reverse("homepage"))
    ```
  - **in templates,** indirectly via `{% url %}`.

    ```html
    <a href="{% url 'homepage' %}">Home</a>
    ```

    **Note:** `{% url %}` is a **built-in** Django template tag. It **works out of the box** in Django templates - **no** import and **no** `{% load %}` statement **required.**
  - in Django REST framework **when** building hyperlinks.

### Error Handling

Django has a **built-in error handling system** that helps us manage exceptions, return proper error pages, and debug applications.
- Django's **built-in error views:** Django automatically **provides** default pages for **common HTTP errors** *such as* 400, 403, 404, 500.
  - When `DEBUG = True` (**development mode**), Django shows a **detailed debug page** with traceback, request info, environment variables, template context.
  - When `DEBUG = False` (**production mode**), Django shows **simple** public-facing error pages (`400.html`, `403.html`, etc.)
- **Custom error pages:** we can override Django's default error pages by creating templates in the project `/templates` folder:

  ```text
  templates/400.html
  templates/403.html
  templates/404.html
  templates/500.html
  ```
- **Custom error handlers:** We may define customer view functions to handle errors in the `urls.py` module at the project level.

  ```python
  # project/urls.py

  handler400 = "myapp.views.custom_400"
  handler403 = "myapp.views.custom_403"
  handler404 = "myapp.views.custom_404"
  handler500 = "myapp.views.custom_500"
  ```

  ```python
  # myapp/views.py

  def custom_400(request, exception):
    return render(request, "400.html", status=400)
  ```
- **Inside views:** we can **return** a `HttpResponse` or **raise** an exception. *For example:*
  - returns a `HttpResponseNotFound`, which is a **subclass of** `HttpResponse` that specifically indicates a 404 error. It internally **sends** an error code `404`. Other **predefined subclasses** include `HttpResponseBadRequest` and `HttpResponseForbidden`.
  - **raises** a `Http404` exception, which is a class defined in the `django.core.exceptions` module. Some **important exception types** are: `ObjectDoesNotExist`, `EmptyResultSet`, and `FieldDoesNotExist`.

### Method Resolution Order (MRO)

- **Method Resolution Order (MRO)** is the **rule** that Python uses **to decide** which class's method/attribute gets **called first** when multiple classes are involved, especially **in multiple inheritance.**
- **MRO becomes important** when:
  - a class inherits from **multiple parent classes.**
  - two **parents contains** a method with the **same name.**
  - mixins are used.
  - want to know which `super` method is called next.
- **MRO decides** the search path Python will follow.

  *For example:*

  ```python
  class A:
    def hello(self):
      print("A")


  class B:
    def hello(self):
      print("B")


  class C(A, B):
    pass


  instance = C()
  instance.hello()  # A
  ```
  Even though the `C` class inherits from both `A` and `B` classes. Both of them have the `hello` method, Python chooses the one of `A`, not `B`. That decision is **based on the MRO.**
- The built-in `mro` method is used to see the MRO. *For example,* `C.mro()` returns the following list, that is the **exact search order** Python uses.

  ```python
  [
    <class '__main__.C'>,
    <class '__main__.A'>,
    <class '__main__.B'>,
    <class 'object'>
  ]
  ```
- Python **uses** an algorithm called **C3 Linearization** to **determine MRO:**
  - **Preserve the order** of inheritance.
  - **Respect MRO** of parent classes.
  - **Avoid** inconsistency and conflicts.
  - Guarantee a **single, predictable** path (linear).

### Naming Convention

- Naming a **view:**
  - use **snake_case for** funtion-based views and **PascalCase for** class-based views.
  - **use** verbs or verb-noun phrases.
  - name **should describe** what the view does.
  - **class-based view** names should **end with** `View`.

  *For example:*

  ```python
  # views.py
  def create_order(request: HttpRequest) -> HttpResponse:
    pass


  def customer_list(request: HttpRequest) -> HttpResponse:
    pass


  class OrderCreateView(View):
    pass


  class CustomerListView(View):
    pass
  ```

- Naming **URL patterns**:
  - use **kebab-case** (hyphen-separated) **for** URL paths, **snake_case for** URL names (the `name=` argument).
  - **use nouns,** not verbs.
  - use **plural nouns** for **list endpoints.**
  - should **describe** the resource/action.

  *For example:*

  ```python
  # urls.py
  urlpatterns = [
    path("my-orders/", views.list_orders, name="order_list")
    path("customers/", views.customer_list, name="customer_list")
  ]
  ```

- Naming a **namespace** (`app_name`):
  - use **snake_case.**
  - **usually** the app name.
  - lowercase.

  *For example:*

  ```python
  # urls.py
  app_name = "demo_app"
  ```

- In bref, use **snake_case for** URL names, function-based views and namespaces, **kebab-case for** URL paths, and **PascalCase for** class-based views.

## Models

- A model is the **single definitive source** of information about the data. It **contains** the **essential fields** and **behaviors** of the data.

  > *A model is a blueprint for a database table, written in Python.*
- Each model is a Python class that **subclasses** `django.db.models.Model`. A **typical definition** of a model class is done **inside the app's `models.py` file.** *For example:*

  ```python
  from django.db import models


  class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
  ```
- **`pk`** stands for **primary key.** It is a **symbolic pointer** to **whatever field** serves as the model's primary key. It is **not a real** model field, just a **built-in alias.** We can use `pk` in **any ORM operations.** *For example:*

  ```python
  User.objects.get(pk=2)
  User.objects.filter(pk__in=[1, 2, 3])
  ```
- **`id` field:** when declaring a model,
  - if **no field** is **explicitly defined** as the **primary key,** Django **automatically creates** an auto‑incrementing `id` field **to serve** as the primary key.
  - if a **specific field is defined** as the primary key, Django **does not** add the default `id` field.
- A model:
  - represents **a single** database **table.**
  - each **attribute** of the model represents a **database field.**
  - each **instance** of the model **is a row.**
  - provides model methods to **perform CRUD** (Create, Read, Update, and Delete) operations using [Django's ORM](#django-orm-object-relationship-mapping) (**Object-Relational Mapper**).

    *For example:*
    - **C**reate

      ```python
      new_user = User(id=1, "John", "Jones")
      new_user.save()
      ```
    - **R**ead

      ```python
      user = User.objects.get(id=1)
      ```
    - **U**pdate

      ```python
      user = User.objects.get(id=1)
      user.last_name = "Smith"
      user.save()
      ```
    - **D**elete

      ```python
      User.objects.filter(id=1).delete()
      ```

### Field Types

The `django.models` module has many field types to choose from.

- `CharField`: is the most used field type. It can hold string data of length specified by `max_length` parameter.
- `TextField`: is similar to `CharField`, but for a longer string.
- `IntegerField`: stores an integer between $-2^{31}$ to $2^{31}-1$ (2_147_483_647). This **limit comes from** Django mapping `IntegerField` to the database `INTEGER` / `INT` data type, which is limited to **32 bits.** Similar fields to store integers of varying lengths:
  - `SmallIntegerField`: stores an integer between $-2^{15}$ to $2^{15}-1$ (32_767).
  - `BigIntegerField`: stores an integer between $-2^{63}$ to $2^{63}-1$ (9.22e18).
  - `PositiveIntegerField`: stores an integer between $0$ to $2^{31}-1$. In fact, it store **non-negative** values.
  - `AutoField`: **only** used **for primary key** and auto-increment, stores an integer between $1$ to $2^{31}-1$.
- `FloatField`: stores a floating-point number.
- `DecimalField`: stores a number **with fixed digits** in the **fractional part.**
- `DateTimeField`: stores the date and time as an object of Python's `datetime.datetime` class.
- `DateField`: stores `datetime.date` value.
- `EmailField`: is a `CharField` with an in-built `EmailValidator`.
- `URLField`: is a `CharField` having in-built validation for URL.
- `FileField`: used to save the **file uploaded** by the user **to** a **designated path** specified by the `upload_to` parameter.

### Model Relationships

- **Primary Key** is a **unique identifier** for each record in a database table, **ensuring** that no two rows have the same value.
- **Foreign Key** is a **field** in one table that **uniquely identifies** a row of **another table,** establishing a **relationship between two table.**
- The idea behind **designing related tables** is to **avoid data redundancy,** unnecessary repetition of the same data in many rows and **ensure data integrity.**

- Relational databases have a mechanism to **prevent** the **deletion of the primary key** if it is **being used** in the **related table** so that the data integrity is **intact.**
- There are **three types of relationships** that exists:
  - **One-to-One** relationship: **a record** in one model is **associated with exactly one record** in another model.

      *For example,* a college can have only one principal.

      ```python
      from django.db import models


      class College(models.Model):
        name = models.CharField(max_length=50)
        strength = models.IntegerField()
        website = models.URLField()


      class Principal(models.Model):
        college_id = models.OneToOneField(College, on_delete=models.CASCADE)
        qualification = models.CharField(max_length=50)
        email = models.EmailField(max_length=50)
      ```

    **Note:** There are several **reasons to use a One‑to‑One** relationship instead of a single large table:
    - **Separation of concerns:** different data has different responsibilities. That keeps models smaller, responsibilities clearer, and code easier to reason about.
    - **Optional or rare data:** some data applies only to some users and are rarely accessed. Splitting avoids lots of `NULL` columns and keeps hot tables small and fast.
    - **Different lifecycles:** sometimes data is created later or can be deleted independently.
    - **Permissions and ownership:** some data should be accessible to different services and have different permissions. *For instance,* `User` table is accessible via auth service while `UserProfile` is accessible via profile service.
    - **Database and performance reasons:** some data like `User` is queried constantly while some other like `UserProfile` is queried occasionally. Splitting avoids wide rows, cache misses, and unnecessary I/O.
    - **Domain modeling (real-world meaning):** One-to-One represents a conceptual extension, not just more columns. *For example,* `Passport` - `Person`, `Engine` - `Car`, `MedicalRecord` - `Patient`, etc. They are separate concepts, even if tightly linked.
  - **One-to-Many** relationship: **a single record** in one model can be **associated with multiple records** in another model.

    *For example,* a teacher is qualified to teach a subject, but there can be more than one teacher in a college who teaches the same subject.

    ```python
    class Teacher(models.Model):
      name = models.CharField(max_length=50)
      email = models.EmailField(max_length=50)


    class Subject(models.Model):
      teacher = model.ForeignKey(Teacher, on_delete=models.CASCADE, related_name="subjects")
      name = models.CharField(max_length=30)
      credits = model.IntegerField()
    ```
  - **Many-to-Many** relationship: **multiple records** in one model are **associated with multiple records** in another model.

    *For example,* more than one teacher can teach the same subject, and a single teacher can teach more than one subject.

    ```python
    class Teacher(models.Model):
      name = models.CharField(max_length=50)
      email = models.EmailField(max_length=50)


    class Subject(models.Model):
      teacher = model.ManyToManyField(Teacher)
      name = models.CharField(max_length=30)
      credits = model.IntegerField()
    ```

    **Note:** Relational databases do **not natively support** Many‑to‑Many relationships and therefore **require an intermediate table.** Django **generates this junction model automatically,** managing **referential integrity** as well as **admin and ORM integration.** This **simplifies** development and **prevents** accidental duplicates, although it **also reduces** the level of customization available.

- `on_delete` option **sepcifies the behavior** in case the **associated object** in the primary model **is deleted.** The values are:
  - **CASCADE:** deletes the object containing the `ForeignKey`. Deleting the reference object will also delete the referred objects.

    *For example,* suppose that a vehicle belongs to a customer. **When the customer** is deleted, **all the vehicles** that reference the customer will **be automatically deleted.**
  - **PROTECT:** is the opposite of **CASCADE.** It prevents deletion of a referenced object if it has an object referencing it in the database.

    *For example,* if a customer has vehicles, it cannot be deleted. Django will raise the `ProtectedError` if the customer is forcefully deleted.
  - **RESTRICT:** prevents deletion of the referenced object by raising `RestrictedError`, but it **allows deletion if** *all referencing objects are also being deleted* **in the same operation.**

    This behavior is **different** from **PROTECT,** which prevents deletion whenever a related reference exists, **even** when that referenced record is being deleted too.

    *For example,* with the code block below

    ```python
    # create a principal associated with the college with id 1
    college = College.objects.get(pk=1)
    pricipal = Principal.objects.create(
      college=college, qualification="good", email="principal@college.com"
    )
    principal.save()

    # delete both the college and the associated principal
    college.delete()
    principal.delete()
    ```
    - if the relationship between `College` and `Principal` is set to **PROTECT,** the deletion will be blocked and a `ProtectedError` will be raised.
    - if the relationship between `College` and `Principal` is set **RESTRICT,** the deletion will be succeed because Django recognizes that the referenced object will be deleted as part of the same operation.
  - **Note:** when `delete` methods are called, Django does **NOT delete rows immediately.** Instead, it **first plans** the entire delete, **then checks** whether it's legal, **then executes** it.
    - Builds a delete graph.
    - Checks constraints (`on_delete`).
    - Executes deletes in a safe order.

    Under **PROTECT** relationship, Django **aborts the deletion immediately** as soon as it detects a related object. It does not considers whether that the related object might also be deleted later, no delete graph analysis is performed.

    Under **RESTRICT** relationship, Django **waits until the entire delete graph is known,** then it determines *whether any restricted objects would remain after the operation.* If so, it raises `RestrictedError`; if not, the deletion procceds.

### Migrations

- Migration is a **mechanism** that **translates** the model changes into database schema changes, allowing for **version control** of the database structure.
- It **propagates** any changes in the model structure *such as* adding, modifying, or removing a field attribute of a model class to the **mapped table.**
- Django's migration is a **version control system.** It has the following commands:
  - `makemigrations` creates migration scripts that reflect changes made to models, which are then applied to the database.
  - `migrate` applies the migration scripts to the database, creating or modifying tables as defined in the migration files.
  - `sqlmigrate` shows the SQL query or queries executed when a certain migration script is run.
  - `showmigrations` displays the status of migrations, indicating which have been applied and which are pending.
- When migrating a model, Django **automatically names the table** as `[app_name]_[model_name]`, *for instance,* `myapp_college`, `myapp_principal`, etc. We can override this by assigning the desired name to `db_table` parameter of the `Meta` class, to be declared inside the model class, as shown below.

```python
from django.db import models


  class College(models.Model):
    name = models.CharField(max_length=50)
    strength = models.IntegerField()
    website = models.URLField()

    class Meta:
      db_table = "college_info"
```

### Django ORM (Object Relationship Mapping)

[Object-Relational Mapping (ORM)](#object-relational-mapping-orm) is the ability to **create** a **SQL query using object-oriented programming language.** This **enables** a **quick turnaround time** in fast **production environments** that need constant updates.

Django has its own ORM layer. Its migration mechanism **propagates** the **models** in **database tables.** We need to **construct** a `QuerySet` via a `Manager` of a **model class** to **retrieve objects** from our database.

Each model is a Python class that subclasses `django.db.models.Model`. *For example:*

```python
from django.db import models


class Menu(models.Model):
  name = models.CharField(max_length=100)
  cuisine = models.CharField(max_length=100)
  price = models.IntegerField()
```

#### Manager

- `Manager` is the **interface** through which **database queries are made** for a model.
- Every Django model has **at least** one `Manager`.
- The **default** manager is `objects`.
- A `Manager` method **returns** `QuerySet` object(s).

  *For example:*

  ```python
  class Menu(models.Model):
    name = models.CharField(max_length=100)
    cuisine = models.CharField(max_length=100)
    price = models.IntegerField()

  print(type(Menu.objects))  # django.db.models.manager.Manager
  print(type(Menu.objects.all()))  # django.db.models.query.QuerySet
  ```
- **When to use** `Manager`s ?
  - Queries related to the **entire table.**
  - Default **filtering logic.**
  - Entry point for **custom query** methods.

#### QuerySet

- A `QuerySet` is a **lazy collection of objects** retrieved from the database.
- A `QuerySet`:
  - **represents** a database query.
  - can be **filtered, sliced, ordered.**

    *For example:*

    ```python
    qs = Menu.objects.filter(name__icontains="pasta")
    ```
  - can be **chained.**

    *For example:*

    ```python
    qs = Menu.objects.filter(name__icontains="pasta").order_by("name")
    ```
    These above query sets are **chained to one SQL query,** not many.
  - is a **lazy evaluation** (not executed until needed).
  - **returns** model instances.

  The query **executes only when:**
  - **iterated** over
  - **converted** to list
  - **printed**
  - **accessed** with the `len` function.

- **How to find the SQL query generated?** the`QuerySet`'s `query` attribute **returns** the **SQL query generated.**

  *For example:*

  ```python
  qs = Menu.objects.filter(name__icontains="pasta").order_by("name").only("name", "price")
  print(qs.query)

  # SELECT "demoapp_menu"."id", "demoapp_menu"."name", "demoapp_menu"."price" FROM "demoapp_menu" WHERE "demoapp_menu"."name" LIKE %pasta% ESCAPE '\' ORDER BY "demoapp_menu"."name" ASC
  ```

- **In bef,**
  - `Manager`: the **entry point** to datbase queries, lives on the model class.
  - `QuerySet`: the **lazy, chainable representation** of a datbase query.

#### CRUD Operations

- **Create** a row in the table:
  - create an object of the model class then use the `save` method to creates a row in the table. *For example:*

    ```python
    m = Menu(name="pho", cuisine="vietnam", price=12)
    m.save()
    ```
  - use the `create` method of the `Manager`. This method will return an instance of the model class.

    ```python
    Menu.objects.create(name="pho", cuisine="vietnam", price=12)
    ```
- **Read** rows:
  - fetch all objects by using the `all` method of the `Manager`. *For example:*

    ```python
    Menu.objects.all()
    ```
  - apply filters to the data fetched from the model by using `filter` method of the `Manager`.

    ```python
    Menu.objects.filter(name__startswith="p")
    ```
- **Update** a row: get the object of that row, assign a new value to the attribute and `save` the object. *For example:*

    ```python
    m = Menu.objects.get(pk=2)
    m.cuisine = "chinese"
    m.save()
    ```
- **Delete** a row: get the object of the corresponding row then call the `delete` method. *For example:*

    ```python
    m = Menu.objects.get(pk=4)
    m.delete()
    ```

### Common Problems

The `Author` and `Book` classes below are used to demonstrate the problems.

```python
from django.db import models


class Author(models.Model):
  name = models.CharField(max_length=100)


class Book(models.Model):
  author = models.ForeignKey(Author, on_delete=models.CASCADE)
  title = models.CharField(max_length=100)
  status = models.CharField(max_length=50)
```

#### N+1 Problem

Refers to a problem where **one query** is used to fetch a list of objects, **followed by N additional** queries **to fetch** their **related data.** *For example:*

```python
books = Book.objects.all()

for book in books:
  print(book.author.name)
```

**To fix** the problem, we need to **use** `select_related` (for **One-to-One** or **One-to-Many** relationships) or `prefetch_related` (for **Many-to-Many** or reverse relationships). *For example:*

```python
books = Book.objects.select_related("author")

for book in books:
  print(book.author.name)
```

#### Sequential Scan (Seq Scan) Problem

Occurs the database **reads every row** in a table, one by one, **to find** those that match the query. *For example:*

```python
Book.objects.filter(status="BORROWED")
```

**To fix** the problem, we can **add indexes** to the queried fields. *For example:*

```python
class Book(models.Model):
  status = models.CharField(max_length=50, db_index=True)
```

#### Fetching Too Many Columns Problem

Refers to a **data-access performance problem** where the query **retrieves more** fields **than** the actual needs. *For example:*

```python
Book.objects.all()
```

**To fix** the problem, we can **use** the `only` method to **specify** the fields we need. *For example:*

```python
Book.objects.only("id", "status")
```

#### Too many JOINs Problem

Happens when a query **joins more tables than are actually needed,** making it slow, complex, and hard for the database optimizer to execute efficiently. *For example:*

```python
Book.objects.select_related("author__profile__country__continent")
```

**To fix** the problem, we should **join only** what we need, **fetch specific** fields rather than entire tables, or intentionally **split queries.** *For example:*

```python
# join only what we need
Book.objects.select_related("author")

# fetch specific fields
Book.objects.only("id", "author__name")
```

### Django Form

- A form is a **document** wherein the user **enters** their responses **at** certain labeled placeholders.
- Django **includes** a `Form` class, its attributes, and methods **in** the `django.forms` module. This class is **used as a base** for a user-defined form design.

  ```python
  form django import forms


  class ApplicationForm(forms.Form):
    pass
  ```
- The **attributes of the form** are `Field` class objects. The `django.forms` module has a collection of `Field` types. These fields **correspond to** the HTML elements they enventually render on the user's browser. *For example:*
  - the `forms.CharField` is translated to HTML's text input type.
  - the `forms.ChoiceField` is equivalent to `<select>` in HTML.

    ```python
    from django import forms


    POSTS = (
      ("mananger", "Manager"),
      ("cashier", "Cashier"),
      ("operator", "Operator"),
    )


    class ApplicationForm(forms.Form):
      name = forms.CharField(label="Name of Application", max_length=50)
      address = forms.CharField(label="Address", max_length=100)
      post = forms.ChoiceField(choices=POSTS)
    ```
- **By convention,** the user-defined **form classes** are **stored in** a `forms.py` file in the **app's package folder.**

#### Form Fields

Some of the **most frequently used fields** are as follow:
- `CharField`: translates to **input** `type=text` HTML form element.

  ```python
  forms.CharField(label="Name of Application", max_length=50)
  ```

  **Set** the field's `widget` property to `forms.Textarea` **to create** a `textarea`.

  ```python
  forms.CharField(label="Name of Application", widget=forms.Textarea)
  ```
- `EmailField`: a `CharField` that can **validate** if the text entered is a **valid email.**

  ```python
  forms.EmailField(max_length=254)
  ```
- `IntegerField`: similar to a `CharField` but customized to **accept only integer** numbers. We **can limit** the value entered by setting `min_value` and `max_value` parameters.

  ```python
  forms.IntegerField(min_value=0, max_value=10)
  ```
- `FloatField`: a text input field that **validates** if the input is a valid **float number.**

  ```python
  forms.FloatField()
  ```
- `DecimalField`: similar to `FloatField` but **supports fixed** numbers of **decimal places.**

  ```python
  forms.DecimalField(max_digits=10, decimal_places=2)
  ```

  `max_digits` and `decimal_places` are **mandatory** parameters of this field type.
- `FileField`: presents an **input** `type=file` element on the HTML form.

  ```python
  forms.FileField(upload_to="uploads/")
  ```
- `ImageField`: similar to `FileField` with **added validation** to check if the uploaded file is an **image**. The [pillow](https://pypi.org/project/pillow/) library is **required** for this field type to be used.

  ```python
  forms.ImageField(upload_to="uploads/")
  ```
- `ChoiceField`: **emulates** the HTML's `select` element. Populates the **drop-down list** with a `choices` parameter whose value should be a **sequence of two item tuples** `([value], [text_displayed])`.

  ```python
  PAYMENT_CHOICES = (
    ("card", "Credit Card"),
    ("cash", "Cash"),
    ("upi", "UPI"),
  )

  forms.ChoiceField(choices=PAYMENT_CHOICES)
  ```

  **Set** the field's `widget` property to `forms.RadioSelect` to create **radio buttons.**

  ```python
  forms.ChoiceField(choices=PAYMENT_CHOICES, widget=forms.RadioSelect)
  ```

#### Form Rendering

To **render** a form object on a browser, we have to **first write** an HTML template and put the form object in `jinja2` tag. *For example,* we create the `form.html` file as follow:

```html
<html>
  <body>
    <form action="{% url 'application-form' %}" action="POST">
      {% csrf_token %}
      <table>
        {{ form }}
      </table>
      <input type="submit" value="Submit">
    </form>
  </body>
</html>
```

**Then** in the app's `views.py` file which renders the `form.html` template and **sends** the `ApplicationForm` object as a context.

```python
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from .forms import ApplicationForm


def render_application_form(request: HttpRequest) -> HttpResponse:
  application_form = ApplicationForm()
  return render(request, "form.html", {"form": application_form})
```

Inside the `form.html` template, the **form** can **be rendered** in **different ways:**
- `{{ form.as_table }}`: renders the form **as table cells** wrapped in `<tr>` tags. The form is **rendered** as a table **by default**. *For example:*

  ```html
  <tr>
    <th><label for="id_name">Name of Applicant:</label></th>
    <td>
      <input type="text" name="name" maxlength="50" required id="id_name">
    </td>
  </tr>
  ```
- `{{ form.as_div }}`: renders the form **as divisions** wrapped in `<div>` tags. *For example:*

  ```html
  <div>
    <label for="id_name">Name of Applicant:</label>
    <input type="text" name="name" maxlength="50" required id="id_name">
  </div>
  ```
- `{{ form.as_p }}`: renders the form **as paragraphs** wrapped in `<p>` tags. *For example:*

  ```html
  <p>
    <label for="id_name">Name of Applicant:</label>
    <input type="text" name="name" maxlength="50" required id="id_name">
  </p>
  ```
- `{{ form.as_ul }}`: renders the form **as list items** wrapped in `<li>` tags. *For example:*

  ```html
  <li>
    <label for="id_name">Name of Applicant:</label>
    <input type="text" name="name" maxlength="50" required id="id_name">
  </li>
  ```

#### Reading From Contents

- A **view function** processes data submitted by the user, whether to create a new record or perform other server‑side actions.
- It first **populate** the form object with the POST data and **check** it is valid.
- The `django.forms.Form` class **provides** the `is_valid` method to **run validation** on each field and **return** `True` if all field validations are passed. *For example:*

  ```python
  from django.http import HttpRequest, HttpResponse
  from .forms import ApplicationForm


  def process_application_form(request: HttpRequest) -> HttpResponse:
    if request.method != "POST":
      return HttpResponse("method not allowed!")

    form = ApplicationForm(request.POST)
    if not form.is_valid():
      return HttpResponse("data submitted is invalid!")

    # process the data submitted
    return HttpResponse("data submitted is processed!")
  ```

- Once the `Form` instance is **validated**, we can **access** the data individual field **via** its `cleaned_data` **attribute.** It ensures that the field contains the output in consistent form. *For example:*

  ```python
  name = form.cleaned_data["name"]
  address = form.cleaned_data["address"]
  post = form.cleaned_data["post"]
  ```

#### Cross-Site Request Forgery (CSRF) Attack

- **CSRF** (Cross-Site Request Forgery) **exploits** the browser's implicit trust, **not a bug** in the code.

  > Browsers **automatically send cookies** (session, auth) with every request to a domain, even if the request was **triggered by** another site.
- A CSRF attack **tricks** a logged-in user's browser **into sending** an **unintended request** to a trusted site, **using** the **user's own cookies** to **perform** an action **without** consent. *For example:*
  - The user **logs into** `bank.com`.
  - The **browser stores** a session cookie `session_id=abc123`.
  - The user **visits** `evil.com` **while** still logged in `bank.com`.
  - `evil.com` contains a **hidden HTML form to** send a request to `bank.com`.
  - The browser **automatically includes** user's session cookie.
  - The bank server **sees** valid session cookie, valid POST request then it **processes** the request.

  The scenario **works because** cookies are **included automatically** and the server **cannot tell whether** the request came from the legitimate form or from another site. That's the **CSRF vulnerability.**

  **Cookies** alone are **not enough,** because they **prove** who the user is **but not where** the request comes from.
- **How CSRF tokens work?**
  - When the **user visits** the website, Django **generates** a radom, secret **CSRF token** for the user.
  - The token is **sent and stored** in a cookie in the browser.
  - When the user submits a form, **the token** stored in the cookies **is embedded** into the HTML form as a **hidden field generated** by `{% csrf_token %}`.
  - The browser **sends both** cookies and the form token.
  - Django's **CSRF middleware compares** the two tokens.
  - If they **match**, the request is **accepted.**
  - If **missing or different**, Django returns **403 Forbidden.**

  The attacker **cannot supply the correct CSRF token** because:
  - it **cannot read cookies** from another domain.
  - it **cannot read form** HTML from another domain.
  - it **cannot guess token** (random and long).
- **When** to **use** a **CSRF token** and **when not** to?
  - CSRF token **required for** `POST`, `PUT`, `PATCH`, `DELETE` when using forms or **modifying** server-side data.
  - CSRF token **not required** for `GET` requests and read-only views.

### Django Admin

- Django Admin Interface, usually called **Django Admin** is a **built-in** web application that **allows for easy management** of users, groups, and permissions.
- To **access** the Django Admin, a superuser is **required.** A **superuser** has the privileges to **add or modify** users and groups, and **can be created** using the `createsuperuser` command as follows.

  ```cmd
  > python manage.py createsuperuser
  ```
- If a user's `is_staff` property is **set** to `True`, they **can log in** to the admin interface. **Non-staff users** cannot access the admin site.
- Django's admin site **provides** a very easy-to-use interface to add and modify users and groups, there are **no real restrictions** as the User admin. *For instance,* a **user** with **staff status:**
  - can **manage** the other users.
  - can **edit** their **own permissions**, which is not warranted.
  - can **allocate** superuser right.

  The out-of-box implementation of the admin site **doesn't prevent** this.
- Since **Django Admin is restricted** to staff users, **to allow** regular (**non-staff**) users to **log in** the website, we need to **create a login page** using Django's built-in authentication system, as shown in the example below.

  ```python
  # views.py
  from django.contrib.auth import authentication, login
  from django.http import HttpRequest, HttpResponse
  from django.shortcuts import render, redirect


  def user_login(request: HttpRequest) -> HttpResponse:
    if request.method != "POST":
      return render(request, "login.html")

    username = request.POST.get("username")
    password = request.POST.get("password")
    user = authenticate(request, username=username, password=password)

    if user is None:
      return render(request, "login.html", {"error": "Invalid credentials!"})

    login(request, user)  # work for non-staff users
    return redirect("home")
  ```

#### Customizing User Admin

- The `UserAdmin` class from the `django.contrib.auth.admin` module **allows** developers to **control** which fields are editable and to implement additional security measures.
- **To customize** the User Admin, we **first extend** the `UserAdmin` class in the app's `admin.py` file, **then unregister** the default `User` model and **register it with** the new exteded class.
  ```python
  # admin.py
  from django.contrib import admin
  from django.contrib.auth.models import User
  from django.contrib.auth.admin import UserAdmin


  class CustomUserAdmin(UserAdmin):
    pass


  admin.site.unregister(User)
  admin.site.register(User, CustomUserAdmin)
  ```

  **Alternatively**, we **can unregister** the `User` model first, then **use** the `admin.register` **decorator to** create and register it with the extended class, as shown below.

  ```python
  # admin.py
  from django.contrib import admin
  from django.contrib.auth.models import User
  from django.contrib.auth.admin import UserAdmin

  admin.site.unregister(User)


  @admin.register(User)
  class CustomUserAdmin(UserAdmin):
    pass
  ```
- In *the example* below, the `CustomUserAdmin` class **prevents users** from **modifying** the `last_login` and `date_joined` fields. It also **prevents non-superusers** from **changing** the `username`, **assigning** groups, user permissions, or **granting superuser** privileges by marking corresponding fields as read-only.

  ```python
  class CustomUserAdmin(UserAdmin):
    readonly_fields: tuple[str, ...] = ("last_login", "date_joined")

    def get_readonly_fields(self, request: HttpRequest, obj: Any = None) -> tuple[str, ...]:
      if obj and not request.user.is_superuser:
        return self.readonly_fields + (
          "username",
          "groups",
          "user_permissions",
          "is_superuser",
        )
      return self.readonly_fields
  ```

- **Notes:**
  - If two apps **both customize** `UserAdmin`, **the one registered last wins**, and the other is silently overridden. No error. No warning. Just override.

    An app's loading **order** is **determined** by its **position** in the `INSTALLED_APPS` list. *For example:*

    ```python
    # settings.py
    INSTALLED_APPS = [
      "app_loaded_first",
      "app_loaded_second",
    ]
    ```
  - **Best practice:** create **one app** responsible for the User Admin.

#### Customizing Model Admin

- Users can **perform** CRUD operations **on a model** through the Django Admin. To enable this, the model must be **registered with the admin site** as follows.
  - **define** the model **in** the app's `models.py` file. *For example:*

    ```python
    # models.py
    from django.db import models


    class Book(models.Model):
      title = models.CharField(max_length=100)
      author = models.CharField(max_length=100)
    ```
  - **register** the model with the admin site **in** the app's `admin.py` file. *For example:*

    ```python
    # admin.py
    from django.contrib import admin
    from .models import Book


    admin.site.register(Book)
    ```
- To customize a **model's admin interface**, we first **create a custom admin** class by **extending** the `ModelAdmin` class, **imported from** `django.contrib.admin` module, **then register** the model with this new admin class, similar to how we customize the User Admin. *For example:*

  ```python
  from django.contrib import admin

  class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author")
    search_fields = ("title__contains", )


  admin.site.register(Book, BookAdmin)
  ```

#### Permissions

- Django has an **in-built system for** handling permissions. This authentication system has **features for both** authentication and authorization.
- A **user** in Django can **be one of three** classifications:
  - **superuser:** is a **top level user** or adminstrator of the system. This type of user **possesses permission** to add, change, or delete other users, as well as perform operations **on all the data** in the project.
  - **staff user:** is **allowed to** access Django Admin Interface. However, a staff user **doesn't automatically get** the permission to create, read, update, and delete data in the Django admin. It **must be** given explicitly.
  - (regular) **user:** is **not authorized to** use the admin site. When a user is created, they're **marked as** a regular, active user by default.
- **Setting** the `is_staff` and `is_superuser` **properties** to `True` **makes a user** a staff user or a superuser, respectively.
- The permission mechanism is **handled by** the `django.contrib.auth` app.
- When a model is created, Django **automatically creates** `add`, `change`, `delete`, and `view` permissions. These permissions follow the **naming pattern** `[app].[action_model]` pattern.
  - `app`: is the application name.
  - `action`: is `add`, `change`, `delete`, or `view`.
  - `model`: is the model name in lowercase.

  *For instance,* `my_app.add_mymodel` **represents** the permission required to add a `MyModel` instance in the `my_app` application.
- A Django **group** is a **convient way** to **assign** the **same set of permissions** to multiple users. A **group** is simply a **collection of permissions** that can **be applied to** one or more users.

#### Enforcing Permissions

- Django app **receives** user information **through** the `request` context.
- **Permissions** are **often enforced at** the view layer. However, they **can also be applied** within templates, URL configurations, and both function-based and class-based views.
- Enforcing permissions **in views:**

  Below are several **common ways to verify** that a user is logged in and **authenticated:**
  - **Use** the `is_anonymous` function of the `request.user` object. *For example:*

    ```python
    from django.core.exceptions import PermissionDenied
    from django.http import HttpRequest, HttpResponse


    def my_view(request: HttpRequest) -> HttpResponse:
      if request.user.is_anonymous():
        raise PermisionDenied()
      return HttpResponse("Authenticated user!")
    ```
  - **Use** the `login_required` decorator, **imported from** `django.contrib.auth.decorators` module. *For example:*

    ```python
    from django.contrib.auth.decorators import login_required
    from django.http import HttpRequest, HttpResponse


    @login_required
    def my_view(request: HttpRequest) -> HttpResponse
      return HttpResponse("Authenticated user!")
    ```

  - **Use** the `user_passes_test` decorator, **imported from** `django.contrib.auth.decorators` module. This decorator **takes** a **single required argument**, which is a boolean function, so it **can be used for both** authentication and authorization. *For example:*

    ```python
    from typing import Union

    from django.contrib.auth.base_user import AbstractBaseUser
    from django.contrib.auth.decorators import user_passes_test
    from django.contrib.auth.models import AnonymousUser
    from django.http import HttpRequest, HttpResponse


    def verify_permission(user: Union[AbstractBaseUser, AnonymousUser]) -> bool:
      return user.is_authenticated() and user.has_perm("my_app.change_category")


    @user_passes_test(verify_permission)
    def update_category(request: HttpRequest) -> HttpResponse
      return HttpResponse("Authorized user!")
    ```

  **For authorization:**
  - **Use** the `permission_required` decorator, **imported from** `django.contrib.auth.decorators` **with** function-based views. *For example:*

    ```python
    from django.contrib.auth.decorators import permission_required
    from django.http import HttpRequest, HttpResponse


    @permission_required("my_app.change_category")
    def update_category(request: HttpRequest) -> HttpResponse
      return HttpResponse("Authorized user!")
    ```
  - **Use** the `PermissionRequiredMixin` class, **imported from** `django.contrib.auth.mixins` **with** class-based views. *For example:*

    ```python
    from django.contrib.auth.mixins import PermissionRequiredMixin
    from django.views.generic import ListView

    from .models import Product


    class ProductListView(PermissionRequiredMixin, ListView):
      model = Product
      permission_required = "my_app.view_product"
      template_name = "product.html"
    ```
- Enforcing permissions **in templates:**
  - Django **automatically injects** the `user` and `perms` variables **into templates,** making authentication and authorization checks **available directly in** the template context.
  - **Check the authentication:**

    ```html
    {% if user.is_authenticated %}
    Authenticated user!
    {% endif %}
    ```
  - **Check the authorization:**

    ```html
    {% if perms.my_app.view_product %}
    Authorized user!
    {% endif %}
    ```
  - **Note** that templates do **not enforce security** on their own. They **only hide** UI elements **and improve** the UX. Actual **permission enforcement** must **be handled** on the **server side,** typically **within views.**
- Enforcing permissions in **URL patterns:**
  - URL patterns **cannot** enforce permissions on their own, but we **can wrap** views with permission checks in `urls.py` **to enforce** access control at the URL level. For example:

    ```python
    # urls.py
    from django.contrib.auth.decorators import login_required, permission_required
    from django.urls import path

    from . import views

    urlpatterns = [
      path("products/", login_required(views.display_products), name="view_product"),
      path(
        "products/<int:pk>/edit/",
        permission_required("my_app.change_product")(views.update_product),
        name="update_product"
      ),
    ]
    ```
  - **This approach** to enforcing permissions **is not recommended.**
  - **Best practice:** URLs route requests. Views enforce permissions.

### Database Configuration

- **By default,** Django **uses the SQLite database** for storing and retrieving application data, since Python provides built-in support for it.
- Django also **supports other databases** such as PostgreSQL, MySQL, and more.

#### Setup Steps

The following steps outline how to configure Django with supported databases.

- **Install** the **database server.** *For example:* PostgreSQL, MySQL.
- **Create** a **database and user,** ensuring both are ready to use.
- **Install** the **appropriate Python driver** so Django can connect to the database. *For example:*

  ```cmd
  # PostgreSQL driver
  > pip install psycopg2-binary

  # MySQL driver
  > pip install mysqlclient
  ```
- **Configure** `settings.py` by **updating** the `DATABASES` setting with the correct `ENGINE`, `NAME`, `USER`, `PASSWORD`, `HOST`, `PORT`, and any required `OPTIONS`. *For example:*

  ```python
  # PostgreSQL
  DATABASES = {
    "default": {
      "ENGINE": "django.db.backends.postgresql",
      "NAME": "mydb",
      "USER": "myuser",
      "PASSWORD": "mypassword",
      "HOST": "localhost",
      "PORT": "5432",
    }
  }

  # MySQL
  DATABASES = {
    "default": {
      "ENGINE": "django.db.backends.mysql",
      "NAME": "mydb",
      "USER": "myuser",
      "PASSWORD": "mypassword",
      "HOST": "localhost",
      "PORT": "3306",
      "OPTIONS": {
        "init_command": "SET sql_mode='STRICT_TRANS_TABLES'",
      },
    }
  }
  ```
- **Run migrations** to initialize the database schema.

  ```cmd
  > python manage.py makemigrations
  > python manage.py migrate
  ```
- **Test connection** to confirm everything is working correctly.

  ```cmd
  > python manage.py dbshell
  ```

  If the command opens a DB shell (`psql`, `mysql`, etc.), the config works.

#### Environment Variables vs. Configuration Files

- **Best practice:**
  - **Never hardcode sensitive information** in source code, as it can easily **be exposed, leaked, or commited** to version control.
  - Use **environment variables** to **manage secrets** and deployment-specific values.
  - Use **configuration files** to **define** structure, defaults, and non-sensitive settings.
- `python-decouple` is a **lightweight** Python package that **helps separate configuration** from code, especially secrets and environment-specific settings. It **allows** Python **read configuration from** environment variables and `.env` files in a clean and safe way. It:
  - **reads environment variables** first,
  - **falls back to** a `.env` file (for local development),
  - **converts values** to proper Python types, and
  - **keeps** secrets out of source code.

  *For example:*

  ```python
  from decouple import config


  DEBUG = config("DEBUG", default=False, cast=bool)
  NAME = config("DB_NAME")
  USER = config("DB_USER")
  PASSWORD = config("DB_PASSWORD")
  HOST = config("HOST")
  ```


## Templates


