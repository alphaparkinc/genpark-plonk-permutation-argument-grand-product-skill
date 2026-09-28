from client import PlonkPermutationArgument

plonk = PlonkPermutationArgument()
wires = [100, 200, 100]
perm = [2, 1, 0]

z = plonk.compute_grand_product(wires, perm)
print(f"Plonk grand product accumulator: {z} (Valid copy constraint: {z == 1})")
