# Django Web Framework  <!-- omit in toc -->

Comprehensive notes covering key concepts of the [Django Web Framework](https://www.coursera.org/learn/django-web-framework) course.

- [Introduction to Django](#introduction-to-django)
  - [HTML vs. HTML5](#html-vs-html5)
    - [Definition](#definition)
    - [Key Differences](#key-differences)
  - [Vitual Environment](#vitual-environment)
  - [Django Project Structure](#django-project-structure)
    - [DRY principle](#dry-principle)
    - [What is a project?](#what-is-a-project)
    - [Project package](#project-package)
    - [ORM Techinque](#orm-techinque)
    - [WSGI](#wsgi)
    - [ASGI](#asgi)
    - [Synchronous vs. Asynchronous Web Apps](#synchronous-vs-asynchronous-web-apps)
    - [Concurrency vs. Parallelism](#concurrency-vs-parallelism)
  - [Django-admin vs. manage.py commands](#django-admin-vs-managepy-commands)
  - [App structure](#app-structure)
  - [Web Framework](#web-framework)
    - [Three-tier Architecture](#three-tier-architecture)
    - [MVC Architecture](#mvc-architecture)
    - [MVT Architecture](#mvt-architecture)


## Introduction to Django

### HTML vs. HTML5

#### Definition

- **HTML** (Hyper Text Markup Language) is the **standard language for structuring** web pages.
- **HTML5** is the **newest version** of HTML, adding modern features for today's web.

#### Key Differences

- HTML5 **introduced semantic tags** such as `<header>`, `<footer>`, `<nav>`, `<section>`, `<article>`, `<aside>`, so browsers and developers understand page structure better, improve code readability. Since these tags have **built-in meaning**, they tell the browser (and developers, screen renders, search engines) **what the content represents**.
  - `<header>` $\rightarrow$ top of a page or section.
  - `<nav>` $\rightarrow$ navigation menu.
  - `<article>` $\rightarrow$ self-contained content (blog post, news article, post).
  - `<section>` $\rightarrow$ logical grouping of related content.
  - `<aside>` $\rightarrow$ sidebar or related info.
  - `<footer>` $\rightarrow$ bottom of a page or section.
- HTML **uses mostly** `<div>` for layout. It has **no meaning** by default.
  - is just a **generic container**.
  - used mainly for grouping elements for styling or scripting.
  - does not describe the purpose of its content.
- HTML5 **supports multimedia** without plugins like Flash.
- HTML5 adds `<canvas>` for **drawing graphics** and animations and improves SVG support.
- HTML5 introduces **new form inputs**, such as: `email`, `date`, `number`, `range`, `color` and **new attributes** such as `placeholder`, `required`, `pattern`, `autofocus`.
- HTML5 **adds client-side storage** like `localStorage`, `sessionStorage`, `IndexedDB`, application cache / service workers while HTML had only cookies.

### Vitual Environment

Python **recommends using a virtual environment to build** Python applications.

A virtual environment is an **isolated environment** having its copy of the interpreter and libraries so that there's **no clash** with the global installation of Python.

Python's virtual environment is set-up with the help of a built-in module named `venv`.

### Django Project Structure

- In Django,
  - **a project** represents the **entire web application**.
  - **an app** is a **sub-module of a project**.
- An **app** is typically used to implement functionality for some specific purpose.
  - **apps can be self-contained**, meaning they do not rely on other apps to function.
  - **apps can be used or reused** in may different projects. This leads nicely to the **DRY principle**.
  - an **app should be feature targeted**, and it's best suited for one and only one thing.
- In bref, **a Django web application is a project that contains many apps**.

#### DRY principle

The DRY principle stands for **Don't Repeat Yourself**. It's a fundamental guideline in software development that says:

> Every piece of knowledge should have a **single**, **unambiguous**, **authoritative** representation within a system.

In simple terms, it **prevents duplicating code, logic, or data**.

- The DRY principle leads to less maintenance, fewer bugs, and better readability.
- The DRY principle applies to coding and refactoring, database schema design, API design, infrastructure/configuration, and documentation.

#### What is a project?

- A Django project **is a Python package containing** the database configuration used by various sub-modules (apps) and other Django-specific settings.
- The `startproject` command of Django-admin is used to **create a new Django project**. It creates the folder of the given name (is called *project directory*), inside which there is another folder of the same name (is called *project package*) and the script `manage.py`.

  ```cmd
  > django-admin startproject <project_name>
  ```
  - **Project directory** is created when we create a Django project. It contains `manage.py` and *project package folder*.
  - **Project package** contains a `settings.py` file and other files.
- The `manage.py` script **has the same role as** the `django-admin` utility. It can perform everything that the `django-admin` utility does. However, using `manage.py` is **more straightforward**, especially if we are required to work on a single project.
- The `startapp` command is used to create a new app. An app is also represented by a folder of a specific file system.
  ```cmd
  > python manage.py startapp <app_name>
  ```
- Django manages the database operations with the **ORM technique**.
- Migration refers to **generating a database table whose** structure matches the data model declared in the app.
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
- `urls.py` defines the **URL patterns** for both the project and the app, **routing requests** to the appropriate view functions. Every time the client **browser requests a URL**, the Django server looks to **match its pattern** and **routes the application to the mapped view**.
- `asgi.py` is used by the application servers following the ASGI standard to **serve asynchronous web applications**.
- `wsgi.py` is the **entry point for** such **WSGI-compatible servers** to serve classical web application.

#### ORM Techinque

**ORM** stands for **Object-Relational Mapping**. It's a programming techinque used to **interact with a relational database** (like PostgreSQL, MySQL, or SQLite) **using objects** in a programming language **instead of writing raw SQL queries**.

ORM **automatically maps**:
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

#### WSGI

**WSGI** stands for **Web Server Gateway Interface**. It's a Python web standard (**specification**) that **defines how** Python **web applications communicate with web servers**.

**Before WSGI**, *every framework and server had its own protocol*, nothing was compatible. WSGI unified everything. It **allows any WSGI-compatible framework** (*Flask, Django <=2.1, Pyramid*) to **run on any WSGI-compatible server** (*Gunicorn, uWSGI, mod_wsgi*).

WSGI is **synchronous** and **designed for traditional** HTTP request/response cycles: no async, no WebSockets, no long-lived connections.

A **WSGI server** is a program that *implements the WSGI specification* and *runs a Python WSGI application*. It handles:
- receiving HTTP requests from clients.
- passing them to the Python application via the WSGI interface.
- returning the responses to the client.

#### ASGI

**ASGI** stands for **Asynchronous Server Gateway Interface**. It's also a Python web standard that defines how web servers comunicate with Python applications, similar to WSGI, but **designed for async use cases**.

**Mordern apps need** WebSockets, long-runing connections, non-blocking async I/O, concurrency without threads, so ASGI was created to **support both synchronous and asynchronous Python code**, including real-time features.

**ASGI is a specification**, not code. It **defines a common interface** between ASGI servers (e.g., *Uvicorn*) and ASGI applications (e.g., *FastAPI, Django 3+*).

An **ASGI server** is a program that *implements the ASGI specification* and *runs ASGI-compatible Python app*.

**ASGI is** the **modern Python web standard** for async apps.
- It **supports both** synchronous and asynchronous code.
- It **enables** WebSockets, streaming, and high concurrency.

#### Synchronous vs. Asynchronous Web Apps

- A **synchronous** web app **handles one request at a time** per worker, following a simple *request $\rightarrow$ process $\rightarrow$ response* pattern. Its characteristics:
  - **Blocking I/O**: while a request is being processed, the worker can't handle another.
  - **Thread/process based concurrency**: to handle more users, it needs to add more worker processes or threads.
  - **Straightforward code**: no `async`/`await`.
  - Great for CPU-bound or simple I/O-bound actions.
- An **asynchronous** web app **handles requests using an event loop**, allowing a single worker to server thousands of connections without blocking. Its characteristics:
  - **Non-blocking I/O**: tasks pause with `await` while waiting such as: Database I/O, HTTP calls, File system I/O, WebSockets.
  - **Concurrency through** `async`/`await`, not threads.
  - **Ideal for high-scale** or real-time applications.
- Async **shines when** we have **lots of waiting**, not lots of computing.

#### Concurrency vs. Parallelism

- **Simple definition:**
  - **Concurrency** = doing many things **seemingly** at the same time.
    - Tasks **overlap in time**.
    - A single worker switches between tasks.
    - Like multitasking.
  - **Parallelism** = doing many things **exactly** at the same time.
    - Tasks run **at the same instant**.
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
  - **Parallelism** helps with **CPU-bound tasks **like heavy computations, machine learning workloads, image processing, compression/encryption. Examples:
    - `multiprocessing`,
    - C-extension parallel code,
    - NumPy operations (internally parallel).

### Django-admin vs. manage.py commands

- Both can be used to **perform the same tasks**, but there are **some subtle differences**, and the choice of usage will depend on how we want to work on project.
- `django-admin` is Django's **command line utility** for administrative tasks. This utility is present **in the scripts folder** of the Django **environment directory**. Django admin utility is executed from inside the terminal.

  *It can also be launched via the call of module* `python -m django`.

- `manage.py` is a script that is the **local version** of Django admin and is located **inside the project folder**. It **sets** the Django settings module environment variable so that it **points to** our project `settings.py` file.
- `manage.py` is a file that **is automatically created** each time we create a Django project, it is **specific to** the virtual environment **of the project**.
- When working on a **single Django project**, developers tend to **use** `manage.py`.
- However, if we need to switch between **multiple Django settings files**, use the **Django admin command** with Django settings module or the settings command line option.

> `manage.py` is more convenient to use than `django-admin`. It runs inside the project folder. When using `django-admin`, you must set `--settings` variable to the required project's `settings.py` file.

### App structure

- An app is **responsible for performing one single task** out of the many involved in the complete web application, represented by the Django project.
- The `startapp` command option of the `manage.py` script creates a default folder structure for the app of that name.

  ```python
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

  **A view** is a **user-defined function** that's **called** when Django's **URL dispatcher identifies** the client's request URL and **matches** it with a URL pattern defined in the `urls.py` file.
- `models.py`. The **data models required** for processing in the app **are created** in this file.

  **A data model** is a Python **class based on** `django.db.models` class. All the models present here **are migrated** to the database tables.

### Web Framework

- Frameworks are **designed to support** the developer in building the web application.
- **The purpose** of a web framework is to make application **development easier** and to **provide** the developer with a **clean structure** that keeps things in order and allows for changes and modifications.
- Frameworks also allow for **code reusability** facilitated by existing code. They **provide a solid foundation** on which to build web application.
- A web application is spli into two parts:
  - **Front-end** is the part of the website that the **user interacts with** via web browser.
  - **Back-end** is the part that **runs on a web server** and usually contains a database.

#### Three-tier Architecture

- Architecture refers to the fundamental structures of a software system.
- Three-tier architecture is a modular based approach to client-server architecture that splits the application into three logical parts:
  - the **presentation tier** is the **layer the users primarily interact with** through user interfaces from their desktop, laptop, or mobile devices. It's **commonly built with a UI framework** or library such as React, and it **communicates** with other tiers **by sending results through** the application interface.
  - the **data tier** usually **consists of database servers** for storing and retrieving information.
  - the **application tier** is what **ties** together the other **two tiers**. It **gets data** from the presentation layer and **persists** it in the data tier.

#### MVC Architecture

- Most of the web frameworks implement the **MVC (Model-View-Control)** architecture.
- The MVC design pattern separates the entire web application development process into three layers: Model, View, and Controller.
  - The **Controller** intercepts the user requests. It **coordinates** with the View and Model layers to **send the appropriate response** back to the client.
  - The **Model** is responsible for **data definitions**, **processing logic** and **interaction** with the backend database.
  - The **View** is the **representation layer** of the application. It **takes care** of the **placement and formatting** of the result and **sends** it to the Controller, which in turn, redirects it to the client as the application's response.

#### MVT Architecture

- The Django framework adapts a **Model-View-Template (MVT)** approach, a slight variation of the MVC approach.
- A Django application consists of four following components:
  - **URL Dispatcher** is **equivalent to the Controller** in the MVC architecture. The `urls.py` module acts as the dispatcher. It **defines** the **URL patterns**. Each URL pattern is **mapped with a view function**.

    When the server receives a request in the client URL, the dispatcher matches its pattern with the patterns available in the `urls.py` module.

    It then routes the flow of the application toward its associated view.
  - The **View** function **reads** the path, query, and body parameters **included in** the client's request. It **uses** the client's and the model's data and **renders** its response using a template.

    *If required*, it uses this data to interact with the models to perform CRUD options.

    > *Django's View layer performs the role of Controller in MVC architecture.*
  - A **Model** is a Python class. An app may have one or more model classes, conventionally put in the `models.py` file.

    Django **migrates the attributes** of the model class **to construct a database table** of a matching structure.

    Django's ORM (Object Relational Mapper) helps perform CRUD operations in an object-oriented way instead of invoking SQL queries.
  - A **Template** is a web page **containing a mix of** static HTML and Django Template Language code blocks.

    Django's **template processor uses** any context data from the view inserted in these blocks to **formulate** a dynamic response.
