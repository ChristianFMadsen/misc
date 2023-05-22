clear all; close all; clc
%% Problem 7

listOfPrimes = zeros(1000,1);
listOfPrimes(1,1) = 2;
listOfPrimes(2,1) = 3;


for i=2:100000
    candidate = 2*i+1;
    listOfPrimes(i+1,1)=candidate;
    for j=1:i-1
    isDivisor = mod(candidate/(2*j+1),1);
        if isDivisor==0
            listOfPrimes(i+1,1)=0;
                break
        end
    end
end

listOfPrimes = nonzeros(listOfPrimes)