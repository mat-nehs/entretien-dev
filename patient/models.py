import uuid
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


LEG_FRACTURE = "F"
HEMATOMA = "H"
SORE = "S"
ANKLE_SPRAIN = "A"
KNEE_SPRAIN = "K"


class Patient(models.Model):
    """Patient model."""
    WOUND_CHOICES = (
        (LEG_FRACTURE, 'Leg Fracture'),
        (HEMATOMA, 'Hematoma'),
        (KNEE_SPRAIN, 'Knee Sprain'),
        (SORE, 'Sore'),
        (ANKLE_SPRAIN, 'Ankle Sprain'),
    )
    secret_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(_("First name"), max_length=50)
    last_name = models.CharField(_("Last name"), max_length=50)
    birthdate = models.DateField(_("Birth date"), auto_now=False, auto_now_add=False, null=True, blank=True)
    wound = models.CharField(max_length=1, choices=WOUND_CHOICES, null=True, blank=True)
    emergency = models.BooleanField(_("emergency"), default=False)

    @property
    def fullname(self):
        """Return fullname."""

    @property
    def birthdate_formatted(self):
        """Return formatted date."""

    @property
    def age(self):
        """Get the patient's age."""

    @property
    def has_majority(self):
        """Patient is major."""

    def is_wounded(self):
        """Is the patient is wounded."""

    def break_his_leg(self):
        """Call this function to break patient leg."""