int** transpose(int** matrix, int matrixSize, int* matrixColSize, int* returnSize, int** returnColumnSizes) {
    int rows = matrixSize;
    int cols = *matrixColSize;
    
    *returnSize = cols;
    *returnColumnSizes = (int*)malloc(sizeof(int) * cols);
    int** result = (int**)malloc(sizeof(int*) * cols);

    for (int i = 0; i < cols; i++) {
        (*returnColumnSizes)[i] = rows;
        result[i] = (int*)malloc(sizeof(int) * rows);
        for (int j = 0; j < rows; j++) {
            result[i][j] = matrix[j][i];
        }
    } // End of inner loop

    return result;
} // <--- MAKE SURE THIS BRACE EXISTS AND IS THE LAST THING IN THE FILE

