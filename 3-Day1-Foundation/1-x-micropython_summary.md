### MicroPython/Python復習 (すでにPythonを習った方を前提)
- MicroPython特有の注意点を説明　(https://micropython-docs-ja.readthedocs.io/ja/latest/rp2/quickref.html)
  - マイコン専用のモジュール、Pinの取り扱い等 
  - MicroPythonかCircuitPythonか？
    - CurcuitPythonはMicroPythonから派生した言語で、Adafruit社が開発メンテナンス
    - 基本的なPythonの仕様は同じだが提供されるモジュールが異なる。同等のモジュールでもメソッド（関数）の仕様が異なる
    - MicroPythonを基本に使い、使いたいセンサのドライバがCircuitPython版しかない場合、CircuitPythonを選択するのが良いのでは
    - CircuitPython版ドライバをMicroPython版にポーティングするのも可能（自力で頑張る） 
