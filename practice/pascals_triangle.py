def generate_pascals_triangle(n):
    triangle = []
    
    for i in range(n):
        if i == 0:
            row = [1]
        else:
            row = [1]  # Start each row with 1
            for j in range(1, len(triangle[-1])):
                row.append(triangle[-1][j-1] + triangle[-1][j])
            row.append(1)  # End each row with 1
        
        triangle.append(row)
    
    return triangle

# Number of rows
num_rows = 9
pascals_triangle = generate_pascals_triangle(num_rows)

# Print Pascal's Triangle
for row in pascals_triangle:
    print(' '.join(map(str, row)).center(num_rows * 4))
