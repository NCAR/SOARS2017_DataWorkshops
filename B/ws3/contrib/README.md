# This is an overlap algorithm for finding overlap between start and end times. 

## Problem
We needed to find whether or not a satellite passes through a region of the orbit in the same local time over a seven month mission. 

## Solution
We convert the start and end time into seconds charactertistic of its position a single day and then create array for each equal to the amount of seconds in a day. We then fill each array with a '1' where the pass occurs and a zero everywhere else. We then test for overlap of the 1's between each array.
