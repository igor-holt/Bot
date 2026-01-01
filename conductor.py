import os
import yaml
import main


def parse_env_to_config():
    """Parse environment variables and write to config.yaml"""
    config = {
        'exchange': os.environ.get('EXCHANGE', ''),
        'api': os.environ.get('API', ''),
        'secret': os.environ.get('SECRET', ''),
        'wallet': os.environ.get('WALLET', '')
    }
    
    with open('config.yaml', 'w') as config_file:
        yaml.dump(config, config_file, default_flow_style=False)
    
    print(f"Configuration written to config.yaml: {config}")


if __name__ == "__main__":
    parse_env_to_config()
    main.main_loop()
