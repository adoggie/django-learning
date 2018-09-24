
<pre>
gaps =[]
def _collect(result, x, y):
  result.append([x[1],y[0]])
  return y

reduce(partial(_collect, gaps), entries)
</pre>
