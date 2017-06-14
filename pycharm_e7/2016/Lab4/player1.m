function [N_guess] = player1(nmin, nmax)
% this function acts as player one in the game described in Lab 4
% input arguments are the bounds on the range from which the 
% secret number is randomly selected

if(nmin>= nmax)
    error('nmax must be greater than nmin!')
else
secret = randi([nmin nmax], 1); % randomly determine key
N_guess = 0; % initialize counter
guess = secret-1; % initialize guess as something that's not the key

while( guess ~= secret) % continue until guess matches secret
    N_guess = N_guess + 1; % count the number of guesses required 
    guess = input(['Guess a number between ', num2str(nmin), ' and ', num2str(nmax), '\n']);

    if secret > guess %if the guess is too low
        fprintf('higher \n')
        nmin = guess; % next guess should be higher than the old one
    elseif secret < guess % if the guess is too high
        fprintf('lower \n')
        nmax = guess; % next guess should be lower than the old one
    else % guess matches secret
        fprintf('congratulations, you guessed the secret number in %d tries \n', N_guess)
    end
end
end
end
