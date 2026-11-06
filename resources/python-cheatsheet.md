# Python Cheat Sheet for This Course

Everything here appears in the labs. Keep this page open while you work.

## Basics (Lab 01)
```python
w = 12.0                      # variable (kN/m); text after # is a comment
L = 6.0
M = w * L**2 / 8              # arithmetic: + - * / and ** (power)
print(f"M = {M:.1f} kN·m")    # f-string: {value:.1f} = 1 decimal place

spans = [4.0, 5.0, 6.0]       # list
spans[0]                      # first item (Python counts from 0); spans[-1] is the last
len(spans)                    # number of items
spans.append(7.0)             # add an item

for s in spans:               # loop: indent the body by 4 spaces
    print(s)

if M <= 75:                   # decision
    print("OK")
else:
    print("NOT OK")

mix = {"cement": 380, "water": 171}   # dictionary: key -> value
mix["water"] / mix["cement"]           # look up values by key

def max_moment(w, L):         # function
    """Max moment of a simply supported beam with uniform load."""
    return w * L**2 / 8
```

## NumPy — fast math on arrays
```python
import numpy as np
x = np.array([1.0, 2.0, 3.0])
x * 2, x.mean(), x.std(), x.min(), x.max(), x.sum()
np.linspace(0, 10, 50)        # 50 evenly spaced numbers from 0 to 10
np.sqrt(x), np.exp(x), np.log(x)
W @ x                         # matrix times vector (neural networks, Week 5)
```

## pandas — tables of data (Lab 02)
```python
import pandas as pd
df = pd.read_csv(get_data("concrete_strength.csv"))   # get_data() is in every setup cell
df.head()                 # first 5 rows
df.shape                  # (rows, columns)
df.describe()             # summary statistics
df.columns                # column names
df["strength_mpa"]        # one column (a Series)
df[["cement_kg_m3", "water_kg_m3"]]          # several columns
df[df["age_days"] == 28]                      # filter rows
df.sort_values("strength_mpa", ascending=False)
df.groupby("age_days")["strength_mpa"].mean() # average by group
df["wc_ratio"] = df["water_kg_m3"] / df["cement_kg_m3"]   # new column
df.isna().sum()           # missing values per column
```

## matplotlib — plots
```python
import matplotlib.pyplot as plt
plt.figure(figsize=(6, 4))
plt.scatter(df["wc_ratio"], df["strength_mpa"], s=10, alpha=0.5)
plt.xlabel("Water–cement ratio (–)")
plt.ylabel("Compressive strength (MPa)")
plt.title("Strength falls as w/c rises")
plt.show()
# also: plt.plot(x, y), plt.hist(values, bins=30), plt.legend(), plt.grid(True)
```

## scikit-learn — machine learning (Labs 04–06, 11–13)
```python
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score, accuracy_score, confusion_matrix

X = df.drop(columns="strength_mpa")      # inputs (features)
y = df["strength_mpa"]                   # target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler().fit(X_train)   # learn scaling from TRAINING data only
model = LinearRegression().fit(scaler.transform(X_train), y_train)
pred = model.predict(scaler.transform(X_test))
mean_absolute_error(y_test, pred), r2_score(y_test, pred)
```

## Language models with transformers (Labs 01, 08, 10, 12)
```python
from transformers import pipeline
chat = pipeline("text-generation", model="Qwen/Qwen2.5-0.5B-Instruct")
messages = [{"role": "user", "content": "What is a water-cement ratio?"}]
chat(messages, max_new_tokens=150, do_sample=False)[0]["generated_text"][-1]["content"]
```

## Reading error messages
Read the **last line** first. Common ones:
| Error | Usually means |
|---|---|
| `NameError: name 'x' is not defined` | Typo, or you didn't run the cell that creates `x` |
| `KeyError: 'col'` | That column/key doesn't exist — check `df.columns` or spelling |
| `TypeError: unsupported operand` | Mixing types, e.g., a number and `None` (did you finish a `# TODO`?) |
| `IndentationError` | The lines inside a loop/function/if must be indented by 4 spaces |
| `ValueError: shapes ... not aligned` | Arrays have mismatched sizes — print `.shape` of each |
