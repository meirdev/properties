Parser for properties file, which is a simple key-value file, comments is also supported.

## Load from string

```python
import properties

string = """
FULL NAME: John Doe
AGE: 42
TIME: 12:00
"""

print(properties.loads(string))
```

```python
{
    "FULL NAME": "John Doe",
    "AGE": "42",
    "TIME": "12:00"
}
```

# Dump to string

```python
import properties

props = {
    "FULL NAME": "John Doe",
    "AGE": "42",
    "TIME": "12:00"
}

print(properties.dumps(props))
```

```text
FULL NAME: John Doe
AGE: 42
TIME: 12:00
```
