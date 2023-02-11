import pathlib
from setuptools import setup

# Каталог, содержащий этот файл
HERE = pathlib.Path(__file__).parent

# Текст файла README
README = (HERE / "README.md").read_text()

# Этот вызов setup() выполняет всю работу
setup(
    name="sal-square",
    version="3.0.0",
    description="Это приводит к возведению числа в квадрат",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/SalakhovaRum/sal-square",
    author="Rumiya",
    author_email="littleangel03@mail.ru ",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    packages=["square"],
    include_package_data=True,
    install_requires=[],
    entry_points={
        "console_scripts": [
            "square=square.__main__:main",
        ]
    },
)

