class OpenFile:
    def __init__(self, path, type):
        self.file = open(path, type)
    
    def __enter__(self):
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
 
 
with OpenFile('hello.txt', 'wt') as f:
    f.write('Мой контекстный менеджер делает тоже самое!')