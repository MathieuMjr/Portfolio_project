from app import create_app
import sys
import config

if len(sys.argv) <= 1:
    print("App runned with default config")
    app = create_app()
else:
    config_name = getattr(config, sys.argv[1])
    print(f"App runned with {config_name}")
    app = create_app(config_name)


if __name__ == '__main__':
    app.run()
