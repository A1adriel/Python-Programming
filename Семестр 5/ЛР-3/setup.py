import setuptools

setuptools.setup(
    name="myspackage",  # УНИКАЛЬНОЕ имя на PyPI
    version="0.1.0",  # Версия - меняется при изменениях
    author="Sambuev Aldar",  # Ваше имя
    author_email="sambuev.2002@gmail.com",  # ДЕЙСТВУЮЩИЙ email (ОБЯЗАТЕЛЬНО)
    description="Flask MVC web application package",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/jamanuriyeva/JamasPackage",
    packages=setuptools.find_packages(),
    python_requires=">=3.8",
    install_requires=[
        "Flask>=2.0.0",
        "Jinja2>=3.0.0",
    ],
    entry_points={
        'console_scripts': [
            'https://github.com/A1adriel/Python-Programming/tree/main/Семестр%205/ЛР-3',
        ],
    },

)
