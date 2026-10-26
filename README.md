# goit-pycore-hw-05

Homework for topic 8 of the course "Python Programming: Foundations and Best Practices 2.0": functional programming and built-in modules.

| File | Task |
|---|---|
| `task_1.py` | `caching_fibonacci()` — Fibonacci numbers with a cache in a closure |
| `task_2.py` | `generator_numbers(text)` and `sum_profit(text, func)` — income numbers from a text |
| `task_3/main.py` | log file analyser (optional task); sample log: `task_3/logfile.log` |
| `task_4.py` | assistant bot from homework 4 with the `input_error` decorator |

No third-party packages are needed.

## Run

```bash
python task_1.py
python task_2.py
python task_3/main.py task_3/logfile.log
python task_3/main.py task_3/logfile.log error
python task_4.py
```

Bot commands (case-insensitive): `hello`, `add <name> <phone>`, `change <name> <phone>`, `phone <name>`, `all`, `close` / `exit`; Ctrl+C or Ctrl+D also exits.
