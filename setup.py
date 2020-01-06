from pathlib import Path
from distutils.core import setup

HERE = Path(__file__).parent
README = (HERE / 'README.md').read_text()


setup(
    name='plyg',
    version='0.0.1',
    description='Clean structures to litter your code.',
    long_description_content_type='text/markdown',
    long_description=README,
    author='Daniel Butler',
    author_email='dabutler89@gmail.com',
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
    url='https://github.com/daniel-butler/plyg',
    packages=['plyg'],
    install_requires=['Click', 'pytest'],
    include_package_data=True,
    entry_points="""
    [console_scripts]
    plyg=plyg.main:cli
    """,
)
