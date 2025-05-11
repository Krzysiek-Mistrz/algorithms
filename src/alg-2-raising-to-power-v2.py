def power(a, n):
    if n == 0:
        return 1
    else:
        if not n % 2:
            x = power(a, n//2)
            return x * x
        else:
            return a * power(a, n - 1)
"""
power(3, 100) : 2∣100⇒x=2 \mid 100 -> x =2∣100⇒x= power(3, 50), return x∗xx*xx∗x
power(3, 50) : 2∣50⇒x=2 \mid 50 -> x =2∣50⇒x= power(3, 25), return x∗xx*xx∗x
power(3, 25) : 2∤25⇒2 \nmid 25 ->2∤25⇒ return 3∗3*3∗power(3, 24)
power(3, 24) : 2∣24⇒x=2 \mid 24 -> x =2∣24⇒x= power(3, 12), return x∗xx*xx∗x
power(3, 12) : 2∣12⇒x=2 \mid 12 -> x =2∣12⇒x= power(3, 6), return x∗xx*xx∗x
power(3, 12) : 2∣6⇒x=2 \mid 6 -> x =2∣6⇒x= power(3, 3), return x∗xx*xx∗x
power(3, 3) : 2∤3⇒2 \nmid 3 ->2∤3⇒ return 3∗3*3∗power(3, 2)
power(3, 2) : 2∣2⇒x=2 \mid 2 -> x =2∣2⇒x= power(3, 1), return x∗xx*xx∗x
power(3, 1) : 2∤1⇒2 \nmid 1 ->2∤1⇒ return 3∗3*3∗power(3, 0)
power(3, 0) ⇒->⇒ return 111
"""