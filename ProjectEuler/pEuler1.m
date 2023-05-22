clear all; close all;
% Problem 1

multOfFiveBelow = 1000/5;

listOfFiveMult = zeros(multOfFiveBelow,1);

i=0;
while i*5 < 995
    i=i+1;
    listOfFiveMult(i,1) = i*5;
end

listOfFiveMult = nonzeros(listOfFiveMult);

listOfThreeMult = zeros(ceil(1000/3),1);

j=0;
while j*3 < 999
    j=j+1;
%     listOfThreeMult(j,1) = j*3;
    if mod(j*3,5)~=0
        listOfThreeMult(j,1) = j*3;
    end
end

listOfThreeMult = nonzeros(listOfThreeMult);

fiveSum = 0;
for i=1:length(listOfFiveMult)
    fiveSum=fiveSum+listOfFiveMult(i,1);
end


threeSum = 0;
for i=1:length(listOfThreeMult)
    threeSum=threeSum+listOfThreeMult(i,1);
end


ans = fiveSum+threeSum
