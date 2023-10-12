import os.path
from utils import build_and_expect_default, build_unittests_and_expect_success, build_reports_and_expect_success


class Test_CustA__Var1:
    @classmethod
    def setup_class(cls):
        cls.variant = "CustA/Var1"

    def test_unit_tests(self):
        build_unittests_and_expect_success(self.variant)

    def test_build(self):
        build_and_expect_default(self.variant)

    def test_reports(self):
        build_reports_and_expect_success(self.variant)

        """SWE.4 reports shall be created"""
        report_types = ["html", "coverage"]
        modules = ["magical_number"]
        for report_type in report_types:
            for module in modules:
                assert os.path.isfile(f"build/{self.variant}/test/src/{module}/reports/{report_type}/index.html")
