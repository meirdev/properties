Simple library for parsing properties files.

## Example

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
