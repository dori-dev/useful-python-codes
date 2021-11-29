"""Custom Python Zip Function
"""


def custom_zip(*iterables):
    """custom zip function(like zip() in python)

    Yields:
        tuple: unit index of all iterables
    """

    sentinel = object()
    iterators = [iter(iterable) for iterable in iterables]

    while iterators:
        result = []

        for iterator in iterators:
            element = next(iterator, sentinel)
            if element is sentinel:
                return
            result.append(element)

        yield tuple(result)
