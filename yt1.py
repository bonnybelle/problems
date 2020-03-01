
queue = [i for i in input('Input: ').split(' ')]


def my_lru_cache(max_size):
    def extended_cache(f):
        cache = {}

        def wrapper(*args, **kwargs):

            # for element in f(cache):
            for i in args:
                if i not in cache:
                    cache[args] = f(*args)
                else:
                    return args

            if len(cache) > max_size:
                cache.pop(0)

                # f(cache).append(element)
        return wrapper
    return extended_cache


#    def cache_clear():'
#        pass
#    wrapper.cache_clear = cache_clear
#    return wrapper
@my_lru_cache(int(input('Cache size: ')))
def list_input(queue):
    return queue


print(list_input(queue))
# list_input.cache_clear()
