======================
django-rest-framework-stripe
======================

Django REST Framework wrapper of the payments Django app for Stripe

* Forked (https://github.com/pinax/django-stripe-payments) and wrapped with Django REST Framework.
* All the templates is gone

Install
======================
* pip install django-rest-framework-stripe
* Add 'payments' to INSTALLED_APPS
* **Add to urls.py:** ``url(r"^api/stripe/", include("payments.api.urls"))``

Endpoints
======================
* current-user/ (GET)
* subscription/ (GET/POST)
* change-card/  (GET/POST)
* charges/      (GET)
* invoices/     (GET)
* plans/        (GET)
* events/       (GET)
* webhook/      (POST)
* cancel/       (POST)

**ALL TEMPLATES AND AJAX VIEWS HAS BEEN REMOVED, USE ADDED ENDPOINTS**

Documentation can be found at http://django-stripe-payments.readthedocs.org
