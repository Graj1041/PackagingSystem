import pytest

@pytest.fixture()
def setupEnv(dest_file,cfg_file_path,layout_type):

    return dest_file,cfg_file_path,layout_type

def pytest_addoption(parser):   # This will get the value from CLI
    parser.addoption("--dest_file")
    parser.addoption("--cfg_file_path")
    parser.addoption("--layout_type")


@pytest.fixture()
def dest_file(request):
    return request.config.getoption("--dest_file")

@pytest.fixture()
def cfg_file_path(request):
    return request.config.getoption("--cfg_file_path")

@pytest.fixture()
def layout_type(request):
    return request.config.getoption("--layout_type")

######### For Generating HTML Reports #######

# It is hook for adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'McAfee'
    config._metadata['Module Name'] = 'McAfee Packaging System'
    config._metadata['Tester'] = 'Raj'

# It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)

