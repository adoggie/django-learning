
<pre>
gaps =[]
def _collect(result, x, y):
  result.append([x[1],y[0]])
  return y

reduce(partial(_collect, gaps), entries)
</pre>

def big_small(big,small,compare,x):
  if x >=compare:
     big.append(x)
  else:
     small.append(x)

big=[]
small=[]
filter(partial(big_small,5),range(10))
