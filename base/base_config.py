#_*_coding:utf-8_*_

from globalVar import gl
from library import scripts
import os

class BaseConfig(object):

    def __init__(self):
        self.yamlConfigPath = os.path.join(gl.configPath, 'config.yaml')

    @property
    def base_url(self):
        confData = scripts.getYamlfield(self.yamlConfigPath)
        return confData['BASE_URL']


if __name__=="__main__":
    print BaseConfig().base_url