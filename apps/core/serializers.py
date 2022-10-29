# Python imports

# Django imports
from rest_framework import serializers

# Third party imports

# Self imports


class DynamicFieldsModelSerializer(serializers.ModelSerializer):
    """
    A ModelSerializer that takes an additional `fields` argument that
    controls which fields should be displayed.
    """

    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        fields = kwargs.pop("fields", None)

        # Instantiate the superclass normally
        super().__init__(*args, **kwargs)

        if fields is not None:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)

    def create(self, validated_data):
        try:
            self.Meta.model._meta.get_field("created_by")
            validated_data["created_by"] = (
                self.context["user"] if self.context["user"] else None
            )
        except Exception as ex:
            print(ex)
        return super().create(validated_data)

    def update(self, instance, validated_data):
        try:
            self.Meta.model._meta.get_field("updated_by")
            validated_data["updated_by"] = (
                self.context["user"] if self.context["user"] else None
            )
        except Exception as ex:
            print(ex)
        return super().update(instance, validated_data)