*** Settings ***
Documentation     A test suite with a single test for valid login.
...
...               This test has a workflow that is created using keywords in
...               the imported resource file.
#Resource          resource.robot
Library           Common_copy.py
Library          SeleniumLibrary


*** Test Cases ***
Valid Login
    Open Browser       http://localhost:7272/
    Input Username1       demo
    Input Text    "password_field"    mode