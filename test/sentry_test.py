import sentry_sdk
# sentry_sdk.init("http://5fcb99f8d6034ba2bd3cfe6eeec15148@192.168.206.133:9000/4",max_breadcrumbs=50,debug=False)

from sentry_sdk import capture_exception

try:
    print("3")
    print(1/0)
    print("4")
except Exception as e:
    sentry_sdk.capture_exception(e)
    print("fdfs")