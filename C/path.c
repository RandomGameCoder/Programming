#include <stdio.h>
#include <stdlib.h>

// function to check if a position is valid and can be visited
int isValid(int x, int y, int n, int m, int maze[][m])
{
    // check if the position is inside the maze and can be visited
    if (x >= 0 && x < n && y >= 0 && y < m && maze[x][y] == 0)
        return 1;
    return 0;
}

// function to find a path through the maze using backtracking
int findPath(int x, int y, int n, int m, int maze[][m])
{
    // if the current position is the destination, return true
    if (x == n - 1 && y == m - 1)
        printf("Reached Destination : (%d, %d)\n", x, y);
        return 1;

    // mark the current position as visited
    printf("Current Position : (%d, %d)\n", x, y);
    maze[x][y] = 2;

    // try moving in each direction
    int dx[8] = {1, 0, 1, -1, 1, -1, 0, -1};
    int dy[8] = {1, 1, 0, 1, -1, 0, -1, -1};
    for (int i = 0; i < 8; i++)
    {
        int new_x = x + dx[i];
        int new_y = y + dy[i];

        // if the new position is valid and can be visited, try to find a path from there
        if (isValid(new_x, new_y, n, m, maze))
        {
            printf("Current Position : (%d, %d)\n", x, y);
            return findPath(new_x, new_y, n, m, maze);
        }
    }

    // if no path was found, backtrack and mark the current position as not visited
    maze[x][y] = 0;
    return 0;
}

int main()
{
    // read n and m from the user
    int n, m;
    printf("Enter the number of rows: ");
    scanf("%d", &n);

    printf("Enter the number of columns: ");
    scanf("%d", &m);

    // dynamically allocate the maze
    int (*maze)[m] = malloc(sizeof(int[n][m]));

    // read the maze from the user
    printf("Enter the maze (0 for empty cell, 1 for obstacle):\n");
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            scanf("%d", &maze[i][j]);
        }
    }

    // print the maze
    printf("\nThe maze is:\n");
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            printf("%d ", maze[i][j]);
        }
        printf("\n");
    }

    // try to find a path through the maze
    int x = findPath(0, 0, n, m, maze);

    if (x == 1)
    {
        printf("Found a path through the maze!\n");
    }
    else
    {
        printf("Could not find a path through the maze.\n");
    }

    // free the dynamically allocated memory
    free(maze);
    return 0;
}
