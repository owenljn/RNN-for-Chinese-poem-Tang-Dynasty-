from poetry_model import PoetryModel


if __name__ == '__main__':
    poetry = PoetryModel()
    poem = poetry.gen(poem_len=50)
    print(poem)