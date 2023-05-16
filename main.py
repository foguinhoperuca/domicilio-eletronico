from kivy.lang import Builder

# from news_feed import NewsFeedApp
from panic import PanicApp


if __name__ == '__main__':
    Builder.load_file('marvel.kv')

    app = PanicApp()
    app.run()
