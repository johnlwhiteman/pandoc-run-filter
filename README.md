# pandoc-run-filter

A simple filter for pandoc that runs commands and scripts capturing the output as images or text.

***Warning: Never run this filter against untrusted content since commands and/or scripts are executed!***

## Markdown Options

Run as a script:

```bash
in="script"
```

Run as a shell command:

```bash
in="shell"
```

Capture output as text:

```bash
out="text"
```

Capture output as an image:

```bash
out="image"
```

Use path to image as output:

```bash
out="image" fig="<path>"
```

## Build and Test Locally

```bash
$ pip uninstall pandoc-run-filter
$ python setup.py build
$ pip install -e .
```


```bash
$ pip install cleanup
$ pip install --editable .
$ python -m pytest ./tests/tests.py
```


