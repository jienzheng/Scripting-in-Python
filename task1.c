#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {

// dynamically allocated memory
int *array = (int *)malloc((argc - 1) * sizeof(int));

// Read elements from command line and convert to integers
for (int i = 0; i < argc - 1; ++i) {
        array[i] = atoi (argv[i + 1]);
}

int thresh = 170;
int upperThresh = 255;
int lowerThresh = 0;

for (int i = 0; i < argc - 1; i++) {
    if (array[i] > thresh) {
        printf("%d ", upperThresh);
    }
    else {
        printf("%d ", lowerThresh);
    }
}

// Free dynamically allocated memory
free(array);

return 0;
}
