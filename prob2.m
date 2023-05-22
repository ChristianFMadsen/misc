clear all; close all;
%% Problem 2

AmountOfFibNumbers = 100;

FibNumbers = zeros(AmountOfFibNumbers,1);
FibNumbers(1,1)=1;
FibNumbers(2,1)=2;


i=2;
while i <= AmountOfFibNumbers
    i=i+1;
    FibNumbers(i,1)=FibNumbers(i-1,1)+FibNumbers(i-2,1);
end

for i=1:length(FibNumbers)
    if FibNumbers(i,1) > 4*10^6 | mod(FibNumbers(i,1),2) == 1
        FibNumbers(i,1) = 0;
    end
end
FibNumbers = nonzeros(FibNumbers);

ans = sum(FibNumbers)