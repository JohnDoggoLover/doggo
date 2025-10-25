#  doggo — The Doggo Programming Language

Doggo is a assembly-style language written in Python.  
She’s small, simple, and surprisingly clever — capable of math, branching, labels, and sleeping.

---

##  Features
- Basic arithmetic: `add`, `sub`, `mul`, `div`, `mod`
- Variables + input (`set`, `finp`, `sinp`)
- Comparison (`cmp`, `jg`, `jl`, `ljg`, `ljl`)
- Labels + control flow (`label`, `ljmp`)
- `sleep`, `exit`, `no` operations
- Built-in constant: `inf = ∞`

---

## ⚙️ Installation

### Option 1 — Run with Python
```bash
git clone https://github.com/JohnDoggoLover/doggo.git
cd doggo
python doggo.py example/hello.dog

```
### Option 2 - Run executaible
```bash
git clone https://github.com/JohnDoggoLover/doggo.git
cd doggo
./doggo.py example/hello.dog
```

## Adding to PATH (Recomended)
### (Non-permament method)
```bash
export PATH="$PATH:/home/[your name]/Desktop/doggo"
```
### (permament method)
```bash
echo 'export PATH="$PATH:/home/[your name]/Desktop/doggo"' >> ~/.bashrc
source ~/.bashrc
```
