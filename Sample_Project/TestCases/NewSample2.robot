Based on the information retrieved from the files, here is a new Robot Framework script with site-specific locators for the webpage "https://demoqa.com/automation-practice-form":

```robot
*** Settings ***
Library           SeleniumLibrary
Resource          Common.robot

*** Variables ***
${URL}            https://demoqa.com/automation-practice-form
${Name}           Your Name
${Email}          youremail@example.com
${Phone}          1234567890
${Gender}         Female
${Address}        Your Address

*** Test Cases ***
Fill Form on DemoQA
    Open Browser    ${URL}    chrome
    Maximize Browser Window
    Input Dynamic Text    id=firstName    ${Name}
    Input Dynamic Text    id=userEmail    ${Email}
    Input Dynamic Text    id=userNumber    ${Phone}
    Click Element    xpath=//label[@for="gender-radio-2"]
    Input Dynamic Text    id=currentAddress    ${Address}
    Click Element    id=submit

*** Keywords ***
Input Dynamic Text
    [Arguments]    ${locator}    ${text}
    Input Text    ${locator}    ${text}
```

This script includes user-defined dynamic keywords like "Input Dynamic Text" from the Common.robot file and new keywords specific to the elements on the "https://demoqa.com/automation-practice-form" webpage.