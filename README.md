# plyg (plug)
Pronounced plug is Clean Structures to litter your code base. 

## QuickStart

Let's get dirty! Install **plyg** with

```python
pip install plyg
```

If we are getting dirty mine as well bring the bus along... 
This bad boy will handle any `event` or `command` we throw at it. 

```
plyg bus
```

Let's checkout what we got. By default it will generate a new file named `messagebus.py` where the command was ran. 
We can get extra freaky and tell it where to put it even give the file a pet name or specify an existing file to add the code to the end. 


**messagebus.py**
```python

```

We are always testy in these parts so we drop some attitude any where we go. 

**test_messagebus.py**
```python

```


```
plyg user-model rough
```

Searches for a `models.py` file to add the following code


```python
class User:
    def __init__(self, id, first, last, email, username):

```


Are the names to clean or dirty for you set them how you'd like creating a config file. 
```
plyg config
```
