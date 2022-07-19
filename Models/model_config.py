# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = config_from_dict(json.loads(json_string))

from typing import Any, TypeVar, Type, cast


T = TypeVar("T")


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


class EmailSettings:
    port: int
    smtp_server: str
    password: str
    from_email: str
    to_email: str
    email_subject: str
    email_message: str

    def __init__(self, port: int, smtp_server: str, password: str, from_email: str, to_email: str, email_subject: str, email_message: str) -> None:
        self.port = port
        self.smtp_server = smtp_server
        self.password = password
        self.from_email = from_email
        self.to_email = to_email
        self.email_subject = email_subject
        self.email_message = email_message

    @staticmethod
    def from_dict(obj: Any) -> 'EmailSettings':
        assert isinstance(obj, dict)
        port = from_int(obj.get("port"))
        smtp_server = from_str(obj.get("smtpServer"))
        password = from_str(obj.get("password"))
        from_email = from_str(obj.get("fromEmail"))
        to_email = from_str(obj.get("toEmail"))
        email_subject = from_str(obj.get("emailSubject"))
        email_message = from_str(obj.get("emailMessage"))
        return EmailSettings(port, smtp_server, password, from_email, to_email, email_subject, email_message)

    def to_dict(self) -> dict:
        result: dict = {}
        result["port"] = from_int(self.port)
        result["smtpServer"] = from_str(self.smtp_server)
        result["password"] = from_str(self.password)
        result["fromEmail"] = from_str(self.from_email)
        result["toEmail"] = from_str(self.to_email)
        result["emailSubject"] = from_str(self.email_subject)
        result["emailMessage"] = from_str(self.email_message)
        return result


class Config:
    email_settings: EmailSettings
    default_refresh_delay: int
    default_stock_code: str

    def __init__(self, email_settings: EmailSettings, default_refresh_delay: int, default_stock_code: str) -> None:
        self.email_settings = email_settings
        self.default_refresh_delay = default_refresh_delay
        self.default_stock_code = default_stock_code

    @staticmethod
    def from_dict(obj: Any) -> 'Config':
        assert isinstance(obj, dict)
        email_settings = EmailSettings.from_dict(obj.get("emailSettings"))
        default_refresh_delay = int(from_str(obj.get("defaultRefreshDelay")))
        default_stock_code = from_str(obj.get("defaultStockCode"))
        return Config(email_settings, default_refresh_delay, default_stock_code)

    def to_dict(self) -> dict:
        result: dict = {}
        result["emailSettings"] = to_class(EmailSettings, self.email_settings)
        result["defaultRefreshDelay"] = from_str(str(self.default_refresh_delay))
        result["defaultStockCode"] = from_str(self.default_stock_code)
        return result


def config_from_dict(s: Any) -> Config:
    return Config.from_dict(s)


def config_to_dict(x: Config) -> Any:
    return to_class(Config, x)
