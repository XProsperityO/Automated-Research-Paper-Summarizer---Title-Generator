from setuptools import setup, find_packages

setup(
    name='research-paper-assistant',
    version='0.1.0',
    author='Your Name',
    author_email='your.email@example.com',
    description='Automated Research Paper Summarizer and Title Generator',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'numpy',
        'pandas',
        'scikit-learn',
        'nltk',
        'transformers',
        'torch',
        'tensorflow',
        'beautifulsoup4',
        'requests'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)