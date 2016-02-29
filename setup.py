from distutils.core import setup

setup(
    name='cronofy',
    version='0.0.5',
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
