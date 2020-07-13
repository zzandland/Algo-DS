class File:
    def __init__(self, name: str, content: str = ''):
        self.name = name
        self.content = content
        
class Directory:
    def __init__(self, name: str):
        self.name = name
        self.contents = {}

class FileSystem:
    def __init__(self):
        self.root = Directory('/')
        
    @staticmethod
    def _getPath(path: str) -> List[str]:
        return list(filter(bool, path.split('/')))

    def ls(self, path: str) -> List[str]:
        paths = self._getPath(path)
        n = self.root
        for path in paths:
            n = n.contents[path]
        if isinstance(n, File): return [n.name]
        return sorted((map(lambda x: x.name, n.contents.values())))

    def mkdir(self, path: str) -> None:
        paths = self._getPath(path)
        n = self.root
        for path in paths:
            if path not in n.contents: n.contents[path] = Directory(path)
            n = n.contents[path]

    def addContentToFile(self, filePath: str, content: str) -> None:
        paths = self._getPath(filePath)
        filename = paths[-1]
        n = self.root
        for path in paths[:-1]:
            n = n.contents[path]
        if filename not in n.contents: n.contents[filename] = File(filename)
        n.contents[filename].content += content

    def readContentFromFile(self, filePath: str) -> str:
        paths = self._getPath(filePath)
        n = self.root
        for path in paths:
            n = n.contents[path]
        return n.content

# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)