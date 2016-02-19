def no_safe_float(obj):
    return float(obj)


def safe_float(obj):
    try:
        return float(obj)
    except ValueError:
        pass


print '--------------'
print safe_float(1.1)
print safe_float('1.a')
print no_safe_float(1.1)
print no_safe_float('1.a')
print '--------------'
