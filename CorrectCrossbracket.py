import wnBracketData
import cPickle

fn = '2004 class M.wnd'

# load the tournament
f = file(fn, 'rb')
t = cPickle.load(f)
f.close()

for w in t.weight_classes.values():
  r = w.GetRound('Quarter-Finals Champion')
  # do the swaps in the quarters
  l = []
  for i in range(r.NumEntries-1,-1,-1):
    l.append(r.Entries[i].NextLose)
    
  # set the new order
  for i in range(0, r.NumEntries):
    r.Entries[i].NextLose = l[i]
    
  r = w.GetRound('Semi-Finals Champion')
  # get rid of the swaps in the semis
  l = []
  for i in range(r.NumEntries-1,-1,-1):
    l.append(r.Entries[i].NextLose)
    
  # set the new order
  for i in range(0, r.NumEntries):
    r.Entries[i].NextLose = l[i]
    
# write the tournament to disk
f = file(fn, 'wb')
cPickle.dump(t,f,True)
f.close()

print 'Done'