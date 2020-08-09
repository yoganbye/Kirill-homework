# Самостоятельно познакомиться с паттернами Factory (фабрика) и Factory method 
# (фабричный метод) и решить следующую задачу:
# «Есть некоторый общий класс родитель Tag, который хранит в себе какой-то HTML тег 
# (например: <tag></tag>). От Tag наследуются еще четыре класса Image, Input, Text 
# (т. е <p></p>), Link (т. е <a></a>).
# С использованием указанных паттернов реализовать следующее поведение: 
# Должна быть возможность создать необходимый тег, явно его не создавая, т. е не через 
# img = Image(), а через фабричный метод или фабрику, например factory.create_tag(name).»

# Пример того, как это должно работать представлен на следующем слайде.

# *Дополнительно:
# Реализовать возможность опциональной передачи атрибутов для тегов, т. е атрибуты могут быть 
# (src для image, href для a и. т. д.) , а могут и не быть.

from abc import ABC, abstractmethod


class FactoryTag(ABC):
    def get_tag(self=''):
        return('<tag></tag>')


class Tag(FactoryTag):
    def get_tag(self, name=''):
        if name == 'image':
            return ImageFactory.get_tag()
        elif name == 'input':
            return InputFactory.get_tag()
        elif name == 'p':
            return TextFactory.get_tag()
        elif name == 'a':
            return LinkFactory.get_tag()
        else:
            return FactoryTag.get_tag()
    

class ImageFactory(Tag):    
    def get_tag(self=''):
        return ('<img>')


class InputFactory(Tag):
    def get_tag(self=''):
        return ('<input></input>')


class TextFactory(Tag):
    def get_tag(self=''):
        return ('<p></p>')


class LinkFactory(Tag):
    def get_tag(self=''):
        return ('<a></a>')


if __name__ == '__main__':
    player = Tag()
    elements = ['image', 'p', '', 'a', 'input']
    for i in elements:
        print(player.get_tag(i))



