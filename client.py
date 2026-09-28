"""Plonk Permutation Grand Product Engine.
100% Python Standard Library.
"""

class PlonkPermutationArgument:
    """Plonk grand product copy constraint permutation argument."""
    PRIME = 2147483647

    def compute_grand_product(self, wire_values, sigma_perm, beta=3, gamma=5):
        z = 1
        for i, val in enumerate(wire_values):
            num = (val + beta * i + gamma) % self.PRIME
            den = (val + beta * sigma_perm[i] + gamma) % self.PRIME
            den_inv = pow(den, self.PRIME - 2, self.PRIME)
            z = (z * num * den_inv) % self.PRIME
        return z
