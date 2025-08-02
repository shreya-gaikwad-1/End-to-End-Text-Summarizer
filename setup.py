import setuptools

with open("README.md", "r", encoding = "utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"     

REPO_NAME = "End-to-End-Text-Summarizer"
AUTHOR_USER_NAME = "shreya-gaikwad-1"
SRC_REPO = "textSummarizer"
AUTHOR_EMAIL = "shreyagaikwad6205@gmail.com"

#Looks for constructor file in every forlder and creates a local package

setuptools.setup(
    name = SRC_REPO,
    version = __version__,
    author = AUTHOR_USER_NAME,
    author_email = AUTHOR_EMAIL,
    description = "A small python package for text summarization",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls = {
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues"
    },
    package_dir = {"": "src"},
    packages = setuptools.find_packages(where = "src")
)
