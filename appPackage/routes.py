from appPackage import appVar

@appVar.route('/')
def idx():
    return 'welcome!'