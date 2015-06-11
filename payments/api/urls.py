from django.conf.urls import patterns, include, url

import views

urlpatterns = patterns('',
    url(r'^current-user/$', views.CurrentCustomerDetailView.as_view(), name='stripe-current-customer-detail'),
    url(r'^subscription/$', views.SubscriptionView.as_view(), name='stripe-subscription'),
    url(r'^change-card/$', views.ChangeCardView.as_view(), name='stripe-change-card'),
    url(r'^charges/$', views.ChargeListView.as_view(), name='stripe-charges'),
    url(r'^invoices/$', views.InvoiceListView.as_view(), name='stripe-invoices'),
    url(r'^plans/$', views.PlanListView.as_view(), name='stripe-plans'),
    url(r'^events/$', views.EventListView.as_view(), name='stripe-events'),
    url(r'^webhook/$', views.WebhookView.as_view(), name='stripe-webhook'),
    url(r'^cancel/$', views.CancelView.as_view(), name='stripe-cancel'),
)