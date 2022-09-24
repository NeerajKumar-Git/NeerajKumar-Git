import queue
def max_width(root):
  q = queue.Queue()
  q.put([root,1])
  max_width=1
  while q.empty() is False:
      size = q.qsize()
      for i in range(size):
          curr,ind = q.get()
          if i == 0:
              first = ind
          if i == size-1:
              last  = ind
          if curr.left is not None:
              q.put([curr.left,2*ind])
          if curr.right is not None:
              q.put([curr.right,2*ind+1])
      max_width = max(max_width,last-first+1)
  return max_width
