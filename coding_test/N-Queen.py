def solve_n_queens(n):
    def backtrack(row, columns, diagonals1, diagonals2, current_solution):
        # 모든 여왕이 배치되면 결과에 추가
        if row == n:
            result.append(list(current_solution))
            return
        
        for col in range(n):
            if col in columns or (row - col) in diagonals1 or (row + col) in diagonals2:
                continue
            columns.add(col)
            diagonals1.add(row - col)
            diagonals2.add(row + col)
            current_solution.append(col)
            backtrack(row + 1, columns, diagonals1, diagonals2, current_solution)
            # 백트랙
            columns.remove(col)
            diagonals1.remove(row - col)
            diagonals2.remove(row + col)
            current_solution.pop()
    
    result = []
    backtrack(0, set(), set(), set(), [])
    return result

def main():
    n = 8  # 예제: 8-Queens 문제
    solutions = solve_n_queens(n)
    print(f"Total solutions: {len(solutions)}")
    for solution in solutions:
        for row in solution:
            print('.' * row + 'Q' + '.' * (n - row - 1))
        print()

if __name__ == "__main__":
    main()
