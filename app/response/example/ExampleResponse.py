from ..BaseResponse import BaseResponse


class ExampleResponse(BaseResponse):

    field = ''

    def __init__(self):
        super().__init__()

    def success(self):
        data = {
            # TODO response data
            'field': self.field
        }
        return super().success(data)