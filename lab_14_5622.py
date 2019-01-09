from collections import deque
WALL_CELL = "#"  # Не прохідна клітина


def mazeMatrix(n):
    maze = [['#' for i in range(n+2)]]
    for i in range(n):
        row = ['#']
        tmp = list(input(''))
        row.extend(tmp)
        row.append('#')
        maze.append(row)
    maze.append(['#'for i in range(n+2)])
    return maze

def wave(maze, start, wall_cell):
    """ функція побудови хвильової матриці для лібіринту
        P4_Maizes зі стартовою точкою start
        wall_cell - символ, що позначає стіну лабіринта або непрохідну його клітину"""

    # P4_Maizes - матриця лабіринту
    # start - початкова позиція у лабіринті у вигляді кортежу (рядкок, стовпчик)

    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    # dx = [-1, -1, 0, 1, 1, 1, 0, -1]
    # dy = [0, -1, -1, -1, 0, 1, 1, 1]

    n = len(maze)     # кількість рядків у матриці P4_Maizes
    m = len(maze[0])  # кількість стовпчиків у матриці P4_Maizes

    # створення та ініціалізація хвильової матриці
    # такої ж розмірності, що і матриця лабіринту
    waveMatrix = []
    for i in range(n):
        row = [-1] * m
        waveMatrix.append(row)

    # створення та ініціалізація sources-матриці
    # такої ж розмірності, що і матриця лабіринту
    sources = []
    for i in range(n):
        row = [None] * m
        sources.append(row)

    q = deque()        # Створюємо чергу
    q.append(start)  # Додаємо у чергу координати стартової клітини
    waveMatrix[start[0]][start[1]] = 0  # Відстань від стартової клітини до себе нуль
    while not len(q) == 0:

        current = q.popleft()  # Беремо перший елемент з черги
        i = current[0]  # координата поточного рядка матриці
        j = current[1]  # координата поточного стовчика матриці
        sources[i][j] = 4
        # Додаємо в чергу всі сусідні клітини
        for k in range (len(dx)):

            i1 = i+dy[k]  # координата рядка сусідньої клітини
            j1 = j+dx[k]  # координата стовпчика сусідньої клітини

            # які ще не були відвідані та у які можна пересуватися
            if maze[i1][j1] != wall_cell:

                if waveMatrix[i1][j1] == -1:
                    q.append((i1, j1))
                # Встановлюємо відстань на одиницю більшу ніж для поточної
                waveMatrix[i1][j1] = waveMatrix[i][j] + 1

                # Встановлюємо координати звідки ми прийшли у клітину
                sources[i][j] -= 1

    # Повертаємо хвильову матрицю, та sources-матрицю
    return sources



def eolymp(n):
    maze = mazeMatrix(n)
    sources = wave(maze,(1,1),WALL_CELL)
    res = 0
    for i in range(n+2):
        for j in range(n+2):
            if sources[i][j] != None:
                res += sources[i][j]*9
    res = res - 4*9
    print(res)
    return res  # Повертаємо створений лабіринт


if __name__ == "__main__":
    n = int(input())
    eolymp(n)