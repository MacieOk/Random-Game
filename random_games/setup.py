from setuptools import setup, find_packages

setup(
    name='random_games',
    version='1.0',
    description='A Python library for generating Young tableaux and performing Jeu de Tacquin simulations.',
    author='Maciej Hendzel',
    author_email='maciej.hendzel@gmail.com',
    packages=find_packages(include=['random_games', 'random_games.*']),
    install_requires=[
        'numpy',
        'matplotlib'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
