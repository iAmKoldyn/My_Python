from selenium import webdriver
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# options = webdriver.ChromeOptions()
# options.headless =  True

# driver = webdriver.Chrome(options=options)
# driver.get(URL)
# sleep(1)
# scheight = .1
# while scheight < 9.9:
#     sleep(3)
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight/%s);" % scheight)
#     scheight += .01
#     S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
#     driver.set_window_size(S('Width'),S('Height')) # May need manual adjustment
#     driver.find_element_by_tag_name('body').screenshot('web_screenshot.png')

# driver.quit()

# options = webdriver.ChromeOptions()
# options.headless = True

# driver = webdriver.Chrome()
# driver.get(URL)

# scheight = .1
# while scheight < 9.9:
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight/%s);" % scheight)
#     scheight += .01

#     S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
#     driver.set_window_size(S('Width'),S('Height')) # May need manual adjustment
#     driver.find_element_by_tag_name('body').screenshot('web_screenshot.png')

# driver.quit()

# scheight = .1
# while scheight < 9.9:
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight/%s);" % scheight)
#     scheight += .01


# 
# 
# 
# 

# driver = webdriver.Chrome()
# driver.get('https://developer.mozilla.org/')
# element = driver.find_element_by_tag_name('body')
# element_png = element.screenshot_as_png
# with open("test2.png", "wb") as file:
#     file.write(element_png)


# def fullpage_screenshot(driver, file):

#         print("Starting chrome full page screenshot workaround ...")

#         total_width = driver.execute_script("return document.body.offsetWidth")
#         total_height = driver.execute_script("return document.body.parentNode.scrollHeight")
#         viewport_width = driver.execute_script("return document.body.clientWidth")
#         viewport_height = driver.execute_script("return window.innerHeight")
#         print("Total: ({0}, {1}), Viewport: ({2},{3})".format(total_width, total_height,viewport_width,viewport_height))
#         rectangles = []

#         i = 0
#         while i < total_height:
#             ii = 0
#             top_height = i + viewport_height

#             if top_height > total_height:
#                 top_height = total_height

#             while ii < total_width:
#                 top_width = ii + viewport_width

#                 if top_width > total_width:
#                     top_width = total_width

#                 print("Appending rectangle ({0},{1},{2},{3})".format(ii, i, top_width, top_height))
#                 rectangles.append((ii, i, top_width,top_height))

#                 ii = ii + viewport_width

#             i = i + viewport_height

#         stitched_image = Image.new('RGB', (total_width, total_height))
#         previous = None
#         part = 0

#         for rectangle in rectangles:
#             if not previous is None:
#                 driver.execute_script("window.scrollTo({0}, {1})".format(rectangle[0], rectangle[1]))
#                 time.sleep(0.2)
#                 driver.execute_script("document.getElementById('topnav').setAttribute('style', 'position: absolute; top: 0px;');")
#                 time.sleep(0.2)
#                 print("Scrolled To ({0},{1})".format(rectangle[0], rectangle[1]))
#                 time.sleep(0.2)

#             file_name = "part_{0}.png".format(part)
#             print("Capturing {0} ...".format(file_name))

#             driver.get_screenshot_as_file(file_name)
#             screenshot = Image.open(file_name)

#             if rectangle[1] + viewport_height > total_height:
#                 offset = (rectangle[0], total_height - viewport_height)
#             else:
#                 offset = (rectangle[0], rectangle[1])

#             print("Adding to stitched image with offset ({0}, {1})".format(offset[0],offset[1]))
#             stitched_image.paste(screenshot, offset)

#             del screenshot
#             os.remove(file_name)
#             part = part + 1
#             previous = rectangle

#         stitched_image.save(file)
#         print("Finishing chrome full page screenshot workaround...")
#         return True


# driver = webdriver.Chrome()

# ''' Generate document-height screenshot '''
# url = "http://effbot.org/imagingbook/introduction.htm"
# url = "http://www.w3schools.com/js/default.asp"
# driver.get(url)
# fullpage_screenshot(driver, "test1236.png")