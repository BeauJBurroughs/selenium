<?php

namespace Facebook\WebDriver;

use Facebook\WebDriver\Remote\DesiredCapabilities;
use Facebook\WebDriver\Remote\RemoteWebDriver;

require_once('../vendor/autoload.php');

// start firefox
$host = 'http://localhost:4444/wd/hub'; // this is the default
$desired_capabilities = DesiredCapabilities::firefox();
$desired_capabilities->setCapability('acceptSslCerts', false);
//TO RUN HEADLESS
$desired_capabilities->setCapability('moz:firefoxOptions', ['args' => ['-headless']]);

$driver = RemoteWebDriver::create($host, $desired_capabilities);

// navigate to 'https://clock.payrollservers.us/?wl=payday.payrollservers.us#/clock/web/login'
$driver->get('https://clock.payrollservers.us/?wl=payday.payrollservers.us#/clock/web/login');
// wait 10 sec
$driver->manage()->timeouts()->implicitlyWait(10);

// print the title of the current page
echo "The title is '" . $driver->getTitle() . "'\n";
echo "<br>";
// print the URI of the current page
echo "The current URI is '" . $driver->getCurrentURL() . "'\n";
echo "<br>";


//write 'tabeytanbgs' in the USERNAME box
$driver->findElement(WebDriverBy::id('Username'))
   ->sendKeys('username');

//write 'P@ssword1' in password box
$driver->findElement(WebDriverBy::id('Password'))
   ->sendKeys('password');

// click the link 'Login'
$Login = $driver->findElement(WebDriverBy::id('Login'));
$Login->click();
// wait 10 sec
$driver->manage()->timeouts()->implicitlyWait(10);

// clockin
//$clockin = "(//button[@id='ClockIn']/div)";
//$clockin = $driver->findElement(WebDriverBy::xpath($clockin));
//$clockin->click();

//clockout
//$clockout = "(//button[@id='ClockOut']/div)";
//$clockout = $driver->findElement(WebDriverBy::xpath($clockout));
//$clockout->click();

//signout
$signout = $driver->findElement(WebDriverBy::id('SignOut'));
$signout->click();

//close the browser
$driver->quit();


// print successfull clockin
echo "<br>";
echo "Successfull ClockIn at " . date("Y/m/d"). "<br>" . date("h:i:sa");
echo "<br>";

// print successfull clockout
echo "<br>";
echo "Successfull ClockOut at " . date("Y/m/d") . "<br>" . date("h:i:sa");
echo "<br>";


?>
