1. What is an RGBA value?
    - red, green, blue, alpha. each is an integer 256 (0,255) total options to create a color

2. How can you get the RGBA value of 'CornflowerBlue' from the Pillow module?
    - ImageColor.getcolor('CornflowerBlue', 'RGBA')

3. What is a box tuple?
    - a tuple value that contains 4 integers for the left edge x coordinate, top y coordiante and width and height

4. What function returns an Image object for, say, an image file named zophie.png?
    - Image.open('zophie.png')

5. How can you find out the width and height of an Image object’s image?
    size method returns a tuple of width, height

6. What method would you call to get Image object for a 100×100 image, excluding the lower-left quarter of it?
    - ImageObj.crop((0,50,50,50))

7. After making changes to an Image object, how could you save it as an image file?
    - using the save method

8. What module contains Pillow’s shape-drawing code?
    ImageDraw

9. Image objects do not have drawing methods. What kind of object does? How do you get this kind of object?
     - ImageDraw objects. you pass the Image object to ImageDraw.Draw()