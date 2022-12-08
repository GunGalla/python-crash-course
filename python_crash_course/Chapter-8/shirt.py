# Упражнения 8.3 и 8.4

def make_shirt(size='L', text='I love Python!'):
    print(f"Shirt's size is {size}.")
    print(f"There must be the following text on the shirt: {text}.")


make_shirt('XXL', 'Hello, World!')
make_shirt(text='Hello, World!', size='XXL')
make_shirt()
