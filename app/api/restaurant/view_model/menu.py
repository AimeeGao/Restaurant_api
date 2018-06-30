# 创建菜单view_model

class MenuCollection:
    def __init__(self, menu_list):
        self.data = []
        for menu in menu_list:
            self.data.append(MenuViewModel(menu))


class MenuViewModel:
    def __init__(self, menu):
        self.name = menu.name
        self.price = menu.price
        self.description = menu.description

    def __getitem__(self,item):
        return getattr(self, item)

    def keys(self):
        # dict(o)
        return ['name', 'price', 'description']
        #return ['name','description']


