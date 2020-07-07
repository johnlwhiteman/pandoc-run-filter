# pandoc-run-filter

A simple filter for pandoc that runs commands and scripts capturing the output as images or text.

<span style="color:red"><b>Warning: Never run this filter against untrusted content since commands and/or scripts are executed!</b></span>

## Markdown Options

Run as a script:
```in=script```

Run as a shell command:
```in=shell```

Capture output as text:
```out=text```

Capture output as an image:
```out=image```


## Markdown Examples

**Run ls * as shell command and capture its output as text:**


``````
```{.run cmd="ls" in="shell" out="text"}
*
```
``````

**Run ls * as shell command and capture its output as an image:**

``````
```{.run cmd="ls" in="shell" out="image"}
*
```
``````

**Run this as a python script and capture its output as text:**
``````
```{.run cmd="python" in="script" out="text"}
print("Can I see this as an image .... this is all good!")
```
``````

**Run this as a python script and capture its output as an image:**
``````
```{.run cmd="python" in="script" out="image"}
print("Can I see this as an image .... this is all good!")
```
``````


**Run this python script and reference the venn.png as output**
``````
```{.run cmd="python" in="script" out="image" img="venn.png"}
from matplotlib_venn import venn2, venn2_circles, venn2_unweighted
from matplotlib_venn import venn3, venn3_circles
from matplotlib import pyplot as plt
venn2(subsets = (30, 10, 5), set_labels = ('Group A', 'Group B'))
plt.savefig("venn.png")
```
``````

