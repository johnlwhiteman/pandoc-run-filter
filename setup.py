import os
from setuptools import find_packages, setup

def read():
    return open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

setup(
    name='pandoc-run-filter',
    version='0.0.1',
    description='A simple filter for pandoc that runs commands and scripts capturing the output as images or text.',
    py_modules=['pandoc-run-filter'],
    url='https://github.com/johnlwhiteman/pandoc-run-filter',
    author='John L. Whiteman',
    author_email='me@johnlwhiteman.com',
    license="BSD-3-Clause",
    keywords=['pandoc', 'filter'],
    python_requires='>=3.6',
    packages=find_packages(),
    classifiers=[
        'Environment :: Console',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'License :: OSI Approved :: BSD 3-Clause "New" or "Revised" license',
        'Operating System :: OS Independent',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Developers',
        'Topic :: Text Processing :: Filters'
    ],
    long_description=read(),
    long_description_content_type='text/markdown',
    install_requires = [
        'pandocfilters >= 1.4',
        'Pillow >= 7.2',
        'PyYAML >= 5.3'
    ],
    extras_require = {
        'dev': [
            'pytest >= 3.7'
        ]
    },
    package_data={},
    entry_points={'console_scripts':['pandoc-run-filter = pandoc_run_filter:main']},
)

