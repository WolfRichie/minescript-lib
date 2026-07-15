from java import import_pyjinn_script, ScriptObject

class PyJinnProxyMeta(type):
    script = None

    @classmethod
    def bind_script(cls, name: str):
        cls.script = import_pyjinn_script(name)
        return cls.script

    @classmethod
    def bind_script_object(cls, script: ScriptObject):
        cls.script = script
        return cls.script

    def _ensure_cache(cls):
        if "_pyj_class_cache" not in cls.__dict__:
            type.__setattr__(cls, "_pyj_class_cache", None)
        if "_pyj_member_cache" not in cls.__dict__:
            type.__setattr__(cls, "_pyj_member_cache", {})

    def _pyj_class(cls):
        cls._ensure_cache()
        if PyJinnProxyMeta.script is None:
            raise RuntimeError("PyJinn script is not set on PyJinnProxyMeta.script")
        cached = cls.__dict__.get("_pyj_class_cache")
        if cached is None:
            cached = PyJinnProxyMeta.script.get(cls.__name__)
            type.__setattr__(cls, "_pyj_class_cache", cached)
        return cached

    def __getattr__(cls, name: str):
        cls._ensure_cache()
        member_cache = cls.__dict__.get("_pyj_member_cache")
        if name in member_cache:
            return member_cache[name]

        target = cls._pyj_class()
        try:
            value = getattr(target, name)
        except Exception:
            value = target[name]

        member_cache[name] = value
        type.__setattr__(cls, name, value)
        return value

    def __call__(cls, *args, **kwargs):
        target_class = cls._pyj_class()
        return target_class(*args, **kwargs)


class PyJinnProxy(metaclass=PyJinnProxyMeta):
  pass