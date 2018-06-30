from app.libs.enums import PlatFormEnum


class CourseCollection:
    def __init__(self, course_list, legals_of_mine):
        self.data = []
        for course in course_list:
            self.data.append(CourseViewModel(course, legals_of_mine))


class CourseViewModel:
    def __init__(self, course, legals_of_mine):
        self.name = course.name
        self.platform = PlatFormEnum.platform_str(course.platform)
        self.verify = False
        self.slogan = course.slogan
        self.thumbnail = course.thumbnail
        self.link = self.get_link(course.pcid)
        # 将发送给前端的id改为慕课网的pcid，不用本系统的id号
        self.id = course.pcid
        self.has_content = course.has_content
        # self.pcid = course.pcid

        for legal in legals_of_mine:
            if legal.cid == course.id:
                self.verify = True

    def get_link(self, id):
        return 'https://coding.imooc.com/class/{}.html'.format(id)

    def __getitem__(self, item):
        return getattr(self, item)

    def keys(self):
        return ['name', 'platform', 'verify', 'slogan', 'thumbnail', 'link', 'id', 'has_content']
