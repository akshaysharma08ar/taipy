from taipy.config import Config, GlobalAppConfig
from taipy.config._config import _Config
from taipy.config.checker import IssueCollector
from taipy.config.checker.checkers.gLobal_config_checker import GlobalConfigChecker


class TestGlobalConfigChecker:
    def test_check_notification_field_is_bool(self):
        collector = IssueCollector()
        config = _Config()
        GlobalConfigChecker(config, collector).check()
        assert len(collector.errors) == 1
        assert collector.errors[0].field == GlobalAppConfig.NOTIFICATION_KEY
        assert collector.errors[0].value is None

        config.global_config.notification = True
        collector = IssueCollector()
        GlobalConfigChecker(config, collector).check()
        assert len(collector.errors) == 0

        config.global_config.notification = False
        collector = IssueCollector()
        GlobalConfigChecker(config, collector).check()
        assert len(collector.errors) == 0
