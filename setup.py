from setuptools import setup, find_packages

with open("README.md", "r") as file:
    long_description = file.read()

setup(
    name='find-temas',
    version='0.2',
    author="Jeferson Alves",
    author_email="ferreira.jefersonn@gmail.com",
    long_description=long_description,
    py_modules=['find-temas'],
    packages=find_packages(),
        classifiers=[
        "Programming Language :: Python :: 3",
    ],
    install_requires=[
        'Click',
        'pandas',
    ],
    entry_points='''
        [console_scripts]
        find-temas=find_temas.commandline:cli
    ''',
    python_requires='>=3.6',
)