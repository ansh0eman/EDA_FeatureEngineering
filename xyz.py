def min_operations_to_reach(a, b):
    memo = {}

    def min_operations(x, y, m):
        if (x, y, m) in memo:
            return memo[(x, y, m)]
        
        if x > a or y > b:
            return float('inf')

        if x == a and y == b:
            return 0

        # Move horizontally
        move_horizontal = 1 + min_operations(x + m, y, m)

        # Move vertically
        move_vertical = 1 + min_operations(x, y + m, m)

        # Increase propulsion strength
        boost_strength = 1 + min_operations(x, y, m + 1)

        memo[(x, y, m)] = min(move_horizontal, move_vertical, boost_strength)
        return memo[(x, y, m)]
    
    return min_operations(0, 0, 1)

def main():
    t = int(input().strip())
    results = []
    for _ in range(t):
        a, b = map(int, input().strip().split())
        results.append(min_operations_to_reach(a, b))
    
    for result in results:
        print(result)

# Example usage:
if __name__ == "__main__":
    main()