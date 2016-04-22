#!/usr/bin/php
<?php
	$bigString = file_get_contents( "/var/www/html/bigString.txt" );

	$pattern1 = '/\w*(?=\sbetray\sthe\sfore)/';
	preg_match($pattern1, $bigString, $match1);
	foreach($match1 as $value) {
		print($value."<br>");
	}
	$pattern2 = '/\w*(?=\sspongy\slungs\sbestowed)/';
	preg_match($pattern2, $bigString, $match2);
	foreach($match2 as $value) {
		print($value."<br>");
	}
	$pattern3 = '/\w*(?=\sjson\sobject\snotation)/';
	preg_match($pattern3, $bigString, $match3);
	foreach($match3 as $value) {
		print($value."<br>");
	}
	// for output consistency
	print("null<br>");
	$pattern4 = '/\w*(?=\sshould\sdo\sagain\sfor\ssuch\sa\ssake)/';
	preg_match($pattern4, $bigString, $match4);
	foreach($match4 as $value) {
		print($value."<br>");
	}
	$pattern5 = '/\w*(?=\sthat\sfalse\sfire)/';
	preg_match($pattern5, $bigString, $match5);
	foreach($match5 as $value) {
		print($value."<br>");
	}
	$pattern6 = '/\w*(?=\sforced\sthunder\sfrom\shis\sheart)/';
	preg_match($pattern6, $bigString, $match6);
	foreach($match6 as $value) {
		print($value);
	}
	$pattern7 = '/\w*(?=\sthy)/';
	preg_match_all($pattern7, $bigString, $match7);
	foreach($match7 as $value) {
		/*foreach($value as $v) {
			print($v." ");
		}*/
		print("<br>found ".count($value)." words preceding 'thy'");
	}
	$pattern8 = '/\w*(?=\sthee)/';
	preg_match_all($pattern8, $bigString, $match8);
	foreach($match8 as $value) {
		/*foreach($value as $v) {
			print($v." ");
		}*/
		print("<br>found ".count($value)." words preceding 'thee'");
	}
	$pattern9 = '/\w*(?=\sthine)/';
	preg_match_all($pattern9, $bigString, $match9);
	foreach($match9 as $value) {
		/*foreach($value as $v) {
			print($v." ");
		}*/
		print("<br>found ".count($value)." words preceding 'thine'");
	}
?>
