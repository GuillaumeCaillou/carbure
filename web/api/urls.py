from django.urls import path

from . import views

urlpatterns = [
	# public, autocomplete api
	path('biocarburant-autocomplete/', views.biocarburant_autocomplete, name='api-biocarburant-autocomplete'),
	path('matiere-premiere-autocomplete/', views.matiere_premiere_autocomplete, name='api-matiere-premiere-autocomplete'),
	path('country-autocomplete/', views.country_autocomplete, name='api-country-autocomplete'),

    # private, producers
    path('producers/sample-lots', views.producers_sample_lots, name='api-producers-sample-lots'),
    path('producers/production-sites-autocomplete/', views.producers_prod_site_autocomplete, name='producers-api-production-sites-autocomplete'),
    path('producers/biocarburant-autocomplete/', views.producers_biocarburant_autocomplete, name='producers-api-biocarburants-autocomplete'),
    path('producers/mp-autocomplete/', views.producers_mp_autocomplete, name='producers-api-mps-autocomplete'),
    path('producers/ges/', views.producers_ges, name='producers-api-ges'),
    path('producers/settings/add-site', views.producers_settings_add_site, name='producers-api-settings-add-site'),
    path('producers/settings/add-certif', views.producers_settings_add_certif, name='producers-api-settings-add-certif'),
    path('producers/settings/add-mp', views.producers_settings_add_mp, name='producers-api-settings-add-mp'),
    path('producers/settings/add-biocarburant', views.producers_settings_add_biocarburant, name='producers-api-settings-add-biocarburant'),
    path('producers/attestation/<int:attestation_id>/lot/save', views.producers_save_lot, name='producers-api-attestation-save-lot'),


    # private, administrators
    path('administrators/users-autocomplete/', views.admin_users_autocomplete, name='admin-api-users-autocomplete'),
    path('administrators/entities-autocomplete/', views.admin_entities_autocomplete, name='admin-api-entities-autocomplete'),

]
