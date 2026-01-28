
# ============================================================
# Prompt builder
# ============================================================

def build_user_prompt(code: str) -> str:
    return USER_PROMPT_TMPL.format(code=code.rstrip())


SYSTEM_PROMPT = """You are given a Python code snippet that already contains an assertion with a placeholder token ??. Execute the code under Python 3.10 semantics and replace ?? with the exact runtime value of the asserted expression. The replacement must be a Python literal (no expressions, no function calls). Do NOT output any extra information. Execute the program step by step before arriving at an answer, and provide the full assertion with the correct output in [ANSWER] and [/ANSWER] tags, following the examples.

[PYTHON]
def f(n):
    return n
x = f(17)
print(f"Result: {x}")
assert(x == ??)
[/PYTHON]
[THOUGHT]
The function f(n) returns the input n directly.
The code calls f(17), so the return value is 17.
The variable x is assigned the result of f(17), so x equals 17.
The assertion checks the value of x.
[/THOUGHT]
[ANSWER]
assert(x == 17)
[/ANSWER]

[PYTHON]
def f(s):
    return s + "a"
y = f("x9j")
print(f"Target result: {y}")
assert(y == ??)
[/PYTHON]
[THOUGHT]
The function f(s) concatenates the string "a" to the input s.
The input is "x9j".
Executing f("x9j") results in "x9j" + "a", which is "x9ja".
The variable y is assigned "x9ja".
The assertion checks the value of y.
[/THOUGHT]
[ANSWER]
assert(y == "x9ja")
[/ANSWER]
"""

USER_PROMPT_TMPL = """
[PYTHON]
{code}
[/PYTHON]
[THOUGHT]
"""