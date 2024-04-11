#Practice Questions
# 1. Briefly describe the differences between the webbrowser, requests, bs4, and selenium modules.
    # webbrowser allows you to open urls in the browser from python programs
    # requests allows you to interact with websites and apis, retrieve and send information to and from them
    # bs4 is a tool for webscraping, it makes html easier to parse
    # selenium is a tool that allows you to interact directly with a website through code

# 2. What type of object is returned by requests.get()? How can you access the downloaded content as a string value?
    # a Response object
    # using the text attribute

# 3. What requests method checks that the download worked?
    # .raise_for_status()
    
# 4. How can you get the HTTP status code of a requests response?
    # Response.status_code

# 5. How do you save a requests response to a file?
    # you can open a new file, write it in binary using iter_content(chunk)

# 6. What is the keyboard shortcut for opening a browser’s developer tools?
    # Command Option I

# 7. How can you view (in the developer tools) the HTML of a specific element on a web page?
    # Right click on the element and choose Inspect

# 8. What is the CSS selector string that would find the element with an id attribute of main?
    # #main

# 9. What is the CSS selector string that would find the elements with a CSS class of highlight?
    # '.highlight'

# 10. What is the CSS selector string that would find all the <div> elements inside another <div> element?
    # 'div div'

# 11. What is the CSS selector string that would find the <button> element with a value attribute set to favorite?
    # 'button[value="favorite"]'

# 12. Say you have a Beautiful Soup Tag object stored in the variable spam for the element <div>Hello, world!</div>. 
#     How could you get a string 'Hello, world!' from the Tag object?
    # spam.getText()

# 13. How would you store all the attributes of a Beautiful Soup Tag object in a variable named linkElem?
    # linkElem.attrs

# 14. Running import selenium doesn’t work. How do you properly import the selenium module?
    # from selenium import webdriver

# 15. What’s the difference between the find_element_* and find_elements_* methods?
    # find_element finds the first, find_elements finds all

# 16. What methods do Selenium’s WebElement objects have for simulating mouse clicks and keyboard keys?
    # the .click method and .send_keys()

# 17. You could call send_keys(Keys.ENTER) on the Submit button’s WebElement object, 
#     but what is an easier way to submit a form with selenium?
    # call the submit() method on the form

# 18. How can you simulate clicking a browser’s Forward, Back, and Refresh buttons with selenium?
    # using the .forward(), .back(), .refresh() methods