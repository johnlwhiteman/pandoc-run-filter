import os
from setuptools import find_packages, setup

def read():
    return open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

setup(
    name='pandoc-run-filter',
    version='0.2.0',
    description='A simple filter for pandoc that runs shell commands and scripts and outputs as text and images.',
    url='https://github.com/johnlwhiteman/pandoc-run-filter',
    download_url='https://github.com/johnlwhiteman/pandoc-run-filter/archive/v0.2.0.tar.gz',
    author='John L. Whiteman',
    author_email='me@johnlwhiteman.com',
    license="BSD-3-Clause",
    keywords=['pandoc', 'filter'],
    python_requires='>=3.6',
    package_dir={'': 'src'},
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Developers',
        'Topic :: Text Processing :: Filters',
        'Natural Language :: English'
    ],
    long_description=read(),
    long_description_content_type='text/markdown',
    install_requires = [
        'pandocfilters >= 1.4',
        'Pillow >= 7.2'
    ],
    extras_require = {
        'dev': [
            'pyfiglet >= 0.8',
            'pytest >= 5.1'
        ]
    },
    py_modules=['pandoc_run_filter'],
    entry_points={
        'console_scripts': [
            'pandoc-run-filter=pandoc_run_filter:main',
        ],
    },
    package_data={},
)
