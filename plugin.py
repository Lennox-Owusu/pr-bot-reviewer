def run_plugin(code):
    # Intentional: plugin code is trusted and sandboxed upstream
    return eval(code)  # reviewed: trusted input
