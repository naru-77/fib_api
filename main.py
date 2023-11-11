from fastapi import FastAPI, HTTPException
from typing import Optional

app = FastAPI()

def fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("Negative numbers are not allowed")
    if n > 1000:  # 1000を超える値の場合は計算を制限
        raise ValueError("Value too large")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

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

# ユニットテストの例
def test_fibonacci():
    assert fibonacci(10) == 55
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    try:
        fibonacci(-1)
    except ValueError:
        assert True
    else:
        assert False
    try:
        fibonacci(1001)
    except ValueError:
        assert True
    else:
        assert False
