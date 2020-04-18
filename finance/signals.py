from django.dispatch import Signal

new_total = Signal(providing_args=["Invoice","request","form"])