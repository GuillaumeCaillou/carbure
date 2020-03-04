from django.db import models

from core.models import Entity, MatierePremiere, TypeBiocarburant, Pays

class AttestationProducer(models.Model):
    producer = models.ForeignKey(Entity, on_delete=models.CASCADE)
    period = models.CharField(max_length=7, blank=False, null=False)
    deadline = models.DateField(blank=False, null=False)

    def __str__(self):
        return '%s - %s' % (self.period, self.producer.name)

    class Meta:
        db_table = 'producer_attestations'
        verbose_name = 'Attestation de Durabilité'
        verbose_name_plural = 'Attestations de Durabilité'	

class ProductionSite(models.Model):
    producer = models.ForeignKey(Entity, on_delete=models.CASCADE)
    name = models.CharField(max_length=64, blank=False, null=False)
    country = models.ForeignKey(Pays, null=False, on_delete=models.CASCADE)
    date_mise_en_service = models.DateField(null=False, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'producer_sites'
        verbose_name = 'Site de Production'
        verbose_name_plural = 'Sites de Production'	

class ProductionSiteInput(models.Model):
    ELIGIBLE_DOUBLE_COMPTAGE = [('Yes', 'Oui'), ('No', 'Non')]

    production_site = models.ForeignKey(ProductionSite, on_delete=models.CASCADE)
    matiere_premiere = models.ForeignKey(MatierePremiere, on_delete=models.CASCADE)
    eligible_double_comptage = models.CharField(max_length=3, choices=ELIGIBLE_DOUBLE_COMPTAGE, default='No')

    def __str__(self):
        return self.matiere_premiere

    class Meta:
        db_table = 'production_sites_input'
        verbose_name = 'Site de Production - Filiere'
        verbose_name_plural = 'Sites de Production - Filieres' 

class ProductionSiteOutput(models.Model):
    GES_OPTIONS = [('Default', 'Valeurs par défaut'), ('Actual', 'Valeurs réelles'), ('NUTS2', 'NUTS2')]

    production_site = models.ForeignKey(ProductionSite, on_delete=models.CASCADE)
    biocarburant = models.ForeignKey(TypeBiocarburant, on_delete=models.CASCADE)
    ges_option = models.CharField(max_length=12, choices=GES_OPTIONS, default='Default')

    def __str__(self):
        return self.biocarburant

    class Meta:
        db_table = 'production_sites_output'
        verbose_name = 'Site de Production - Biocarburant'
        verbose_name_plural = 'Sites de Production - Biocarburants' 

class ProducerCertificate(models.Model):
    CERTIF_STATUS_CHOICES = [("Pending", "En Attente de validation"), ("Valid", "Validé"), ("Expired", "Expiré")]
    producer = models.ForeignKey(Entity, on_delete=models.CASCADE)
    production_site = models.ForeignKey(ProductionSite, null=True, on_delete=models.CASCADE)
    expiration = models.DateField()
    date_added = models.DateField(auto_now_add=True)
    certificate = models.FileField()
    status = models.CharField(max_length=32, choices=CERTIF_STATUS_CHOICES, default="Pending")
    certificate_id = models.CharField(max_length=64, null=False, blank=False)

    def __str__(self):
        return self.certificate_id

    class Meta:
        db_table = 'producer_certificates'
        verbose_name = 'Certificat'
        verbose_name_plural = 'Certificats'	

