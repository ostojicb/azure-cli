# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "database-fleet-manager fleet tier disable",
    is_preview=True,
)
class Disable(AAZCommand):
    """Disables a tier.
    """

    _aaz_info = {
        "version": "2023-08-01-preview",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.databasefleetmanager/fleets/{}/tiers/{}/disable", "2023-08-01-preview"],
        ]
    }

    def _handler(self, command_args):
        super()._handler(command_args)
        self._execute_operations()
        return self._output()

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.fleet_name = AAZStrArg(
            options=["--fleet-name"],
            required=True,
            id_part="name",
            fmt=AAZStrArgFormat(
                pattern="^(?!.*--)[a-z0-9]+(?:-[a-z0-9]+)*$",
            ),
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        _args_schema.tier_name = AAZStrArg(
            options=["--tier-name"],
            required=True,
            id_part="child_name_1",
            fmt=AAZStrArgFormat(
                pattern="^(?!.*--)[a-z0-9]+(?:-[a-z0-9]+)*$",
            ),
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.FleetTiersDisable(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class FleetTiersDisable(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DatabaseFleetManager/fleets/{fleetName}/tiers/{tierName}/disable",
                **self.url_parameters
            )

        @property
        def method(self):
            return "POST"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "fleetName", self.ctx.args.fleet_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
                **self.serialize_url_param(
                    "tierName", self.ctx.args.tier_name,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2023-08-01-preview",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()

            _schema_on_200 = cls._schema_on_200
            _schema_on_200.id = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.name = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.properties = AAZObjectType()
            _schema_on_200.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.properties
            properties.capacity = AAZIntType()
            properties.database_capacity_max = AAZFloatType(
                serialized_name="databaseCapacityMax",
            )
            properties.database_capacity_min = AAZFloatType(
                serialized_name="databaseCapacityMin",
            )
            properties.database_size_gb_max = AAZIntType(
                serialized_name="databaseSizeGbMax",
            )
            properties.disabled = AAZBoolType(
                flags={"read_only": True},
            )
            properties.family = AAZStrType()
            properties.num_of_empty_preprovisioned_databases = AAZIntType(
                serialized_name="numOfEmptyPreprovisionedDatabases",
            )
            properties.pool_num_of_databases_max = AAZIntType(
                serialized_name="poolNumOfDatabasesMax",
            )
            properties.pooled = AAZBoolType()
            properties.serverless = AAZBoolType()
            properties.service_tier = AAZStrType(
                serialized_name="serviceTier",
            )

            return cls._schema_on_200


class _DisableHelper:
    """Helper class for Disable"""


__all__ = ["Disable"]
