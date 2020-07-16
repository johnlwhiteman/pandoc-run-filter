# pandoc-run-filter (v 0.1.0)

A simple pandoc filter that runs an embedded command or script in a markdown document capturing its output as an image or text.

This tool has two basic use cases:

1. Execute a program or command as specified in the markdown
2. Execute a script that you embed in the markdown itself

The tool then captures the output and passes it to *pandoc* as either:

1. Text
2. Image

So what could go wrong?

```
 /\  /\ !!!!!!!!! /\  /\
|! ||! |!!!!!!!!!|! ||! |
|! ||! |         |! ||! |
|! ||! | Warning |! ||! |
|! ||! |         |! ||! |
|__||__|!!!!!!!!!|__||__|
(__)(__)!!!!!!!!!(__)(__)
```

***Warning: Only run this tool on markdown content that you trust. Don't blindly run it on unverified content since inputs are executed while running pandoc.***

```
 /\  /\ !!!!!!!!! /\  /\
|! ||! |!!!!!!!!!|! ||! |
|! ||! |         |! ||! |
|! ||! | Warning |! ||! |
|! ||! |         |! ||! |
|__||__|!!!!!!!!!|__||__|
(__)(__)!!!!!!!!!(__)(__)
```

## Install

```bash
$ pip install pandoc-run-filter
```

## Test

```bash
$ pip install pytest pyfiglet
$ pytest ./tests/tests.py
```

## Run

```bash
$ pandoc --filter pandoc-run-filter myfile.md -o myfile.epub
```

## Uninstall

```bash
$ pip uninstall pandoc-run-filter -y
```

## Markdown Options

pandoc-run-filter looks for the following syntax in a markdown file where *.run* is the keyword.

``````
```{.run cmd="?" in="?" out="?" img="?"}
?
```
``````

Some examples of *cmd* might include:

* echo
* python
* dir
* ls
* myprogram
* /home/user/myprogram
* ../../myprogram
* ...

Next, the *in* parameter tells us how *cmd* should be executed. We have two options here:

Run as a shell command:

```bash
in="shell"
```

Run as an embedded script:

```bash
in="script"
```

Next, the *out* parameter tells us how the output should be handled. We have a few options here too:

Capture as text:

```bash
out="text"
```

Capture as an image:

```bash
out="image"
```

If *out* is an image and what gets executed generates an image file, then we can use the optional *img* parameter to point to the path of that file. If this option is not provided, then this tool does its best to convert the output to an image.

```bash
out="image" img="<path>"
```

That's about it. Now, it's time for some examples. There were taken from the use cases under the *./tests* directory.


## Examples

### [./tests/01.md](./tests/01.md)

*Run the echo command in a shell and capture the output as text*

Markdown:

``````
```{.run cmd="echo" in="shell" out="text"}
'This is output as text.'
```
``````

Pandoc:

```bash
pandoc -i 01.md --filter pandoc-run-filter -o 01.epub
```

Output:

```bash
'This is output as text.'
```

[01.epub](./epubs/01.epub)


### [./tests/02.md](./tests/02.md)

*Run the echo command in a shell and convert the output to an image*

Markdown:

``````
```{.run cmd="echo" in="shell" out="image"}
'This is the output but converted to an image.'
```
``````

Pandoc:

```bash
pandoc -i 02.md --filter pandoc-run-filter -o 02.epub
```

Output:

![](./images/02.png)

[02.epub](./epubs/02.epub)


### [./tests/03.md](./tests/03.md)

*Run an embedded python script and capture the output as text*

Markdown:

``````
```{.run cmd="python" in="script" out="text"}
import pyfiglet
r = pyfiglet.figlet_format('Hi There!', font = 'banner')
print(f'''The is an embedded python script that generates ascii art.\n''')
print(r)
```
``````

Pandoc:

```bash
pandoc -i 03.md --filter pandoc-run-filter -o 03.epub
```

Output:

```bash
The is an embedded python script that generates ascii art.

#     #      #######                             ###
#     # #       #    #    # ###### #####  ###### ###
#     # #       #    #    # #      #    # #      ###
####### #       #    ###### #####  #    # #####   #
#     # #       #    #    # #      #####  #
#     # #       #    #    # #      #   #  #      ###
#     # #       #    #    # ###### #    # ###### ###

```

[03.epub](./epubs/03.epub)

### [./tests/04.md](./tests/04.md)

*Run embedded python script and capture the output as a path to an image it created*

Markdown:

``````
```{.run cmd="python" in="script" out="image" img="04.png"}
from PIL import Image, ImageDraw, ImageFont
T = 'Hi There!'
W = 400
H = 400
shape = [(50, 50), (W - 10, H - 10)]
fnt = ImageFont.truetype('arial.ttf', 18)
image = Image.new(mode = 'RGB', size = (W, H), color='white')
draw = ImageDraw.Draw(image)
w, h = draw.textsize(T, fnt)
draw.rectangle(shape, fill ='#AAAAAA', outline ='#000000')
draw.text(((W-w)/2,(H-h)/2), T, font=fnt, fill='black')
image.save('04.png')
```
``````

Pandoc:

```bash
pandoc -i 04.md --filter pandoc-run-filter -o 04.epub
```

Output:

![](./images/04.png)


[04.epub](./epubs/04.epub)
