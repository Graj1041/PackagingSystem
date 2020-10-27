import os,sys
import shutil
from Utilities.customLogger import LogGen
from Utilities.readConfigFile import ConfigReader
import pytest

class Test_Packaging_System:

    logger = LogGen.log_gen()

    @pytest.fixture()
    def setup(self, setupEnv):
        self.destination_file, self.cfg_file_path, self.layout_type = setupEnv
        self.logger.info('Input destination file :: ' + self.destination_file)
        self.logger.info('Input config file path :: ' + self.cfg_file_path)
        self.logger.info('Input layout type :: ' + self.layout_type)

        if self.destination_file is None:
            self.logger.error("Please enter destination file, it can not be empty")
            assert False
        else:
            if not os.path.exists(self.destination_file):
                os.mkdir(self.destination_file)

        if self.cfg_file_path is None:
            self.logger.error("Please enter config file path, it can not be empty")
            assert False
        else:
            if not os.path.exists(self.cfg_file_path):
                self.logger.error("Config file path doesn't exists, please enter correct config file path")
                assert False

        if self.layout_type is None:
            self.logger.error("Please enter layout type, it can not be empty")
            assert False
        else:
            if self.layout_type not in ['Release', 'Debug', 'Both']:
                self.logger.error("Kindly enter correct layout type")
                assert False

        self.l_src, self.l_dest = ConfigReader.read_config(self.cfg_file_path, self.layout_type)

    def test_copyingRecords(self,setup):
        self.logger.info('Copying the records of ' + self.layout_type + ' layout type from given source to destination path')
        for i in range(len(self.l_dest)):
            self.logger.info('Copying binaries from ' + self.l_src[i] + ' to ' + self.l_dest[i])
            shutil.copytree(self.l_src[i], self.l_dest[i])

        for dest in self.l_dest:
            self.logger.info('Moving destination directory ' + dest + ' to ' + self.destination_file)
            shutil.move(dest, self.destination_file)

        self.logger.info('creating zip file after copying the records of layout type ' + self.layout_type)
        shutil.make_archive(self.destination_file, 'zip', root_dir=self.destination_file)

        self.logger.info('removing the temp file ' + self.destination_file)
        shutil.rmtree(self.destination_file)

        if os.path.exists(self.destination_file + '.zip'):
            self.logger.info('Packaging is successful for given layout type ' + self.layout_type)
            assert True
        else:
            self.logger.info('Packaging is unsuccessful for given layout type ' + self.layout_type)
            assert False
