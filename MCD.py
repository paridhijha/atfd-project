import copy
from sets import Set
class MCD:
    
    def __init__(self, Q, mappedQuerySubgoals, V, viewSubGoals, phi, hh):
        self.Q =Q
        self.V = V
        self.psi = {}
        self.hh =hh
        self.phi = phi
        self.mappedQuerySubgoals = mappedQuerySubgoals
        self.viewSubGoals = viewSubGoals
        
    def printMcd(self):

        string =  " V(Y)c = { "+ self.V.toString +"}"
        gc=""
        for sg in self.mappedQuerySubgoals:
            gc=gc+sg.toString
        string = string + " gc = { "+ gc + " }"

        vsg=""
        for sg in self.viewSubGoals:
            vsg=vsg+sg.toString
        string = string + " vsg = { "+ vsg + " }"

        phi=""
        for k,v in self.phi.iteritems():
            phi = phi + k + "->" + v + "  "

        string = string + " phi = { "+ phi + " }"

        
        print "MCD =", string
 
