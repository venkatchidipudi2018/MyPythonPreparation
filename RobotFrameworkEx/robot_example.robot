*** Settings ***
Library SeleniumLibrary

*** Variables ***
${MY_VARIABLE} Hello World

*** Keywords ***
Login With Credentials From CSV
[Arguments] ${filename}
${data}= Get File ${filename}
: FOR ${row} IN @{data}
${username}= Set Variable ${row['username']}
${password}= Set Variable ${row['password']}
Login ${username} ${password}

*** Test Cases ***
Login Test
[Documentation] Test the login functionality
: TRY
Login john.doe password
Log Login successful
: EXCEPT AssertionError
Log Login failed: username or password is incorrect
