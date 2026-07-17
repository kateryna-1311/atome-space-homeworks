from setuptools import find_packages, setup

setup(
    name="expense_bot",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "python-telegram-bot==21.3",
        "python-dotenv==1.0.1",
    ],
)
