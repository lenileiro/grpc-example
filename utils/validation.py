import grpc
class ErrorHandler:
    @staticmethod
    def isvalid(field,request, context):
            try:
                if not request:
                    context.set_code(grpc.StatusCode.NOT_FOUND)
                    context.set_details(f'{field} field required')
            except Exception as e:
                print(e)
            finally:
                if isinstance(request, str):  
                    if request.strip() == '':
                        context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
                        context.set_details(f'{field} cannot be blank')
                if isinstance(request, int):
                    if not request > 4:
                        context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
                        context.set_details(f'{field} cannot be less than one')