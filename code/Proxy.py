from java import import_pyjinn_script, ScriptObject

class PyJinnProxy:
    script = None

    @classmethod
    def bind_script(cls, name: str):
        cls.script = import_pyjinn_script(name)
        return cls.script

    @classmethod
    def bind_script_object(cls, script: ScriptObject):
        cls.script = script
        return cls.script

    def __init__(self, class_name: str):
        self._class_name = class_name
        self._pyj_class_cache = None

    def _pyj_class(self):
        if PyJinnProxy.script is None:
            raise RuntimeError("PyJinn script is not set on PyJinnProxy.script")
        
        if self._pyj_class_cache is None:
            self._pyj_class_cache = PyJinnProxy.script.get(self._class_name)
        return self._pyj_class_cache

    def __getattr__(self, name: str):
        target = self._pyj_class()
        try:
            value = getattr(target, name)
        except Exception:
            value = target[name]

        setattr(self, name, value)
        return value

    def __call__(self, *args, **kwargs):
        return self._pyj_class()(*args, **kwargs)
