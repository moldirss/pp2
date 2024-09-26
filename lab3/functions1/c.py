def solve(numheads, numlegs):
    for chickens in range(numheads + 1):
        rabbits = numheads - chickens
        if 2 * chickens + 4 * rabbits == numlegs:
            return chickens, rabbits
    return None, None

# Example usage:
chickens, rabbits = solve(35, 94)
print(f"We have {chickens} chickens and {rabbits} rabbits.")
