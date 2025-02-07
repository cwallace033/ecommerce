# Overview

This is a simple web app for a product that my wife sells on Amazon. To test it simply run python3 manage.py runserver. This will allow you to open the page on a web browser

I decided to write this program to become more familiar with how Django works in creating web apps. It also serves as a good template for to build an e-commerce store. 

[Software Demo Video](https://youtu.be/ZoiYzasW39M)

# Web Pages

There are currently two pages. The first is the home page. On this page there is a dynamically created product. The product image, product name, product description, product price, and add to cart button are all created dynamically. The testimonials are also dynamically generated. The second page is the cart page. This page has the same dynamically created elements with a remove button in place of the add to cart button. There is also a dynamically created total price. All of the dynamically created content is stored in a database. Django defaults to SQLite so that is what I used for this project. 

# Development Environment

This project was created in VS code. It, of course, uses python, html, css and javascript. The Django library was key to this project. 

# Useful Websites

* [Real Python](https://realpython.com/get-started-with-django-1/)
* [Django](https://docs.djangoproject.com/en/5.1/intro/tutorial01/)

# Future Work

* I want to add a checkout page to get user information
* I would also like to set up a user system that requires logging in to keep track of the items in the cart. 
