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
- [View](#view)
  - [Generic Views](#generic-views)
  - [HTTP](#http)
    - [HTTP Request](#http-request)
    - [HTTP Response](#http-response)
    - [HTTP Methods](#http-methods)
    - [HTTP Versions](#http-versions)
    - [HOL Blocking](#hol-blocking)
    - [HTTP Status Codes](#http-status-codes)
    - [HTTPS](#https)
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
    - [reverse Function](#reverse-function)
  - [Error Handling](#error-handling)
  - [Class-based Views](#class-based-views)
  - [Method Resolution Order (MRO)](#method-resolution-order-mro)


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

    > Django's View layer performs the **role of Controller** in MVC architecture.
  - A **Model** is a Python class. An app may have one or more model classes, conventionally put in the `models.py` file.

    Django **migrates the attributes** of the model class **to construct a database table** of a matching structure.

    Django's ORM (Object Relational Mapper) helps perform CRUD operations in an object-oriented way instead of invoking SQL queries.
  - A **Template** is a web page **containing a mix of** static HTML and Django Template Language code blocks.

    Django's **template processor uses** any context data from the view inserted in these blocks to **formulate** a dynamic response.


## View

- The **primary role** of the view function is to **fetch the data** from the client's request, **apply** a certain processing logic to it and **send an appropriate response** back to the client.
- It **receives** the request data in an object of class `HttpRequest`.
- The **return value** of the view function is a `HttpResponse` object containing the actual contents, the status code, and some header information.

### Generic Views
- Django make the view declaration process easier with its generic class-based view.
- The `django.views.generic` module contains serveral view classes that provide the functionality required to perform tasks such as rendering a template, showing an instance, showing the list of instances and so on.
- Some generic views are `TemplateView`, `CreateView`, `ListView`, `DetailView`, and `UpdateView`.

### HTTP

- HTTP stands for **HyperText Transfer Protocol**.
- HTTP is **a core operational protocol** of the world wide web. It **enables** a web browser to **comunicate** with a web server.
- HTTP is a **request-response** based protocol. It works with a **client -> request -> server -> response** cycle.
  - A client (web browser) sends the **HTTP request** to a server.
  - The web server sends the **HTTP response** back to the browser.
- HTTP is **used for almost all communication on the web**, including: loading web pages, APIs and webservices, file transfers, form submissions, and so on.
- It's a **stateless protocol**.
  - Each HTTP **request is independent**.
  - Servers do **not remember past requests** unless cookies or sessions are used.

#### HTTP Request

An example of a HTTP request:

  ```text
  GET / HTTP/1.1
  Host: developer.mozilla.org
  Accept-Language: en
  ```

A HTTP request **consists of:**
- a **method**, e.g., `GET`
- a **path** (*resource location*), e.g., `/`
- a **version**, e.g., `HTTP/1.1`
- **headers** *contain additional information* about the request and the client that is making the request. Headers can contain information **such as** the server name, the server port, the request method type, and the content type. **The content** of the header can **depend on** the specific client and server. Example:

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

- Following the header, the response will **optionally contain a message body** consisting of the response content, such as the HTML document, the image file, and so forth.

  ```html
  <html>
    <body>
      <p>Hello world!</p>
    </body>
  </html>
  ```

- **HTTP status code**, e.g., `200`, contained **within the header indicate** if the HTTP request successfully completed. The code values are in the range of 100-599 and are grouped by purpose.
- The **status message**, e.g., `OK`, is a text representation of the status code.

#### HTTP Methods

- HTTP mehod describes the **type of action** that client wants to perform and **comunicates** it to the server.
- The primary or the **most commonly used** HTTP methods are: `GET`, `POST`, `PUT`, `PATCH`, and `DELETE`.
- `GET` method:
  - is used to **retrieve information** from the given server.
  - is **safe**. It does *not change* server data.
  - is **idempotent**. The *same request* yields the *same result*.
  - data is **sent in the URL** (*query string*).
  - should **not be used** for **sensitive** data.
  - **example:** the following request **retrieves** user with id `5`.

    ```text
    GET /users/5
    ```
- `POST` method:
  - is used to **create new data** on the server.
  - is **NOT idempotent**. Sending a same request twice may create duplicates.
  - data is **sent** in the **body**.
  - is **used for** new submissions, uploads, form data.
  - **example:** the following request **creates** a new user.

    ```text
    POST /users
    {
      "name": "John"
    }
    ```
- `PUT` method:
  - is used to **fully update** an existing resource.
  - is **idempotent**. The *same request* yields the *same result*.
  - **replaces** the **entire resource unless** implemented otherwise.
  - must include the **full updated data**. If *any field is missing*, it may be overwritten or remove.
  - **example:** the following request **replaces** user with id `5` with the provided data.

    ```text
    PUT /users/5
    {
      "name": "John",
      "age": 25
    }
    ```
- `PATCH` method:
  - is used to **partially update** the resource. It tells the server to *update only* the provided fields.
  - is **idempotent**. The *same request* yields the *same result*.
  - **example:** the following request **updates only** the `age` of the user with id `5`.

    ```text
    PATCH /users/5
    {
      "age": 25
    }
    ```
- `DELETE` method:
  - is used to **remove a resource**.
  - is **idempotent**. Deleting the *same item repeatedly* gives the *same result*.
  - **removes data** from the server.
  - **example:** the following request **deletes** the user with id `5`.

  ```text
    DELTE /users/5
  ```

> **Note** that HTTP methods are **only conventions**, not enforcement. The developer's **code determines** whether the operation is actually **idempotent**.

#### HTTP Versions

The three most commonly used HTTP versions are `HTTP/1.1`, `HTTP/2`, and `HTTP/3`.

- `HTTP/1.1`
  - **text-based** protocol. It means **messages** are written in **human-readable** plain text.
  - **one request** per TCP connection (unless using `keep-alive`).
  - if one request is **delayed**, others are blocked due to **HOL** (*Head-of-Line*) **blocking**. Browsers open many parallel TCP connections to compensate.
  - **pros:**
    - simple, widely supported.
    - **works everywhere**, even on very old systems.
  - **cons:**
    - **significant latency** with many small resources (e.g., *100+ assets* per page).
    - inefficient for modern web workloads.
- `HTTP/2`
  - **binary framing** layer. It means the protocol **uses structured binary data frames** (*machine-readable packages*) instead of text. It's **more compact** than text and is **faster** to parse.
  - **multiplexing:** multiple simultaneous streams over a single TCP connection.
  - **header compression** (HPACK): smaller request $\rightarrow$ faster transfers.
  - stream prioritization.
  - **faster** than HTTP/1.1 **when** network quality is good.
  - **still suffers** from TCP-level HOL blocking:
    - if packets are lost, the **entire connection stalls**.
    - **multiplexing doesn't help** because they share one TCP connection.
  - **pros:**
    - low latency.
    - more efficient for complex sites.
    - widespread support.
  - **cons:**
    - performance **drops significantly** on mobile or unstable networks.
- `HTTP/3`
  - **binary framing** layer.
  - runs over **QUIC**, which is built on **UDP** instead of TCP.
  - **QUIC** includes:
    - built-in **TLS 1.3** encryption.
    - stream-level flow control.
    - **connection migration**. Keep connection **alive when IP changes**, helpful for mobile.
  - no TCP HOL blocking $\rightarrow$ **stream are independent**.
  - **faster connection setup:**
    - no separate TCP + TLS handshake.
    - often **0-RTT** (zero round-trip time) **startup**.
  - handles packet loss gracefully.
  - **pros:**
    - **best** for modern mobile networks.
    - **extremely fast** in high-latency environments.
    - **robust when switching** networks, e.g., Wi-Fi $\rightarrow$ mobile data.
  - **cons:**
    - **still rolling out** globally.
    - firewalls and enterprise networks sometimes **block UDP**.

#### HOL Blocking

- HOL blocking stands for **Head-Of-Line Blocking**.
- It is **a performance problem** that occurs in network protocols when **one slow** or lost packet **blocks all the packets behind** it, even if those later packets could otherwise have been processed.
- In `HTTP/1.1`
  - each TCP connection handles **one request at a time**.
  - if **one request is slow**, every request behind it in that connection **waits**.
  - browsers opent many parallel connections to reduce this problem.
- In `HTTP/2`
  - **supports multiplexing**, multiple streams on one connection.
  - **still uses TCP**, which has packet-level HOL blocking:
    - if **one TCP packet is lost**, TCP must wait and retransmit it.
    - **all HTTP/2 streams** on that connection **pause until** the packet is recovered.
- In `HTTP/3`
  - **No** TCP HOL blocking.
  - uses **QUIC, built on UDP**, handles **streams independently**.
  - if **one packet is lost**:
    - only the **affected streams waits**.
    - all **other streams continue** normally.
- HOL blocking **makes website slower** because:
  - a **single lost** packet **affects all streams**, requests behind it.
  - **high-latency** or mobile networks suffer more.
  - **performance degrades** for real-time or resource-heavy website.
- **TCP has HOL blocking** because:
  - TCP **enforces strict, in-order delivery**.
  - **treats the connection as one** continuous byte stream.
  - if one packet is lost $\rightarrow$ whole connection halts.
- **QUIC solves** TCP's connection-wide **HOL blocking problem**:
  - built-on UDP $\rightarrow$ QUIC **controls** ordering + reliability **itself**.
  - multiple **independent streams** inside one connection.
  - packet loss **affects only** the stream involved.

#### HTTP Status Codes

- HTTP status codes are **three-digit numbers** that a web **server sends** back **in** an **HTTP response** to **tell the client** (browser, app, API, etc.) **what happened** to its request.
- They are grouped into **five categories**, each representing a different class of response.
- **1xx - Informational** indicates that the request **was received** and is **still being process**. The **most common informational responses** are:
  - **100 Continue:** server acknowledges request headers, client can send body.
  - **101 Switching Protocols:** server is switching protocols, e.g., to WebSocket.
  - **102 Processing:** server **is working** but not finished. It's **not a final** response, it's **sent before** the final status code to **prevent** the client from **timing out** while the server is doing something that takes a long time, *e.g.,* large file operations, deep searches, etc.
- **2xx - Success** indicates that the request **was successfully processed** by the server. The **most common success responses** are:
  - **200 OK:** standard success response.
  - **201 Created:** a new resource was created, e.g., after `POST`.
  - **202 Accepted:** the server **acccepted the request**, but **has not processed** it yet and **may process it later**. It's often used in APIs, **for asynchronous processing** (background jobs).
  - **204 No Content:** success, but no response body, common for `DELETE`.
- **3xx - Redirection** indicates to the client that **the requested resource** has **been moved to a different path**. Browsers, and most HTTP clients **automatically follow new URL** unless users explicitly disable that behavior. The **most common redirection responses** are:
  - **301 Moved Permanently:** resource moved to a new permanent URL, **method might change**.
  - **302 Found:** temporary redirect, **method might change**.
  - **304 Not Modified:** client can use a cached version.
  - **307 Temporary Redirect:** like 302, but **method must not change**.
  - **308 Permanent Redirect:** like 301 but **method must not change**.
- **4xx - Client Errors** indicates that the client made a bad request. The **most common client errors responses** are:
  - **400 Bad Request:** the request was malformed.
  - **401 Unauthorized:** authentification is required.
  - **403 Forbidden:** authentification OK, but access denied.
  - **404 Not Found:** resource not found.
  - **405 Method Not Allowed:** request method not allowed. It means the server **understands the method** but that method is **not allowed for** this specific resource.
  - **409 Conflict:** resource conflict, e.g., duplicate data.
  - **429 Too Many Requests:** rate limiting.
- **5xx - Server Errors** indicates that the server failed to process a valid request. The **most common server errors responses** are:
  - **500 Internal Server Error:** generic server failure. It means the **server encountered** an **unexpected condition** and could **not fulfill** the request.
  - **501 Not Implemented:** server doesn't support the requested method. It means the server does **NOT recognize** the method.
  - **502 Bad Gateway:** indicates a **problem between servers**. A server acting as a **gateway or proxy** received an **invalid response** from an upstream server.
  - **503 Service Unavailable:** server overloaded or down for maintaince.
  - **504 Gateway Timeout:** upstream server didn't respond in time.

#### HTTPS

- HTTPS stands for **HTTP Secure**.
- Uses **SSL/TLS encryption**.
  - **SSL (Secure Sockets Layer)** is **deprecated** and insecure now. SSL is **completely disabled** in modern browsers, severs.
  - **TLS (Transport Layer Security)** is the *newer and current* security protocol. **Only TLS 1.2 and TLS 1.3** are recommended today.
- **Data is encrypted**, so attacker can't read or tamper with it.
- **Requires** an **SSL/TLS certificate** issued by a **trusted Certificate Authority** (CA).
- **Ensures data integrity**. Information arrives unchanged.
- **Protects** user privacy by **encrypting all transmitted data**.
- **How HTTPS works:**
  1. client $\rightarrow$ server: "Hello!". When we visit a HTTPS site, the browser **sends** the server a **hello message** which **contains**:
     - **supported encryption** methods,
     - **supported TLS** versions,
     - a **random number**, used to generate keys later.
  2. server $\rightarrow$ client: "Here's my certificate". The server **replies** with a message which **contains**:
     - its **SSL/TLS certificate**,
     - its **public keys**,
     - a **random number** of its own.
  3. the browser **checks** if the **certificate** is **valid and trusted**, then **creates a session key**:
     - **generates** a **secret symmetric key**.
     - **encrypts** this key **with** the **server's public key**.
     - **sends it back** to the server. **Only** the **server can decrypt** this because it has the private key.
  4. **secure encrypted tunnel is establish.**
      - Now, **both** browser and server **share** the same **secrete session key**.
      - They **use symmetric encryption** to **exchange data** securely.
  5. **encrypted data transfer begins.** Every request/response is encrypted: URLs (except domain), cookies, form data, API calls, headers (partially).

### Request and Response Objects

- Django **handles** the request and response **with the help of** `HttpRequest` and `HttpResponse` classes in the `django.http` module.
- Django **obtains** the `HttpRequest` object **from the context provided** by the server.
- As a client's **request received**, Django's **URL dispatcher** mechanism **invokes a view** that matches the URL pattern **and passes** this `HttpRequest` object **as the first argument** so that all the request metadata is available to the view for processing.

#### HttpRequest Object

The `HttpRequest` object **contains** metadata about the **client's request**, including method, GET and POST parameters, cookie, and user information. Some of the **main attributes and methods** of an `HttpRequest` object (`request`) are:

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

URL stands for **Uniform Resource Locator**. It's simply an address where the files are stored. For example,
- `https://www.littlelemon.com/customers/5`.
- `https://www.littlelemon.com/menu/?year=2022`.

A URL is made up of multiple parts put together:
- **scheme** or referred as the **protocol** is located at the beginning of any url address and can be identified as `http` or `https`. The protocol **determines the set of rules** around the transmission and exchange data.
- **subdomain** is **located before the domain** and usually contains the home page and other important pages. The **most common subdomain** is World Wide Web represented by `www`.
- **domain**, e.g., `littlelemon.com`, consists of two parts:
  - **second level domain** refers to an organization or the name of a company. e.g., `littlelemon`.
  - **top level domain** is used to reference a country or category of the organization. e.g., `.com` address can indicate a comercial entity.
- **path** also known as the **page path** directs the user to the **location of a resource**. e.g., `/customers/5`, `/menu`.
- **query string** begins with a question mark symbol `?` and is **placed after** the URL path. It **contains parameters** represented as **key value pairs**. e.g., `?year=2022`.

### Parameters

The view function in Django **receives** its **mandatory argument** as the **request object** from the server context. The client **may pass additional arguments** via different methods.

#### Path Parameter

- A path parameter is **a variable part** of the URL that is **used to identify a specific resource**, such as `/customers/5`, where `5` is an argument of the path parameter.
- There may be **multiple path parameters** in the URL, separated by the **path separtor**, the slash symbol `/`.
- **How it works:**
  - The URL dispatcher **maps the pattern to** the view function and identifies `5` as the customer id `cust_id` parameter.

    ```python
    path("custmers/<int:cust_id>/", views.customers, name = "customers"),
    ```
  - The parameter **is parsed as** `cust_id` parameter and **picked** by the `views.customers()` function. The view `customers` function needs an **additional parameter** `cust_id`, as shown in the following example, because an **argument was passed** inside the `urls.py` file.

    ```python
    def customers(request: HttpRequest, cust_id: int):
      pass
    ```
  - The **parameter names** added inside the `path` function in the `urls.py` file **must match the ones added** inside the `customers()` view function associated with it in the `views.py` file. The parameters **order isn't important**.

#### Path Converters

- The URL pattern treats the **identifiers in angular brackets** `<>` as the path parameters.
- **By default**, it **parses** the received **value to** the **string type**.
- Path parameters avaiblable are:
  - `str`: matches any **non-empty string** and **excludes** the path separator `/`. This is the default if a converter isn't included in the expression.
  - `path`: matches any **non-empty string** and **includes** the path separator `/`.
  - `int`: matches **zero or any positive** integer and **returns** an `int`.
  - `uuid`: matches a formatted UUID and **returns** a UUID instance.
  - `slug`: matches any slug string consisting of ASCII letters or numbers, **including** the hyphen and underscore characters.

#### Query Parameter

- A query string is a **sequence** of one or more **key-value pairs** concatenated by the ampersand symbol `&`. They're added to the URL **after** a question mark symbol `?`.

  For example: `https://www.littlelemon.com/customers/name=John&age=35`
- The URL dispatcher **doesn't parse** these parameters. They **are fetched** by the view function **from** the request object it receives.
- The key-value pairs in the query string **are added** to the `request.GET` property. The request object's `GET` property is a **dictionary-like** object. Hence, values can be get as shown in the following example.

  ```python
  def customers(request: HttpRequest):
    name = request.GET.get("name")
    age = request.GET.get("age")
  ```

#### Body Parameter

- Body parameters are data sent in the **body of** a `POST` request, **typically** from an **HTML form**, which is not visible in the URL.
- Values can be get via request object's `POST` progerty, as demonstrated below.

  ```python
  def customers(request: HttpRequest):
    name = request.POST.get("name")
    age = request.POST.get("age")
  ```

### URL Dispatcher

- URL dispatcher is Django's **mechanism** that **uses patterns** that are defined by URL mapping in `urls.py` **to route request** to the correct view.
- **How it works:**
  1. a **request comes** in, e.g., `/customers/5/`.
  2. Django **removes** the domain name and leading slashes.
  3. URL dispatcher **looks** at the `urlpatterns` list in `urls.py` file(s).
  4. It checks each pattern, from **top to bottom**.
  5. The **first matching pattern** triggers the **corresponding view**.
  6. Django **calls** that view and **returns** the response.

#### URL Mapping

- URL mapping is a **set of URL patterns** that **are defined** in `urls.py` file(s). It's a list of instruction or **a table of routes**.
- **Components** of URL mapping:
  1. **URL patterns:** written in `urls.py` using `path()` or `re_path()` function.
  2. **Views:** functions or classes that handle the request.
  3. **Arguments / Parameters:** dynamic segments like `<id>` or `<slug>`.
  4. **Names:** each URL can be given a `name` **for reverse** URL lookup.
- **Example** of a URL mapping:

  ```python
  path("article/<int:year>/<slug:title>/", views.article, name="article")
  ```

#### Regular Expressions in URLs

- Regular expressions are used to **define**, extract, and validate **dynamic URL paths** before they are sent to the associated view function.
- To **use regular expressions** in URLs, it needs to **import and use** the `re_path()` function from the `django.urls` module.
- Example:

  ```python
  from django.urls import path, re_path

  from . import views


  urlpatterns = [
    path("menu_item/10/", views.display_menu_item, name="static_path"),
    path("menu_item/<int:id>/", views.display_menu_item, name="dynamic_path"),
    re_path(r"^menu_item/([0-9]{2})/$", views.display_menu_item, name="regex_path"),
  ]
  ```

#### URL Pattern Convention

Django follows a convention similar to directory in Unix:
- ending pattern with a **trailing slash**: to look like a "container" endpoints. For example, `"menu_item/10/"`.
- **NOT include** a leading slash.

Django by default redirects URLs like `example.com/menu_item/10` to `example.com/menu_item/10/`. Hence, the pattern `menu_item/10/` works with both `example.com/menu_item/10` and `example.com/menu_item/10/`, but `menu_item/10` doesn't work with `example.com/menu_item/10/`.

Django does not expect leading slash, so `/menu_item/10/` won't match `example.com/menu_item/10/`.

**Rule of thumb: never use** leading slash, **use trailing slash** to keep consistency.

#### URL Namespacing

- The **application namespace** is created **by defining** `app_name` variable in the applications's `urls.py` module and assigning it the name of the app.
- Django **differentiates** between **same-name URLs** in multiple apps with application namespace.
- The `app_name` defines the **application namespace** so that the views in this app are identified by it.

  ```python
  >>> reverse("demoapp:index")
  "/demo/"
  ```
- We can also **define** the **instance namespace** in the `include` function **while adding** an app's `urlpatterns`.

  ```python
  urlpatterns = [
    path("demo/", include("demoapp.urls", namespace="demoapp"))
  ]
  ```

#### reverse Function

- `reverse()` function **does the opposite** of URL matching. It **takes** a URL name (and optionally parameters) and **returns** the **actual URL path** as a string.
- It's **useful to:**
  - **avoid hard-coding URLs** as strings.
  - **keep URLs consistent** even if our URL patterns change.
  - help when **generating links** inside views, models, forms, etc.
- Example:
  - URL name is defined in the `urls.py` module.

    ```python
    path("menu/<str:dish>/<int:menu_id>/", views.menu_items, name="menu_items")
    ```
  - Using `reverse()` function in the `views.py` module to get the actual URL path.

    ```python
    from django.urls import reverse

    url = reverse("menu_items", kwargs={"name": "pasta", "menu_id": 10})
    print(url)  # /menu/pasta/10/
    ```
- The `reverse()` function is **commonly used:**
  - **in views** to redirect.

    ```python
    from django.shortcuts import redirect
    from django.urls import redirect

    return redirect(reverse("homepage"))
    ```
  - **in templates**, indirectly via `{% url %}`.

    ```html
    <a href="{% url 'homepage' %}">Home</a>
    ```
  - in Django REST framework **when** building hyperlinks.

### Error Handling

Django has a **built-in error handling system** that helps us manage exceptions, return proper error pages, and debug applications.
- Django's **built-in error views:** Django automatically **provides** default pages for **common HTTP errors** such as 400, 403, 404, 500.
  - When `DEBUG = True` (**development mode**), Django shows a **detailed debug page** with traceback, request info, environment variables, template context.
  - When `DEBUG = False` (**production mode**), Django shows **simple** public-facing error pages (`400.html`, `403.html`, etc.)
- **Custom error pages:** we can override Django's default error pages by creating templates in the project `/templates` folder:

  ```text
  templates/400.html
  templates/403.html
  templates/404.html
  templates/500.html
  ```
- **Custom error handlers**: We may define customer view functions to handle errors in the `urls.py` module at the project level.

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
- **Inside views:** we can **return** a `HttpResponse` or **raise** an exception. For example,
  - returns a `HttpResponseNotFound`, which is a **subclass of** `HttpResponse` that specifically indicates a 404 error. It internally **sends** an error code `404`. Other **predefined subclasses** include `HttpResponseBadRequest` and `HttpResponseForbidden`.
  - **raises** a `Http404` exception, which is a class defined in the `django.core.exceptions` module. Some **important exception types** are: `ObjectDoesNotExist`, `EmptyResultSet`, and `FieldDoesNotExist`.

### Class-based Views

- Class-based views are **views written as classes**, instead of functions (*function-based views*).

  Example:
  ```python
  # views.py
  from django.views import View
  from django.http import HttpRequest, HttpResponse


  class HomeView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
      return HttpResponse("Hello world!")


  # urls.py
  from django.urls import path
  from .views import HomeView

  urlpatterns = [
    path("home/", HomeView.as_view(), name="home")
  ]
  ```
- Class-based views **repond** to HTTP requests using class **instance methods:** `get`, `post`, `put`, `delete`, `patch`.
- They allow to **structure view logic** in an **object-oriented way**, making code more **reusable**, **organized**, and **extensible**.
  - **code reusability:** we can **create base classes** and let other views **inherit** behavior.
  - **cleaner** and **orgnized code:** logic is **grouped into class methods** instead of long function-based views.
  - **extensiblity:** we can override just the parts we need.
- Django provides many **built-in generic views** such as `ListView`, `DetailView`, `CreateView`, `UpdateView`, `DeleteView`, `FormView`.
- Class-based views **allow** inheritance and **mixins**.
  - A mixin is a class **designed to be inherited alongside another** class to **add extra features**, but **not mean to stand alone**.
  - Mixins are **reusable**, contain **small, focused logic**, allow to **combine behaviors** cleanly.
  - When using mixins, always place them **before** the view class so that Python's **MRO (Method Resolution Order)** to find the mixin methods first.

    Example:
    ```python
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
- **The choice** of function-based views and class-based view **depends on** complexity, reusability, and clarity.
  - if the view is **simple** $\rightarrow$ use function-based views.
  - if the view is **complex or reusable** $\rightarrow$ use class-based views.
- **Use function-based views when:**
  - **simple view:** returns a template, handles one request method, has straightforward behavior.
  - no need for inheritance, need **maximum transparency and control**.
  - the view is **small and not reused**.
  - prefer **direct control**.
- **Use class-based views when:**
  - need to **handle multiple HTTP methods** cleanly.
  - want to **reuse or extend** behavior.
  - **using generic views** such as `ListView`, `DetailView`, `CreateView`, `UpdateView`, `DeleteView`, `FormView`.
  - need **cleaner, structured** code. Class-based views break behavior into clear override-able methods.
  - **need mixins:** authentication, permissions, etc.

### Method Resolution Order (MRO)

- **Method Resolution Order (MRO)** is the **rule** that Python uses **to decide** which class's method/attribute gets **called first** when multiple classes are involved, especially **in multiple inheritance**.
- **MRO becomes important** when:
  - a class inherits from **multiple parent classes**.
  - two **parents contains** a method with the **sasme name**.
  - mixins are used.
  - want to know which `super` method is called next.
- **MRO decides** the search path Python will follow.

  Example:
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
  Even though the `C` class inherits from both `A` and `B` classes. Both of them have the `hello` method, Python chooses the one of `A`, not `B`. That decision is **based on the MRO**.
- The built-in `mro` method is used to see the MRO. For example, `C.mro()` returns the following list, that is the **exact search order** Python uses.

  ```python
  [
    <class '__main__.C'>,
    <class '__main__.A'>,
    <class '__main__.B'>,
    <class 'object'>
  ]
  ```
- Python **uses** an algorithm called **C3 Linearization** to **determine MRO**:
  - **Preserve the order** of inheritance.
  - **Respect MRO** of parent classes.
  - **Avoid** inconsistency and conflicts.
  - Guarantee a **single, predictable** path (linear).
