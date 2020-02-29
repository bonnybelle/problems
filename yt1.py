queue = [i for i in input('Input: ').split(' ')]


def decorator(f):
    max_size = int(input('Cache size: '))
    cache = {}

    def wrapper(*args):
        # for element in f(cache):

        if args not in cache:
            cache[args] = f(*args)
        else:
            return args
        if len(cache) > max_size:
            cache.pop(0)

            # f(cache).append(element)

    return wrapper


#    def cache_clear():'
#        pass
#    wrapper.cache_clear = cache_clear
#    return wrapper
@decorator
def list_input(queue):
    return queue


print(list_input(queue))
# list_input.cache_clear()
