# TypeFX
Tired of your boring print statement? Use TypeFX to make your python statements more interesting in python.

### Basic Syntax
t(txt, time)

'txt' is the text you want to write

'time' controls how slow it writes

->The higher the time the slower the text writes out

->Has a default value if you do not pass an argument for it

### Import
```
from type import t
```

### Extended Usage
Writing a '^' in txt will make your text move to the next line
Writing a '%' in txt will make your text skip a iine (basically \n)

### Example
Basic
```
t("Hi how is your day?", 0.03)
```

Or

```
t("Breakfast%1. Eggs^2. Milk")
```

