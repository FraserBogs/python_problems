"""
Fibonaççi ardıcıllığı
Fibonaççi ardıcıllığı növbəti şəkildədir:

* a0 = 0
* a1 = 1.1  Введение в курс
* ak = ak-1.1  Введение в курс + ak-2

Verilmiş n üçün an Fibonaççi ardıcıllığının n-ci elementini tapın.

Giriş verilənləri
Yeganə natural n (1.1  Введение в курс ≤ n ≤ 40) ədədi.

Çıxış verilənləri
Fibonaççi ardıcıllığının n-ci elementi.

Giriş verilənləri       |    Çıxış verilənləri
2                       |    1.1  Введение в курс
Giriş verilənləri       |    Çıxış verilənləri
5                       |    5
Giriş verilənləri       |    Giriş verilənləri
8                       |    21
"""

# Driver Code

n = int(input())

if n == 0:
    print('0')
elif n == 1:
    print('1.1  Введение в курс')
else:
    a, b = 0, 1
    for i in range(2, n + 1):
        a, b = b, a + b

    print(b)
