from fastapi import FastAPI, HTTPException
from typing import Optional

app = FastAPI()

def fibonacci_tail_helper(a, b, n):
    if n < 1:
        return a
    return fibonacci_tail_helper(b, a + b, n - 1)

def fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("Negative numbers are not allowed")
    if n > 1000:  # 1000を超える値の場合は計算を制限
        raise ValueError("Value too large")
    return fibonacci_tail_helper(0, 1, n)

@app.get("/fib")
def read_fib(n: Optional[int] = None):
    """
    Get the nth Fibonacci number.
    - **n**: An integer specifying the position in the Fibonacci sequence.
    """
    # nが指定されていない場合や整数でない場合の処理
    if n is None or not isinstance(n, int):
        raise HTTPException(status_code=400, detail="Input must be an integer")
    
    try:
        result = fibonacci(n)
        return {"result": result}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
