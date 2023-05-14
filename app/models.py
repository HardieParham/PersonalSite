class WorkCard():
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.works = []

    def add_works(self, works_list: list):
        self.works = works_list


class Works():
    works_list = []

    def __init__(self, description: str, link: str):
        self.image_link = link
        self.description = description
        Works.works_list.append(self)

    def __repr__(self):
        return f'{self.description}'


RLG = WorkCard('RLG', 'Project Structural Engineer')
stA = Works('St Andrews', 'test.png')
Sharron = Works('Sharron Church', 'test2.png')
RLG.add_works(Works.works_list)

print(RLG.works)
