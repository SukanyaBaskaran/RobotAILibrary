*** Settings ***
Library    Browser  timeout=30s
Resource   ../Resources/Common.robot
Library    SeleniumLibrary

Test Setup    Create Screenshot Folder
Test Teardown    Test Teardown Activities for dry run
#Suite Teardown    Close all browsers


*** Variables ***
${Browser}    Chromium
${Url}    https://demoqa.com/automation-practice-form

*** Test Cases ***
Open Browser and Check Title
    [Tags]    TC01
    new browser    ${Browser}   headless=False
    new page    ${Url}  wait_until=load
    wait for load state    timeout=20s
    new page    ${Url}  wait_until=load
    wait for load state    timeout=20s
    close context    CURRENT