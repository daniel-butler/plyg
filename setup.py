from distutils.core import setup

setup(
    name='plyg',
    version='0.0.1',
    description='Clean structures to litter your code.',
    author='Daniel Butler',
    author_email='dabutler89@gmail.com',
    url='https://github.com/daniel-butler/plyg',
    packages=['plyg'],
    install_requires=['Click', 'pytest'],
    include_package_data=True,
    entry_points="""
    [console_scripts]
    plyg=plyg.main:cli
    """,
)
