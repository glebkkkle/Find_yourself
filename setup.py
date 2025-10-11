from setuptools import setup, find_packages

setup(
    name="find_yourself",
    version="0.1",
    packages=find_packages(),  # automatically finds 'src' package
    install_requires=[
        "streamlit",
        "llama-cpp-python",
        "Pillow",
        "requests",
 
    ],
)