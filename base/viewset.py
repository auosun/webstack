from rest_framework import viewsets
from rest_framework.exceptions import ParseError


class HttpFuncViewSet(viewsets.ModelViewSet):
    """
    封装常用操作http request方法
    """

    @staticmethod
    def __get_request_data(from_, k, default=None, ignore: bool = False):
        r = from_.get(k)
        if r is None:
            if default is not None:
                return default

            if not ignore:
                raise ParseError(detail=f"lack of {k}")

        return r

    def param_get(self, k, default=None, ignore: bool = False):
        """
        从query_params键值对取值
        :param k: 键
        :param default: 默认值
        :param ignore: 如果设为false，取不到值则报错
        :return:
        """
        return self.__get_request_data(self.request.query_params, k, default, ignore)

    def payload_get(self, k, default=None, ignore=False):
        return self.__get_request_data(dict(self.request.data), k, default, ignore)
