# from rest_framework.exceptions import NotFound, ValidationError
# from rest_framework.views import exception_handler
#
#
# def custom_exception_handler(exc, context):
#     response = exception_handler(exc, context)
#
#     if isinstance(exc, ValidationError):
#         response.data = {
#             "error": "Неправильные параметры фильтрации",
#             "detail": exc.detail,
#         }
#
#     if isinstance(exc, NotFound):
#         response.data = {
#             "error": "По запросу ничего не найдено",
#             "detail": exc.detail,
#         }
#     return response
