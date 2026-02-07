class SyllabusProcessor:
    # init class
    def __init__(self, data):
        self.data = data
        pass

    # temporary function
    def test_process(self) -> str:
        if self.data is None:
            return "Data is None!!!"
        else:
            return self.data

    def get_class_name(self):
        #     get class name
        return "Underwater Basket Weaving"


    def initialize_syllabus(self):
        json_syllabus = {'raw_text': self.data}

        json_syllabus.append({ 'class_name': self.get_class_name()})


        return self.test_process()
