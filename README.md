

```json
{
    "name": "AFD1",
    "description": "Automa che riconosce le stringhe (0 1* 0)",
    "alphabet": ["0", "1"],
    "states": ["A", "B", "C"],
    "start_state": "A",
    "final_states": ["C"],
    "transitions": {
        "A": {
            "0": "B"
        },
        "B": {
            "0": "C",
            "1": "B"
        }
    }
}
```
![1](out/AFD1.png)
![2](out/AFDtom.png)
