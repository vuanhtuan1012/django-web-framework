# Django Web Framework  <!-- omit in toc -->

- [Introduction to Django](#introduction-to-django)
  - [HTML vs. HTML5](#html-vs-html5)
    - [Definition](#definition)
    - [Key Differences](#key-differences)
  - [Vitual Environment](#vitual-environment)


## Introduction to Django

### HTML vs. HTML5

#### Definition

- **HTML** (Hyper Text Markup Language) is the **standard language for structuring** web pages.
- **HTML5** is the **newest version** of HTML, adding modern features for today's web.

#### Key Differences

- HTML5 **introduced semantic tags** such as `<header>`, `<footer>`, `<nav>`, `<section>`, `<article>`, `<aside>`, so browsers and developers understand page structure better, improve code readability. Since these tags have **built-in meaning**, they tell the browser (and developers, screen renders, search engines) **what the content represents**.
  - `<header>` → top of a page or section.
  - `<nav>` → navigation menu.
  - `<article>` → self-contained content (blog post, news article, post).
  - `<section>` → logical grouping of related content.
  - `<aside>` → sidebar or related info.
  - `<footer>` → bottom of a page or section.
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