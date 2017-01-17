#

def tags(tag_name):
    def f_decorator(func):
        a = 1
        print(tag_name)
        def f_wrapper(text):
            print(text)
            return '<{tag_name}>{text}</{tag_name}>'.format(tag_name=tag_name, text=func(text, a=a))
        return f_wrapper
    return f_decorator




@tags('strong')
def get_text(text, **args):
    print(args.get('a'))
    return text

print(get_text('hello'))

