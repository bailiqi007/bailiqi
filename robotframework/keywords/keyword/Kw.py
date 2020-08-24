import os
import sys
# cur_filepath = os.path.dirname(__file__)
sys.path.append(r"e:\\0_github仓库\\bailiqi\\robotframework")

from lib.robot_ext.rf_keyword.rf_logger import logger


class Kw:
    def create_github_repo(self, name):
        logger.info("info 的打印日志")
        return "Created repo with name: " + name

    def get_github_repo(self):
        logger.debug("debug 的打印日志")
        return "Getting repos now..."


class ClsWithDifName:
    def delete_github_repo(self, name):
        logger.error("error  的打印日志")
        return "Deleting repo with name: " + name


if __name__ == "__main__":
    logger.debug("hello wo shi zmy")
    logger.info("info ....")
    logger.error("error ....")