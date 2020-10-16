Die folgenden Library müssen erst installiert werden.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
robotframework                   
robotframework-pageobjectlibrary 
robotframework-pythonlibcore     
robotframework-selenium2library  
robotframework-seleniumlibrary   
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

*****PageObject*****
Mit PageObject kann man Keywords in Robotframework benutzen und anschließend auch Keywords vom SeleniumLibarary direkt benutzen.

Wenn man mit sl = SeleniumLibarary() ein Instance anlegt und mit sl.open_browser ein neues Browser öffnet, kann die Keyword aus Selenium nicht den Instance bearbeiten.

Beim PageObject gibt es Schwäche, dass beim Unittest kann die Keywords nicht durchgeführt werden.


