import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"

REPO_NAME = "End-to-end-ML-Project-with-MLflow"
AUTHOR_USER_NAME = "entbappy"
SRC_REPO = "mlProject"
AUTHOR_EMAIL = "entbappy73@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author="MD_SHADAB_AHMED",
    author_email="ahmed11shadab@gmail.com",
    description="A small python package for ml app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{'MD_SHADAB_AHMED'}/{'End-to-end-ML-Project-with-MLflow'}",
    project_urls={
        "Bug Tracker": f"https://github.com/{'MD_SHADAB_AHMED'}/{'End-to-end-ML-Project-with-MLflow'}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)