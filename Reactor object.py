#This is a program that can be used to create a reactor as an object. The object will take in the parameters like
#reactor volume, volumetric flow rate, molar flow rate, and return the conversion obtained. We'll also need a Reaction 
#object - that defines the reaction that is taking place as well as it's stoichiometry.

#Let's create the reaction class. It should contain the following information:
    #Stoichiometric cofficients, rate constant, order of reaction, reversibility, temperature at which rate constant is given, 
    #activation energy, equilibrium constant.
    
class Reaction:
    def __init__(self, reaction_coefficients, rate_constant):
        self.coefficients = list(reaction_coefficients)
        self.k = rate_constant
        self.reactant_coefficients = []
        for coefficient in self.coefficients:
            if coefficient < 0:
                self.reactant_coefficients.append(coefficient)
        
        #The reaction rate will be -ra = k*C[i]^(reaction_coefficients[i])
    def get_reaction_rate(self, reactant_concentrations):
        if len(reactant_concentrations) < len(self.reactant_coefficients):
            return "You need to enter the concentrations of all the reactants"
        C = list(reactant_concentrations)
        concentration_dependent_term = 1.0
        for i in range(len(C)):
            concentration_dependent_term = concentration_dependent_term * C[i] ** -self.reactant_coefficients[i]
            
        return self.k * concentration_dependent_term

class Reactor:
    def __init__(self, reaction, reactor_volume, feed_rate_of_reactants, volumetric_flow_rate):
        self.reaction = reaction    #This is a Reaction object
        self.v0 = volumetric_flow_rate
        self.F = list(feed_rate_of_reactants)
        self.V = reactor_volume
    
    def get_conversion(self):
        # We need to create and solve the odes according to the reaction
        pass
        


