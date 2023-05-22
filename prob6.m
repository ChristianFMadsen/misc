clear all; close all; clc
%% Problem 6
n=100;

sumOfSquares = 0;
for i=1:n
    sumOfSquares=sumOfSquares+i^2;
end


squareOfSum = (n*(n+1)/2)^2;

difference = squareOfSum-sumOfSquares


