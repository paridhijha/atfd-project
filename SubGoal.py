# A subgoal is of form q{x1,x2,x3} where q is predicate name and x1,x2 are arguments (either variables or constants)
class SubGoal:
    args = []

    def __init__(self, name, args):
        self.name = name
        self.args = args
        self.toString = self.name + "(" + (", ".join(self.args)) + ")"
                      
    def mapSubgoal(self, i, mapping):
        args = []
        for a in self.args:
            n=a
            if a in mapping.keys():
                n=mapping[a]
            args.append(n)
        return SubGoal(self.name, args)


    
