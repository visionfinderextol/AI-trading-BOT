"""KeitaroAI Bot — Secure Launcher."""

import importlib.util, sys, os

os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), "src"))

def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod

load("engine", "core/engine.pyc")
load("server", "server.pyc")
app_mod = load("app", "app.pyc")
app_mod.main()
