# TypeFX
Tired of your boring print statement? Use TypeFX to make your python statements more interesting

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

^^ Are useful if you want to list things

### Example
Basic
```
t("Hi how is your day?", 0.03)
```

Or bit more advanced

```
t("Breakfast^1. Eggs^2. Milk"^Toast%Whats your breakfast?, 0.07)
```

