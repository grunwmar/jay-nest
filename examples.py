import math
from jay_nest import Jay
""" ================================ Examples ================================ """

print("\n ------------ HYPOTENUSE ------------")
# Simple action of sojka:
a = 4
b = 3
c = math.sqrt((a**2 + b**2) |Jay()["Sojka uvnitř hlásí {value}[{typename}]"]) | Jay()["Sojka venku hlásí {value}[{typename}]"]


# Jay free
def polynomial_1(*coefs):
    exp_coefs = [(exp, coef) for exp, coef in enumerate(coefs)]
    return lambda x: sum([ ec_tuple[1] * x ** ec_tuple[0] for ec_tuple in exp_coefs])

# Jay occupied
def polynomial_2(*coefs):
    exp_coefs = [(exp, coef) for exp, coef in enumerate(coefs)] | Jay()["exp_coefs={value}"] # jay tells value of [...] result

    # Jay tells values of ec_tuple[1] - coefficient
    return lambda x: sum([(ec_tuple[1] | Jay()["coef={value}"]) * \

    # Jay tells values of ec_tuple[1] - expontent
    (x ** (ec_tuple[0] | Jay()["exp={value}"])) for ec_tuple in exp_coefs] | Jay() \

    # first jay tells computed values a*x**k, second jays tells the sum of these values
    ["List={value}"]) | Jay()["Lambda={value}"]

""" Lambdas in polynomial_1 and polynomial_2 are same, but in second case """
""" the lambda is expanded by filling with jays and commentaries. """


coefs = [-1,0,2]

print("\n ------------ POLYNOMIAL 1 ------------")
p1 = polynomial_1(*coefs)(20)
print("p1=", p1)

print("\n ------------ POLYNOMIAL 2 ------------")
p2 = polynomial_2(*coefs)(20)
print("p2=", p2)
