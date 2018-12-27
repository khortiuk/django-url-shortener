import string
import random


def generate_key(instance):
    key = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(5))
    inst = instance.__class__
    if inst.objects.filter(key=key).exists():
        return generate_key(instance)
    return key
