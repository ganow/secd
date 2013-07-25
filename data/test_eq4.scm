((lambda x x) a)

((lambda x
    (lambda y
        (x y)))
    ((lambda x
        (lambda y
            (x y)))
        (lambda x
            (lambda y
                y))))

(1 2 3 (4 5))