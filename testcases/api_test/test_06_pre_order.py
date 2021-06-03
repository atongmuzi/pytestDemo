import pytest
import allure
from operation.order import pre_trade
from testcases.conftest import api_data
from common.logger import logger


@allure.step("-----下单前的预下单、点击支付按钮的接口-----")
def step_1(order_type, item_id, sku_no, use_pcoin):
    order_type = {1: lambda: '盲盒', 2: lambda: '摆件', 3: lambda: '一番赏'}[order_type]()
    use_pcoin = {False: lambda: '不使用', True: lambda: '使用'}[use_pcoin]()
    logger.info("下单类型为：{}, 商品ID为：{}, sku_no为：{}, 是否使用P币：{}".format(order_type, item_id, sku_no, use_pcoin))


class TestUserTrade():
    """用户下单"""
    @pytest.mark.parametrize(
        "order_type, item_id, sku_type, sku_no, act_id_list, use_pcoin,"
        " except_result, except_code, except_msg",api_data["test_pre_trade"])
    def test_user_pre_trade(self, order_type, item_id, sku_type, sku_no, act_id_list, use_pcoin, except_result, except_code, except_msg):
        logger.info("**********开始执行测试用例**********")
        result = pre_trade(order_type, item_id, sku_type, sku_no, act_id_list, use_pcoin)
        step_1(order_type, item_id, sku_no, use_pcoin)


