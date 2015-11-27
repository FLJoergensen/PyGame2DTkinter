import Queue as Q

class Job(object):
    def __init__(self, priority, description):
        self.priority = priority
        self.description = description
        print 'New job:', description
        return
    def __cmp__(self, other):
        return cmp(self.priority, other.priority)

q=Q.PriorityQueue()

q.put( Job(3,"1"))
q.put( Job(10,"2"))
q.put( Job(1,"3"))
q.put( Job(3,"4"))
q.put( Job(-1,"5"))

while True:
    try:
        j=q.get_nowait()
        print (j.priority,j.description)
    except:
        break
    
