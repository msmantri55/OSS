/**
 * fifteen.c
 *
 * Computer Science 50
 * Problem Set 3
 *
 * Implements Game of Fifteen (generalized to d x d).
 *
 * Usage: fifteen d
 *
 * whereby the board's dimensions are to be d x d,
 * where d must be in [DIM_MIN,DIM_MAX]
 *
 * Note that usleep is obsolete, but it offers more granularity than
 * sleep and is simpler to use than nanosleep; `man usleep` for more.
 */

#define _XOPEN_SOURCE 500

#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

// constants
#define DIM_MIN 3
#define DIM_MAX 9

// board
int board[DIM_MAX][DIM_MAX];

// dimensions
int d;

// prototypes
void clear(void);
void greet(void);
void init(void);
void draw(void);
bool move(int tile);
bool won(void);

int main(int argc, string argv[])
{
    // ensure proper usage
    if (argc != 2)
    {
        printf("Usage: fifteen d\n");
        return 1;
    }

    // ensure valid dimensions
    d = atoi(argv[1]);
    if (d < DIM_MIN || d > DIM_MAX)
    {
        printf("Board must be between %i x %i and %i x %i, inclusive.\n",
            DIM_MIN, DIM_MIN, DIM_MAX, DIM_MAX);
        return 2;
    }

    // greet user with instructions
    greet();

    // initialize the board
    init();

    // accept moves until game is won
    while (true)
    {
        // clear the screen
        clear();

        // draw the current state of the board
        draw();

        // check for win
        if (won())
        {
            printf("ftw!\n");
            break;
        }

        // prompt for move
        printf("Tile to move: ");
        int tile = GetInt();

        // move if possible, else report illegality
        if (!move(tile))
        {
            printf("\nIllegal move.\n");
            usleep(500000);
        }

        // sleep thread for animation's sake
        usleep(500000);
    }

    // success
    return 0;
}

/**
 * Clears screen using ANSI escape sequences.
 */
void clear(void)
{
    printf("\033[2J");
    printf("\033[%d;%dH", 0, 0);
}

/**
 * Greets player.
 */
void greet(void)
{
    clear();
    printf("WELCOME TO GAME OF FIFTEEN\n");
    usleep(2000000);
}

/**
 * Initializes the game's board with tiles numbered 1 through d*d - 1
 * (i.e., fills 2D array with values but does not actually print them).
 */
void init(void) {
  int tile = (d * d) - 1;
  // row
  for (int row = 0; row < d; row++) {
    // column
    for (int column = 0; column < d; column++) {
      board[row][column] = tile;
      tile--;
    }
  }

  // swap 1 and 2 if board contains odd number of tiles
  if (((d * d) - 1) % 2 != 0) {
    board[d - 1][d - 2] = board[d - 1][d - 2] + board[d - 1][d - 3];
    board[d - 1][d - 3] = board[d - 1][d - 2] - board[d - 1][d - 3];
    board[d - 1][d - 2] = board[d - 1][d - 2] - board[d - 1][d - 3];
  }
}

/**
 * Prints the board in its current state.
 */
void draw(void) {
  // loop through rows
  for (int row = 0; row < d; row++) {
    // loop through values in each row
    for (int column = 0; column < d; column++ ) {
      if (board[row][column] == 0) {
        // empty tile
        printf(" _ ");
      } else {
        // print value
        printf("%2d ", board[row][column]);
      }
    }

    printf("\n");
  }
}

/**
 * If tile borders empty space, moves tile and returns true, else
 * returns false.
 */
bool move(int tile) {
  int tile_row;
  int tile_column;
  if (tile > ((d * d) - 1)) {
    return false;
  }

  for (int row = 0; row < d; row++) {
    for (int column = 0; column < d; column++) {
      if (board[row][column] == tile) {
        tile_row = row;
        tile_column = column;
      }
    }
  }

  // get position of blank tile WRT input tile
  int tmp = board[tile_row][tile_column];
  if (tile_row > 0 && board[tile_row - 1][tile_column] == 0) {
    board[tile_row][tile_column] = board[tile_row - 1][tile_column];
    board[tile_row - 1][tile_column] = tmp;
    return true;
  } else if (tile_row <= d - 2 && board[tile_row + 1][tile_column] == 0) {
    board[tile_row][tile_column] = board[tile_row + 1][tile_column];
    board[tile_row + 1][tile_column] = tmp;
    return true;
  } else if (tile_column > 0 && board[tile_row][tile_column - 1] == 0) {
    board[tile_row][tile_column] = board[tile_row][tile_column - 1];
    board[tile_row][tile_column - 1] = tmp;
    return true;
  } else if (tile_column <= d - 2 && board[tile_row][tile_column + 1] == 0) {
    board[tile_row][tile_column] = board[tile_row][tile_column + 1];
    board[tile_row][tile_column + 1] = tmp;
    return true;
  } else {
    return false;
  }
}

/**
 * Returns true if game is won (i.e., board is in winning configuration),
 * else false.
 */
bool won(void) {
  for (int row = 0; row < d; row++) {
    for (int column = 0; column < d - 1; column++) {
      if ( board[d - 1][d - 2] == ((d * d) - 1) && board[d - 1][d - 1] == 0) {
        return true;
      }
      else if (board[row][column+1] - board[row][column] == 1) {
        continue;
      } else {
        return false;
      }
    }
  }

  return true;
}