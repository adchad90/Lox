from setuptools import setup, find_packages

setup(
    name='lox',  # name of the package
    version='0.1.0',
    description='A secure CLI password manager',
    author='Aditya Chavan',
    author_email='iaditya.2016@gmail.com',
    packages=find_packages(),  # automatically finds 'password_manager' and submodules
    install_requires=[
        'cryptography',
        'pyperclip',
        'bcrypt'
    ],
    entry_points={
        'console_scripts': [
            'lox=lox.main:main',  # CLI command: lox
        ],
    },
    python_requires='>=3.7',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
)
