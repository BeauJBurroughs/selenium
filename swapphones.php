<?php

namespace Facebook\WebDriver;

use Facebook\WebDriver\Remote\DesiredCapabilities;
use Facebook\WebDriver\Remote\RemoteWebDriver;

require_once('vendor/autoload.php');

$EXT1 = $_REQUEST['swap1'];
$EXT2 = $_REQUEST['swap2'];
//FOR TESTING
//$EXT1 = 310;
//$EXT2 = 309;

// start firefox
$host = 'http://localhost:4444/wd/hub'; // this is the default
$desired_capabilities = DesiredCapabilities::firefox();
$desired_capabilities->setCapability('acceptSslCerts', false);
//TO RUN HEADLESS
$desired_capabilities->setCapability('moz:firefoxOptions', ['args' => ['-headless']]);
$driver = RemoteWebDriver::create($host, $desired_capabilities);

// navigate to 'http:/10.40.51'
$driver->get('http://10.40.0.51');

// print the title of the current page
echo "The title is '" . $driver->getTitle() . "'\n";
echo "<br>";
// print the URI of the current page
echo "The current URI is '" . $driver->getCurrentURL() . "'\n";
echo "<br>";
//print Extension EXT1 and Extension Swapped
echo "<center>";
echo "Extension " . $EXT1 . " and Extension " . $EXT2 . " Swapped";
echo "</center>";
echo "<br>";

//switch to frame
$my_frame='mainFrm';
$driver->switchTo()->frame($my_frame);

//write 'ADMIN2' in the USERNAME box
$driver->findElement(WebDriverBy::name('userName'))
   ->sendKeys('ADMIN2');

//write '9999' in password box
$driver->findElement(WebDriverBy::name('password'))
   ->sendKeys('9999'); // fill PASSWORD BOX

// click the link 'Login'
$Login_link = $driver->findElement(WebDriverBy::linkText('Login'));
$Login_link->click();
// wait 10 sec
$driver->manage()->timeouts()->implicitlyWait(10);

// click the link 'Swap'
$Swap_link = $driver->findElement(
    WebDriverBy::linkText('Swap')
);
$Swap_link->click();

//select phones to swap
$xpath1 = "(//option[@value='" . $EXT1 . "'])";
$xpath2 = "(//option[@value='" . $EXT2 . "'])[2]";
$swap1 = $driver->findElement(WebDriverBy::xpath($xpath1));
$swap1->click();
$swap2 = $driver->findElement(WebDriverBy::xpath($xpath2));
$swap2->click();

// click the link 'Apply'
$Apply_link = $driver->findElement(WebDriverBy::linkText('Apply'));
$Apply_link->click();

// click the link 'Home'
$Home_link = $driver->findElement(
    WebDriverBy::linkText('Home')
);
$Home_link->click();

// click the link 'Logout'
$Logout_link = $driver->findElement(
    WebDriverBy::linkText('Logout')
);
$Logout_link->click();

// close the browser
$driver->quit();
