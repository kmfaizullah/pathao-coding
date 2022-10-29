def serializer_perform_create(serializer, *args, **kwargs) -> dict:
    serializer.is_valid(raise_exception=True)
    new_obj = serializer.save()
    return new_obj, serializer.data