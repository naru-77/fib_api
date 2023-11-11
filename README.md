# フィボナッチ数 API ドキュメント

## 概要

この API は、指定された順番にあるフィボナッチ数を返します。フィボナッチ数列は、最初の二項が 1 で、その後の各項は前の二項の和になっています（例：1, 1, 2, 3, 5, 8, ...）。

## エンドポイント

GET /fib

### パラメータ

- n（整数）: フィボナッチ数列のどの項を取得するかを指定します。例えば、n=5 の場合、数列の第 5 項を返します。

### 応答

- 成功時：フィボナッチ数列の指定された項の値を含む JSON オブジェクトを返します。例：{"result": 5}。

- エラー時：エラーメッセージを含む JSON オブジェクトと HTTP ステータスコード 400 を返します。例：{"detail": "Negative numbers are not allowed"}。

### 制限事項

この API は、n が 0 以上 1000 以下の整数であることを要求します。
n がこの範囲外の場合、エラーメッセージが返されます。

### 使用例

1. 正常なリクエスト：

```sql
curl -X GET "https://fib-api-4cgh.onrender.com/fib?n=10"
```

応答：{"result": 55}

1. エラーの場合（負の数）：

```sql
curl -X GET "https://fib-api-4cgh.onrender.com/fib?n=-1"
```

応答：{"detail": "Negative numbers are not allowed"}
