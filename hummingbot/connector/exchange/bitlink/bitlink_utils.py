from decimal import Decimal
from typing import Any, Dict

from pydantic import Field, SecretStr

from hummingbot.client.config.config_data_types import BaseConnectorConfigMap, ClientFieldData
from hummingbot.core.data_type.trade_fee import TradeFeeSchema

CENTRALIZED = True
EXAMPLE_PAIR = "BTC-USDT"
DEFAULT_FEES = TradeFeeSchema(
    maker_percent_fee_decimal=Decimal("0.001"),
    taker_percent_fee_decimal=Decimal("0.001"),
)


# def is_exchange_information_valid(exchange_info: Dict[str, Any]) -> bool:
#     """
#     Verifies if a trading pair is enabled to operate with based on its exchange information
#     :param exchange_info: the exchange information for a trading pair
#     :return: True if the trading pair is enabled, False otherwise
#     """
#     return exchange_info.get("showStatus") is True


class BitlinkConfigMap(BaseConnectorConfigMap):
    connector: str = Field(default="bitlink", const=True, client_data=None)
    
    bitlink_api_key: SecretStr = Field(
        default=...,
        client_data=ClientFieldData(
            prompt=lambda cm: "Enter your Bitlink API key",
            is_secure=True,
            is_connect_key=True,
            prompt_on_new=True,
        ),
    )
    bitlink_api_secret: SecretStr = Field(
        default=...,
        client_data=ClientFieldData(
            prompt=lambda cm: "Enter your Bitlink API secret",
            is_secure=True,
            is_connect_key=True,
            prompt_on_new=True,
        ),
    )

    class Config:
        title = "bitlink"


KEYS = BitlinkConfigMap.construct()

OTHER_DOMAINS = ["bitlink_testnet"]
OTHER_DOMAINS_PARAMETER = {"bitlink_testnet": "bitlink_testnet"}
OTHER_DOMAINS_EXAMPLE_PAIR = {"bitlink_testnet": "BTC-USDT"}
OTHER_DOMAINS_DEFAULT_FEES = {"bitlink_testnet": DEFAULT_FEES}


class BitlinkTestnetConfigMap(BaseConnectorConfigMap):
    connector: str = Field(default="bitlink_testnet", const=True, client_data=None)
    
    bitlink_testnet_api_key: SecretStr = Field(
        default=...,
        client_data=ClientFieldData(
            prompt=lambda cm: "Enter your Bitlink Testnet API Key",
            is_secure=True,
            is_connect_key=True,
            prompt_on_new=True,
        ),
    )
    bitlink_testnet_api_secret: SecretStr = Field(
        default=...,
        client_data=ClientFieldData(
            prompt=lambda cm: "Enter your Bitlink Testnet API secret",
            is_secure=True,
            is_connect_key=True,
            prompt_on_new=True,
        )
    )
    
    # bitlink_testnet_api_key: SecretStr =("Qn0LX1JY7hZVAHkQnVWaBpkzf0jZx6vKaZyLFTwwTEZ3iusCQ86mwfaILZrtMyR0")
    # bitlink_testnet_api_secret: SecretStr =("o2pSNYMhiuLypkyesHVFvz9CSdX7Fq7wstpVtQSFiiWvf16ib8hfQHMzl8kzEDgllhz")

    class Config:
        title = "bitlink_testnet"


OTHER_DOMAINS_KEYS = {"bitlink_testnet": BitlinkTestnetConfigMap.construct()}
