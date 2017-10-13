function [movie] = createMovie(pattern)
%set the initial background 
pic = %TO BE COMPLETED
%set 'movie' as a VideoWriter object
movie = VideoWriter('myMovie.avi');
%specify the number of frames to show per second
movie.FrameRate = %TO BE COMPLETED
%open the movie file
open(movie);
%loop to show each step of the cellular automaton
for %TO BE COMPLETED      
    pic = %TO BE COMPLETED
    %display the image
    imshow(pic);
    %capture the frame
    frame = getframe;
    %add the new frame to the movie
    writeVideo(movie,frame);
end
%close the movie file
close(movie); 
end