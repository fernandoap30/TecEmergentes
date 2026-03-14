from dataclasses import dataclass
@dataclass
class RUC:
    razon_social: str = ""
    estado: str = ""
    condicion: str = ""
    direccion: str = ""
    distrito: str = ""
    provincia: str = ""
    dpto: str = ""
    @classmethod
    def desde_dict(cls, data: dict) -> "RUC":
        return cls(
            razon_social=data.get("razon_social", ""),
            estado=data.get("estado", ""),
            condicion=data.get("condicion", ""),
            direccion=data.get("direccion", ""),
            distrito=data.get("distrito", ""),
            provincia=data.get("provincia", ""),
            dpto=data.get("dpto", ""),
        )
@dataclass
class DNI:
    first_name: str = ""
    full_name: str = ""
    first_last_name: str = ""
    second_last_name: str = ""
    document_number: str = ""
    @classmethod
    def desde_dict(cls, data: dict) -> "DNI":
        return cls(
            first_name=data.get("first_name", ""),
            full_name=data.get("full_name", ""),
            first_last_name=data.get("first_last_name", ""),
            second_last_name=data.get("second_last_name", ""),
            document_number=data.get("document_number", ""),
        )