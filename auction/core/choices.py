from django.db.models import TextChoices


class AuctionStatus(TextChoices):
    OPEN = 'O', "Open"
    DONE = 'C', "Close"


class ItemStatus(TextChoices):
    OPEN = 'N', "New"
    DONE = 'U', "Used"
