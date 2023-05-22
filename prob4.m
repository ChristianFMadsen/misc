clear all; close all; clc
%% Problem 4


largestPalindrome=0;
for i=100:999
    for j=100:999
        number = i*j;
        reverseNumber = str2num(reverse(num2str(number)));
        if number==reverseNumber
            if number>largestPalindrome
                largestPalindrome=number;
            end
        end
    end
    end

largestPalindrome