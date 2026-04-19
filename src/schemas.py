from pydantic import BaseModel, ConfigDict, Field, AliasPath

class BaseIntegrationSchema(BaseModel):
    model_config = ConfigDict(
        extra='ignore',
        str_strip_whitespace=True
    )

class Users(BaseIntegrationSchema):
    id: int
    name: str = None
    username: str
    email: str = None
    phone: str = None
    website: str = None
    address_street: str | None = Field(validation_alias=AliasPath('address', 'street'))
    address_suite: str | None = Field(validation_alias=AliasPath('address', 'suite'))
    address_city: str | None = Field(validation_alias=AliasPath('address', 'city'))
    address_zipcode: str | None = Field(validation_alias=AliasPath('address', 'zipcode'))
    address_geo_lat: str | None = Field(validation_alias=AliasPath('address', 'geo', 'lat'))
    address_geo_lng: str | None = Field(validation_alias=AliasPath('address', 'geo', 'lng'))
    company_name: str | None = Field(validation_alias=AliasPath('company', 'name'))
    company_catchPhrase: str | None = Field(validation_alias=AliasPath('company', 'catchPhrase'))
    company_bs: str | None = Field(validation_alias=AliasPath('company', 'bs'))

class Posts(BaseIntegrationSchema):
    id: int
    userId: int
    title: str
    body: str = None

class Comments(BaseIntegrationSchema):
    id: int
    postId: int
    name: str
    email: str
    body: str = None