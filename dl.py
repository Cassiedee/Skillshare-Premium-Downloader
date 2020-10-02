import sys
from skillshare import Skillshare

# or by class ID:
# dl.download_course_by_class_id(189505397)

def main():
    dl = Skillshare()
    course_url = sys.argv[1]
    dl.download_course_by_url(course_url)


def info():
    print('###########################################################################')
    print('###########################SkillShare Downloader###########################')
    print('###########################################################################')


if __name__ == "__main__":
    info()
    main()


    
