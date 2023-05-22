clear all; close all; clc
%% Problem 5

%Not particularly clever/elegant

number=2520;
max=20;
divisors=linspace(1,max,max)

while( sum(mod(number./divisors,1)) ~= 0)
    number=number+1;
end

number

