clear all; close all; clc
%% Problem 3

listOfPrimes = zeros(1000,1);
listOfPrimes(1,1) = 2;
listOfPrimes(2,1) = 3;


for i=2:10000
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

number=600851475143;

listOfPrimeFactors = zeros(50,1);

for i=1:length(listOfPrimes)
    if mod(number/listOfPrimes(i,1),1)==0
        listOfPrimeFactors(i,1)=listOfPrimes(i,1);
    end
end
listOfPrimeFactors = nonzeros(listOfPrimeFactors)

product=1;
for i=1:length(listOfPrimeFactors)
    product=product*listOfPrimeFactors(i,1);
end

test = product/number
