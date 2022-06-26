from SQLAlchemyGenerator import SQLAlchemyGenerator
from PydanticGenerator import PydanticGenerator
from FastAPIGenerator import FastAPIGenerator
from SQLGenerator import SQLGenerator
from DockerComposeGenerator import DockerComposeGenerator
from RelationshipHandler import RelationshipHandler
from view import Input

resources = [
    {
        "name": "Customer",
        "table_name": "Customers",
        "fields": [
            {
                "name": "custid",
                "type": "integer",
                "nullable": False
            },
            {
                "name": "name",
                "type": "string",
                "length": 45,
                "nullable": True
            },
            {
                "name": "address",
                "type": "string",
                "length": 40,
                "nullable": True
            },
            {
                "name": "city",
                "type": "string",
                "length": 30,
                "nullable": True
            },
            {
                "name": "state",
                "type": "string",
                "length": 2,
                "nullable": True
            },
            {
                "name": "zip",
                "type": "string",
                "length": 9,
                "nullable": True
            },
            {
                "name": "area",
                "type": "integer",
                "nullable": True
            },
            {
                "name": "phone",
                "type": "string",
                "length": 9,
                "nullable": True
            },
            {
                "name": "repid",
                "type": "integer",
                "nullable": False
            },
            {
                "name": "creditlimit",
                "type": "decimal",
                "nullable": True
            }
        ],
        "primary_key": "custid",
        "relationships": [
            {
                "type": "ONE-TO-MANY",
                "table": "Ord",
                "reference_field": "custid"
            }
        ]
    },
    {
        "name": "Order",
        "table_name": "Ord",
        "fields": [
            {
                "name": "ordid",
                "type": "integer",
                "nullable": False
            },
            {
                "name": "total",
                "type": "decimal",
                "nullable": True
            },
            {
                "name": "totaltva",
                "type": "decimal",
                "nullable": True
            }
        ],
        "primary_key": "ordid",
        "relationships": [
            {
                "type": "ONE-TO-MANY",
                "table": "Items",
                "reference_field": "ordid"
            }
        ]
    },
    {
        "name": "Product",
        "table_name": "Products",
        "fields": [
            {
                "name": "prodid",
                "type": "integer",
                "nullable": False
            },
            {
                "name": "descrip",
                "type": "string",
                "length": 30,
                "nullable": True
            },
            {
                "name": "vat",
                "type": "decimal",
                "nullable": True
            },
            {
                "name": "exp_date",
                "type": "date",
                "nullable": True
            }
        ],
        "primary_key": "prodid",
        "relationships": [
            {
                "type": "ONE-TO-MANY",
                "table": "Items",
                "reference_field": "prodid"
            }
        ]
    },
    {
        "name": "Item",
        "table_name": "Items",
        "fields": [
            {
                "name": "itemid",
                "type": "integer",
                "nullable": False
            },
            {
                "name": "actualprice",
                "type": "decimal",
                "nullable": True
            },
            {
                "name": "qty",
                "type": "integer",
                "nullable": True
            },
            {
                "name": "itemtot",
                "type": "decimal",
                "nullable": True
            },
            {
                "name": "tva",
                "type": "decimal",
                "nullable": True
            },
            {
                "name": "itemgen",
                "type": "decimal",
                "nullable": True
            },
            {
                "name": "guarantee",
                "type": "integer",
                "nullable": True
            },
            {
                "name": "exp_date",
                "type": "date",
                "nullable": True
            }
        ],
        "primary_key": "itemid"
    }
]

if __name__ == "__main__":
    res = {"resources": resources}
    r = RelationshipHandler(Input(**res).resources)
    r.execute()
    resources = [resource.dict() for resource in r.resources]

    sqlalchemy_generator = SQLAlchemyGenerator(resources)
    pydantic_generator = PydanticGenerator(resources)
    fastapi_generator = FastAPIGenerator(resources)
    sql_generator = SQLGenerator(resources)
    docker_generator = DockerComposeGenerator()

    docker_generator.generate()
    sql_generator.generate()
    sqlalchemy_generator.generate()
    pydantic_generator.generate()
    fastapi_generator.generate()
