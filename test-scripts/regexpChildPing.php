<?php
    /*  * This is the process being called by the user.
        * From here, we'll launch child process child.php */
    
    // open child process
    $child = popen('sleep 5; echo "slept 5"', 'r');
    
    /*  * Do some work, while already doing other
        * work in the child process. */

    // get response from child (if any) as soon at it's ready:
    $response = stream_get_contents($child);

    pclose($child);
    
    print($response);
?>
