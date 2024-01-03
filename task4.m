% Reads in the Mickey png.
img = imread('mickey.png');

% Reshapes Mickey to a 1D array.
img_1d = reshape(img, [1, 65536]);

% Writes the pixels into the input.txt file with spaces in between.
dlmwrite('input.txt', img_1d, 'delimiter', ' ');
