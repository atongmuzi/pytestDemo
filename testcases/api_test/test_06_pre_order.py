import pytest
import allure
from operation.order import pre_trade
from testcases.conftest import api_data
from common.logger import logger


@allure.step("-----下单前的预下单-----")
def step_1(order_type, item_id, sku_no, use_pcoin):
    order_type = {0: lambda: '盲盒', 1: lambda: '摆件', 2: lambda: '一番赏'}[order_type]();
    use_pcoin = {}
    logger.info("下单类型为：{},商品ID为：{},sku_no为：{},使用P币：{}".format(order_type, item_id, sku_no, use_pcoin))

