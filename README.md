# SECDマシン

### 実行方法

予め用意したスクリプトの実行

	python secd.py /path/to/script

対話モードの起動

	python secd.py

### 受けつける構文

ex 1)

	((lambda x (x (x y))) (1 2 3))

result 1)

	S: [[1, 2, 3], [[1, 2, 3], y]]
	E: []
	C: []
	D: D0


ex 2)

	((lambda x
	    (lambda y
	        (x y)))
	    ((lambda x
	        (lambda y
	            (x y)))
	        (lambda x
	            (lambda y
	                y))))

result 2)

	S: [<clos y, [x, y], [<x = <clos y, [x, y], [<x = <clos x, (lambda y: y), []>>]>>]>, [1, 2, 3], [[1, 2, 3], y]]
	E: []
	C: []
	D: D0

ラムダ式を記述する際は((lambda 束縛変数 本体) 実引数)のように記述し、
スペースかもしくは改行とタブで間を区切る。
なお、括弧を省略する記法は用いることができない。

### 対話モード

対話的に入力文字列を受け取って結果を返すことができる。
このモードでも複数行にわたっての入力が可能であり、
改行のみを入力した時点でそれまでのコードが実行される。