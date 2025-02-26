*** Settings ***
Library   RobotFrameworkAI
Library    Collections
Library    OperatingSystem
*** Variables ***


*** Test Cases ***
Generate Specific Test Data
     [Documentation]    Test
     ${response}=  Generate Test Data    openai    address
     Log    ${response}

Create AI assitant to learn Framework
    [Tags]    GOD
    # Define File Paths as a List
    @{FILE_PATHS} =    Create List    ${EXECDIR}\\Sample_Project\\Locators_POM
    ...    ${EXECDIR}\\Sample_Project\\Resources\\Common.robot
    ...    ${EXECDIR}\\Sample_Project\\TestCases\\Sample.robot
    Set AI Model    openai
    Set Name    Test Assistant
    Set Instructions    This assistant is capable of handling various technical queries.
    Set Model    gpt-4o
    Set Temperature    1.5
    Set Top P    0.8
#    Set Response Format    { "type": "json_object" }
    Create Assistant
    Set Message    Learn our Framework from the attached files and generate a new Robotframework script with the site specific new dynamic xpaths for the Webpage - "https://demoqa.com/automation-practice-form". Use user defined dynamic keywords like "Input Dynamic Text","Click Dynamic Text","Page should contain Dynamic Element" etc from attached Common.robot file and also generate new keywords as per the website elements. No other explanations needed.Need just the code snippet alone to save the response directly as a robot file
    ${RESPONSE}=    Send Message    file_paths=${FILE_PATHS}
    # Wait for AI response
    Sleep    15s
    Log    ${RESPONSE}

    # Save the generated files
    Create File    ${EXECDIR}\\Sample_Project\\TestCases\\NewSample3.robot    ${RESPONSE}

    Log    "Generated files saved successfully!"
    Delete Assistant