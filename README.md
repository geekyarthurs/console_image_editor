# Samuel's Edit

Developer: [Mahesh C. Regmi](https://facebook.com/xSamuelArthursx)



Samuel's Edit is a console-based image editor built on top of Python.

  - Add text
  - Resize Images
  - Scaling and Pasting

# Upcoming Features!

  - Cursor's Feature
  - Efficient pasting 
  - Filters addition




### Tech

Samuel's Edit uses a number of open source projects (or not ) to work properly:

* [OpenCV] - Enhanced Computer Vision for processing Images
* [PIL] - Efficient Image Processing library on python3.


And of course Samuel's Edit itself is open source with a [public repository][samueledits] on GitHub.

### Installation

Samuel's Edit requires openCV and PIL to run properly.

Install the dependencies and devDependencies and start the server.
Refer to this link to install opencv [Install OpenCV](https://docs.opencv.org/3.4/d2/de6/tutorial_py_setup_in_ubuntu.html)

```sh
$ cd samueledits
$ pip install pipenv
$ pipenv shell
$ sudo pip install requirements.txt
$ python3 main.py <image_name>
```
##### Virtual Env Installations

```sh

$ cd samueledits
$ pip install pipenv
$ pipenv shell
$ sudo pip install -r requirements.txt
$ python3 main.py <image_name>

```
##### Opening Image in SamuelEdits

You can open image on samueledits by this command.
```sh
python3 main.py <image_name>
```

You can change image if opened once using the command given below.
```sh
python3 main.py change <image_name>
```

##### Open Viewed Image

See the image by just typing show.

```sh
>show
```


##### Getting Image Resolution

Get the image resolution (width or height) by the command below.

```sh
>shape
```

##### Rotating Image

You can rotate image in any degree you want as simple as this ( this rotates in clockwise direction)

```sh
>rotate 90
```
You can provide clockwise or anticlockwise by using another parameter.

```python
>rotate 90 c #clockwise
>rotate 90 ac #anticlockwise
```

##### Cropping Image
You can crop image by passing either two values to start from top end or start from custom end.
It's very easy.
```python
>crop 20 10 # crops from 10 to the bottom and 20 to the right
>crop 20 10 100 200 # crops image from 20 to 100 on length and 10 to 200 on height.
```

##### Getting Points on the Image
If you are confused where to put the image , text or cropping you can get where is the current (x,y) by command below.

```python
>point 10 20 # point (10,20) - (x,y) on the image.
```

##### Adding Text to Image

You can add text to the image by some easy steps.

First initialize your text by sending scale factor, text and color.

```python
>text 1-hello world-white
>text 0.5-hi-black
```

Since the text is initialized, you can now write the text into the image by passing where you want to put it.

```python
>write 100 100 # (x,y) = (100,100)
```

##### Reset Changes

Reset changes by simply typing reset.

```python
>reset
```





### Development

Want to contribute? Great!
Thanks to Aju100 and TheBinitGhimire.

### Todos

 - Write MORE Tests
 - Add Night Mode

License
----

MIT


**Free Software, Hell Yeah!**




   
