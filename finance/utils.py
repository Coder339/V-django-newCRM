import random
import string


def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def unique_cust_sno_generator(instance):
    cust_new_id= random_string_generator()

    Klass= instance.__class__

    qs_exists= Klass.objects.filter(order_id= cust_new_id).exists()
    if qs_exists:
        return unique_cust_sno_generator(instance)
    return cust_new_id