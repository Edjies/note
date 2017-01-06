#

def tags(tag_name):
    def f_decorator(func):
        def f_wrapper(text):
            print('abc')
            return '<{tag_name}>{text}</{tag_name}>'.format(tag_name=tag_name, text=text)
        return f_wrapper
    return f_decorator


def empty_decorator(func):
    def f_wrapper(text):
        return func(text)
    return f_wrapper


@tags('p')
@empty_decorator
@tags('strong')
def get_text(text):
    return text


print(get_text('hello'))