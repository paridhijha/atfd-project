# CQ has form q{X} : e_1{X_1},..., e_n{X_n}
# head = q{X} is a type of Subgoal (having predicate and arguments)
# subgoals = e_1{X_1},..., e_n{X_n} is a set of Subgoals (having predicate and arguments)
class ConjQuery:
    def __init__(self, head, subgoals):
        self.head = head
        self.subgoals = subgoals
        self.i = 0
        self.toString = str(self.head.toString) + " : " + ", ".join(str(x.toString) for x in self.subgoals)
   
    def mapQuery(self):
        i = self.i +1;
        mapping={}
        nsubgoals=[]
        nhead = self.head.mapSubgoal(i, mapping)
        for sg in self.subgoals:
            nsubgoals.append(sg.mapSubgoal(i,mapping))
        return ConjQuery(nhead, nsubgoals)
  
