from sympy import * #library to work with logical expressions:  https://www.sympy.org/en/index.html 

#implement your logic, Knowledgebase, TT-Entails, FC-Entails, etc. here
#This code will be imported in main.py


#Example knowledgebase
KNOWLEDGEBASE = [
    "B11 <=> (P12 | P21)",
    "B11"
]

# You can use this class to implement your logic or you can implement your own classes or functions
class KnowledgebasedAgent:

    def TT_ENTAILS(self, knowledgebase, alpha):
        """Algorithm to determine if the current knowledgebase entails alpha"""
        #TODO: Implement this function
    
    def PL_FC_ENTAILS(self, knowledgebase, q):
        """Checks if the knowlegebase entails query q
           Beware, q can only be positive
        """
        #TODO: Implement this function
