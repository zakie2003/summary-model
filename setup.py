import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


__version__ = "0.1.0"

REPO_NAME = "Text Summarization with Transformers"
AUTHOR_NAME = "zakie2003"
SRC_REPO= "text_summarization_with_transformers"
AUTHOR_EMAIL = "zk.khan2003@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_NAME,
    author_email=AUTHOR_EMAIL,
    description="A package for text summarization using transformer models.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=SRC_REPO
)