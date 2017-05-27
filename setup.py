from distutils.core import setup

setup(name='Michelangelo',
      version='0.1',
      description='Webpages analizer',
      author='Unlogical',
      author_email='sakujo8744@mail.ru',
      packages=['beautifulsoup4'],
      install_requires=['beautifulsoup4', 'langdetect'],
      tests_require=['pytest'])
