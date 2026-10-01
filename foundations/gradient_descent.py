class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        minimum = init
        def gradient(x):
            return 2*x
        while iterations > 0:
            minimum = minimum - learning_rate * gradient(minimum)
            iterations -= 1
        return round(minimum, 5)
