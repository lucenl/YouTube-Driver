from webdriver_manager.core.os_manager import OperationSystemManager, ChromeType

def time2seconds(s):
    """
    Converts a given time (video duration, ad time, etc.) to seconds
    """
    s = s.split(':')
    s.reverse()
    wait = 0
    factor = 1
    for t in s:
        wait += int(t) * factor
        factor *= 60
    return wait

def get_chrome_version():
    br_ver = OperationSystemManager().get_browser_version_from_os(ChromeType.GOOGLE)
    return int(br_ver.split('.')[0])