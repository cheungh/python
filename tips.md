### library path
<pre>
import sys  
for each in sys.path:  
     print each
</pre>

### list current dir contents
<pre>
for each in os.listdir("."):
     print each
</pre>

### list comprehension
<pre>
[i for i in range(10)]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

[i for i in range(10) if i > 5]
[6, 7, 8, 9]


rows = [1, 2, 3, 4]
cols = [6, 7, 8, 9]
print [each*2 for each in [c*r for c in cols for r in rows]]
[12, 24, 36, 48, 14, 28, 42, 56, 16, 32, 48, 64, 18, 36, 54, 72]


</pre>
