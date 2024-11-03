from robot import *
from link_extractor import *
from urllib.request import urlopen
from image_extractor import *


if __name__ == '__main__':
    # prepare('http://www.apress.com/robot.txt')
    # print(is_allowed('http://hajba.hu/category/software-development/java-software-development/','bookbot'))
    target_url = 'http://www.apress.com/'
    apress = download_page(target_url)
    # links = extract_links(apress)
    # for link in links:
    #     print(link)
    image_locations = extract_image_locations(apress)

    for src in image_locations:
        print(src)