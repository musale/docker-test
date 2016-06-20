from django.db import models


class Broker(models.Model):
    name = models.CharField(u'Name of Broker', max_length=250, null=True, blank=True)
    contact = models.CharField(u'Contact of Broker', max_length=250, null=True, blank=True)

    def __unicode__(self):
        return '{0}'.format(self.name)

    class Meta:
        verbose_name = 'Broker'
        verbose_name_plural = 'Brokers'


class GarbagePoint(models.Model):
    """
    Area which garbage is being collected
    """
    BIGPAPER = 'BIG PAPER'
    SMALLPAPER = 'SMALL PAPER'
    PAPER_SIZES = (
        (BIGPAPER, BIGPAPER),
        (SMALLPAPER, SMALLPAPER),
    )
    location = models.CharField(u'Name of Location', max_length=250, null=True, blank=True)
    type_of_location = models.CharField(u'Type of Location', max_length=250, null=True, blank=True)
    person_in_charge = models.CharField(u'Person in Charge', max_length=250, null=True, blank=True)
    contacts = models.CharField(u'Contacts', max_length=250, null=True, blank=True)
    paper_size = models.CharField(u'Paper Size', max_length=250, null=True, blank=True, choices=PAPER_SIZES)
    number_of_papers = models.CharField(u'Number of Papers', max_length=250, null=True, blank=True)
    created_at = models.DateTimeField(u'Creation Date', auto_now=True)
    updated_at = models.DateTimeField(u'Update Date', auto_now_add=True)

    def __unicode__(self):
        return "{0}::{1}".format(self.location, self.type_of_location)

    class Meta:
        verbose_name = 'Garbage Collection Area'
        verbose_name_plural = 'Garbage Collection Areas'


class Cost(models.Model):
    """
    A cost incurred by the garbage man
    """
    name = models.CharField(u'Name of Cost', max_length=250, null=True, blank=True)
    description = models.CharField(u'Description', max_length=250, null=True, blank=True)
    amount = models.DecimalField(
        u"Amount",
        max_digits=9,
        decimal_places=2,
        default=00.00
    )
    created_at = models.DateTimeField(u'Creation Date', auto_now=True)
    updated_at = models.DateTimeField(u'Update Date', auto_now_add=True)

    def __unicode__(self):
        return '{0} {1} {2}'.format(self.name, self.description, self.amount)

    class Meta:
        verbose_name = 'Cost'
        verbose_name_plural = 'Costs'


class Collection(models.Model):
    """
    A garbage collection made
    """
    PAID = 'PAID'
    UNPAID = 'UNPAID'
    PAYMENT_CHOICES = (
        (PAID, PAID),
        (UNPAID, UNPAID)
    )
    collection_area = models.ForeignKey(GarbagePoint, related_name="collection_area")
    broker = models.ForeignKey(Broker, related_name="broker", blank=True, null=True)
    payment_status = models.CharField(u'Payment Status', max_length=250, null=True, blank=True, choices=PAYMENT_CHOICES,
                                      default=UNPAID)
    amount = models.DecimalField(
        u"Amount",
        max_digits=9,
        decimal_places=2,
        default=00.00
    )
    created_at = models.DateTimeField(u'Creation Date', auto_now=True)
    updated_at = models.DateTimeField(u'Update Date', auto_now_add=True)

    def __unicode__(self):
        return '{0} {1} {2}'.format(self.collection_area, self.created_at, self.updated_at)

    class Meta:
        verbose_name = 'Collected Garbage Record'
        verbose_name_plural = 'Collected Garbage Records'
