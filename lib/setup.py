from setuptools import setup, find_packages
import os

# Get the long description from the README file
here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, '..', 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="n8n_utils",
    version="0.1.0",
    packages=find_packages(where='.'),
    package_dir={'': '.'},
    install_requires=[
        "jsonschema>=4.0.0",
        "networkx>=2.6.3",
        "matplotlib>=3.4.3",
        "click>=8.0.0",
        "python-dotenv>=0.19.0",
    ],
    entry_points={
        'console_scripts': [
            'n8n-validate=n8n_utils.ci.validator:main',
            'n8n-visualize=n8n_utils.visualization.visualizer:main',
        ],
    },
    python_requires='>=3.8',
    author="Your Name",
    author_email="your.email@example.com",
    description="Utilities for n8n workflow validation and visualization",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/n8n-free-templates",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
