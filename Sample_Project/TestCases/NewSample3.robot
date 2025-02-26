```robot
*** Settings ***
Library    SeleniumLibrary
Variables  ../Locators_POM/Locators.py
Resource   Common.robot

*** Variables ***
${URL}     https://demoqa.com/automation-practice-form

*** Test Cases ***
Fill Form with Dynamic XPaths
    Open Browser    ${URL}    Chrome
    Maximize Browser Window
    Input Dynamic Text    //input[@id='firstName']    John
    Input Dynamic Text    //input[@id='lastName']    Doe
    Input Dynamic Text    //input[@id='userEmail']    john.doe@example.com
    Click Dynamic Text    //label[@for='gender-radio-1']
    Input Dynamic Text    //input[@id='userNumber']    1234567890
    Input Dynamic Text    //input[@id='dateOfBirthInput']    01 Jan 2000
    Click Dynamic Text    //label[text()='Reading']
    Input Dynamic Text    //textarea[@id='currentAddress']    123 Main St
    Page Should Contain Dynamic Element    //button[@id='submit']
    Click Dynamic Text    //button[@id='submit']
    [Teardown]    Close Browser

*** Keywords ***
Input Dynamic Text
    [Arguments]    ${xpath}    ${text}
    Wait Until Element Is Visible    ${xpath}
    Input Text    ${xpath}    ${text}

Click Dynamic Text
    [Arguments]    ${xpath}
    Wait Until Element Is Visible    ${xpath}
    Click Element    ${xpath}

Page Should Contain Dynamic Element
    [Arguments]    ${xpath}
    Wait Until Element Is Visible    ${xpath}
    Element Should Be Visible    ${xpath}
```