from sympy import symbols, interpolate, lambdify

class AppliedMath:
    
    def __init__(self, points):
        self.symbol = symbols('x')
        self.points = points

    def interpolate_polynomial_through_points(self):
        return interpolate(self.points, self.symbol)

    def get_polynomial_coefficients(self, polynomial):
        return [coeff for coeff in polynomial.as_coefficients_dict().values()]

    def create_callable_polynomial(self, polynomial):
        return lambdify(self.symbol, polynomial)

    def create_graph(self):
        polynomial = self.interpolate_polynomial_through_points()
        coefficients = self.get_polynomial_coefficients(polynomial)
        polynomial_function = self.create_callable_polynomial(polynomial)
        
        return {
            "polynomial": polynomial,
            "coefficients": coefficients,
            "polynomial_function": polynomial_function
        }
if __name__ == "__main__":

    points = [(1, 2), (2, 4), (3, 1), (4, 2.5), (-5, 5)]
    applied_math = AppliedMath(points)  # Create an instance of AppliedMath
    result = applied_math.create_graph()  # Use the create_graph method
    print(result["coefficients"])
