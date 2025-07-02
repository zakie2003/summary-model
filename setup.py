# filepath: /home/zakie/Coding/Python/ML/summary-model/setup.py
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

__version__ = "0.1.0"

REPO_NAME = "summary-model"
AUTHOR_NAME = "zakie2003"
SRC_REPO = "text_summarization_with_transformers"
AUTHOR_EMAIL = "zk.khan2003@gmail.com"

setuptools.setup(
    name=REPO_NAME,
    version=__version__,
    author=AUTHOR_NAME,
    author_email=AUTHOR_EMAIL,
    description="A package for text summarization using transformer models.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_NAME}/{REPO_NAME}",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    install_requires=[],
)