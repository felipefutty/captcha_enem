<?php

include("anticaptcha.php");
include("imagetotext.php");

$api = new ImageToText();
$api->setVerboseMode(true);
        
//your anti-captcha.com account key
// TODO: ADD YOUR KEY
$api->setKey("");


// csv found
// TODO: fill <> with your 3 letters name
$mycsv = fopen("dataset-<>.csv", "w") or die("Unable to open file!");

for ($i = 1; $i <= 1000; $i++){
	//setting file
	// TODO: fill <path> with the path to your captcha imagens and <letters> with your 3 letters name
	$api->setFile("<path>/$i-<letters>.png");

	if (!$api->createTask()) {
    		$api->debout("API v2 send failed - ".$api->getErrorMessage(), "red");
   	 	return false;
	}

	$taskId = $api->getTaskId();


	if (!$api->waitForResult()) {
    		$api->debout("could not solve captcha", "red");
    		$api->debout($api->getErrorMessage());
	} else {
		$txt = "$i-frn,".$api->getTaskSolution()."\n";
		fwrite($mycsv, $txt);
    		echo $txt;
	}
}
fclose($mycsv);
