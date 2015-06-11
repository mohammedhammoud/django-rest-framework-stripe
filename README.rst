======================
django-stripe-payments
======================

Django REST Framework wrapper of the payments Django app for Stripe

* Forked (https://github.com/pinax/django-stripe-payments) and wrapped with Django REST Framework.
* All the templates is gone

Install
======================
* pip install django-rest-framework-stripe
* **Add to urls.py:** ``url(r"^api/stripe/", include("django_rest_framework_stripe.payments.api.urls")),``

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

Documentation can be found at http://django-stripe-payments.readthedocs.org
