from distutils.core import setup
from cronofy import __version__

setup(
    name='cronofy',
    version= __version__,
    author='Derek Edwards',
    author_email='derek.edwards@coachlogix.com',
    packages=['cronofy', 'cronofy.test'],
    url='https://github.com/coachlogix/cronofy-python',
    license='MIT',
    description='Cronofy Python SDK',
    long_description='README.md',
    install_requires=[
        "requests >= 2.5.3"
    ],
)
