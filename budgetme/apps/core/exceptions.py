from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    handlers = {
        'NotFound': _process_not_found_error,
        'ValidationError': _process_generic_error
    }

    exception_class = exc.__class__.__name__
    if exception_class in handlers:
        return handlers[exception_class](exc, context, response)

    return response


def _process_generic_error(exc, context, response):
    errors = response.data
    if 'error' in errors:
        errors = errors['error']

    response.data = {
        'errors': errors
    }

    return response


def _process_not_found_error(exc, context, response):
    view = context.get('view', None)

    if view and hasattr(view, 'queryset') and view.queryset is not None:
        error_key = view.queryset.model._meta.verbose_name

        response.data = {
            'errors': {
                error_key: response.data['detail']
            }
        }
    else:
        response = _process_generic_error(exc, context, response)

    return response
