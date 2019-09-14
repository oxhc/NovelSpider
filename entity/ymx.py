class YmxNovel:
    def __init__(self, id, chapter_id,chapter_name = '', content=''):
        print( id+" "+chapter_id+" "+chapter_name+'\n')
        self.id = id
        self.chapter_id = chapter_id
        self.content = content
        self.chapter_name = chapter_name

