---
redirect_from:
  - "/"
interact_link: content/tutorials/00-Introduction.ipynb
title: 'Tutorials'
prev_page:
  url: /
  title: ''
next_page:
  url: /tutorials/00-Introduction
  title: '00-Introduction'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---

## Introduction

Welcome to the Voytek Lab GitHub and Jupyter notebook collection.
This is the first Jupyter notebook in a tutorial series which broadly discusses the main topics involved with the projects  being done in Voytek lab. We will walk through many of the concepts and calculations that are used in Voytek lab.

Knowledge in python is ***greatly*** recommended to help understand these tutorials and to help you preform these procedures, although it is not super necessary. Here are a couple of links which broadly go over Python. <br>

[Python: COGS 108](https://github.com/COGS108/Tutorials/blob/master/w02-02a-Python.ipynb)<br>
[Python: CodeAcademy](https://github.com/COGS108/Tutorials/blob/master/w02-02a-Python.ipynb)<br>

The purpose of this notebook is to:

- Introduce you to Jupyter Notebook
- Learn how to run cells
- Install relevant modules
- Load your data into a Jupyter Notebook

This notebook will be a brief introduction and I encourage you to explore these tools further. 

<img src="./img/jupyter_logo.png" />

### What is Jupyter notebook & Set up

<div class="alert alert-success">
Jupyter notebook is a way to develop program processes that we can easily run our data through. It lets us write, run, and present code easily.
</div>

Jupyter notebook is a tool from  Anaconda - a python distribution which a manages different python environments for scientific computing. Jupyter is an example of an environment from Anaconda. There are 2 ways to consume these tutorials. If you think you will be using Jupyter in he future, I recommend following the first option. Otherwise if you just want to take a look at these tutorials and never return to Jupyter - use the second link which will lead you to a cloud-based environment which allows you to run these tutorial notebooks.

#### Follow along using Git

<img src="./img/github_logo.png" height="150" width="150">

- Download anaconda from [here](https://store.continuum.io/cshop/anaconda/)

- Clone this [repository](https://github.com/voytekresearch/tutorials) by using git clone 

- Run the 'Anaconda Navigator' GUI from first bullet point and launch this Jupyter notebook.

- Navigate to where you cloned the GitHub repository and click on the .ipynb file you want to run.

#### Follow along using Binder

<img src="./img/binder_logo.png" height="100" width="100">

or alternatively, if you don't want to install anything open this [Binder link](https://mybinder.org/v2/gh/voytekresearch/tutorials/master). You can consume 100% of these tutorials this way too.

<div class="alert alert-info">
If you are unfamiliar with Jupyter Notebook, follow this link for an introduction <a href="https://github.com/COGS108/Tutorials/blob/master/01-JupyterNotebooks.ipynb" class="alert-link">COGS 108: Jupyter Notebook</a> Here is a link for a more indepth Jupyter <a href="https://www.dataquest.io/blog/jupyter-notebook-tutorial/" class="alert-link"> tutorial.</a>
</div>



Also here are a list of [shortcuts](http://maxmelnick.com/2016/04/19/python-beginner-tips-and-tricks.html) - you may find yourself doing a few commands frequently and its nice to use a quick shortcut to save time.

## Modules

<div class="alert alert-success">
In this section we will discuss the python modules used most often in Voytek lab and how to install them.
</div>

<div class="alert alert-info">
Follow this <a href="https://github.com/COGS108/Tutorials/blob/master/04-DataSciencePython.ipynb" class="alert-link">link</a> to learn about the common Voytek lab modules.
</div>

#### Installing modules using Anaconda
If you are using anaconda, you will be able to install many modules by opening 'Anaconda Prompt' and running the command "pip install *module name*" For example:<br><br>
$pip install pandas
<br><br> pip is a nifty module managing tool. On the other hand if you are using Binder to follow along then everything should be set up already.



{:.input_area}
```python
# here are some common modules used in Voytek lab:
import numpy as np #library of math functions
import pandas as pd #library of data analysis functions
import matplotlib.pyplot as plt #functions to plot data
import sklearn as skl # tools for data mining and machine learning
```


### Importing Data

Now let's bring in some data. To do that, we need to tell python where to get the data from and save it as a variable. 
'emodat.npy' is data from one channel of an ECoG recording from a subject looking at faces displaying various emotions. 

We'll use this data in several of the tutorials. It should be saved at './dat/emodat.npy'



{:.input_area}
```python
# The name of the data file to load
filename = "./dat/emodat.npy"

# Loading data
data = np.load(filename)
```


Let's use our plotting library to plot some of the data.



{:.input_area}
```python
plt.plot(data[0:1000]) #this is what about 1 second of ECoG data looks like
```





{:.output_data_text}
```
[<matplotlib.lines.Line2D at 0x2dfa1ce2f98>]
```




![png](../images/build/tutorials/00-Introduction_20_1.png)


Alright, that's all we're going to talk about here.

Good luck with Jupyter notebook and the rest of the tutorials!
