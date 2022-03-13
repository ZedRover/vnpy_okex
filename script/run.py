from vnpy.event import EventEngine
from vnpy.trader.engine import MainEngine
from vnpy_okex import OkexGateway
from vnpy_ctp import CtpGateway
config = {
    "API Key":"5e3e9503-35a8-4626-a4ff-095c69109e40",
    "Secret Key":"FF492EEB3396D13999713D9026E3C823",
    "Passphrase": "Aa123456",
    "会话数": 3,
    "代理地址": "",
    "代理端口": "",
    "服务器": ["REST","TEST"]
}

if __name__=='__main__':
    event_engine = EventEngine()
    main_engine = MainEngine(event_engine)
    main_engine.add_gateway(OkexGateway)
    main_engine.connect(config,'')
